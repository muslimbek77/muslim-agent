import json
import re
from pathlib import Path

import numpy as np

from config import BASE_DIR


def normalize_text(text):
    """Matnni kichik harflarga o'tkazib, keraksiz belgilarni olib tashlaydi.

    Bu funksiya qidiruv va vektor yaratishda bir xil formatdagi matn
    hosil qilish uchun ishlatiladi, shuning uchun "Muslim" va "muslim"
    kabi qiymatlar bir xil hisoblanadi.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\u0410-\u044f\u04e0-\u04ff\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text):
    """Matnni so'z tokenlarga ajratib qaytaradi.

    Har bir chunk va foydalanuvchi savoli uchun so'zlar to'plami chiqariladi,
    keyin bu so'zlar vektor ko'rinishga aylantiriladi.
    """
    return [token for token in normalize_text(text).split() if token]


class SimpleVectorStore:
    """JSON faylga saqlanadigan oddiy vektor ma'lumotlar ombori.

    Bu loyiha uchun yetarli bo'lgan yengil yechim: har bir chunk uchun
    bag-of-words vektori yaratiladi va rag_index.json fayliga saqlanadi.
    """

    def __init__(self, chunks, index_path=None):
        """Vektor indeksini yaratish yoki mavjud fayldan yuklash."""
        self.index_path = Path(index_path) if index_path else BASE_DIR / "rag_index.json"
        self.chunks = chunks

        if self.index_path.exists():
            self._load_from_disk()
        else:
            self.vocab = self._build_vocab(chunks)
            self.matrix = self._build_matrix(chunks, self.vocab)
            self.save()

    @staticmethod
    def _build_vocab(chunks):
        """Barcha chunklardan barchasini o'z ichiga olgan so'zlar lug'atini tayyorlaydi."""
        vocabulary = set()
        for chunk in chunks:
            vocabulary.update(tokenize(chunk["body"]))
        return sorted(vocabulary)

    @staticmethod
    def _term_frequency(text, vocab):
        """So'zlar sonini hisoblab, vektor ko'rinishiga o'tkazadi.

        Masalan: {"muslim": 2, "agent": 1} kabi qiymatlar vektor ichida
        saqlanadi. Bu har bir chunk uchun umumiy "semantic" ko'rsatkichdir.
        """
        counts = {word: 0 for word in vocab}
        for token in tokenize(text):
            if token in counts:
                counts[token] += 1
        return np.array([counts[word] for word in vocab], dtype=float)

    @classmethod
    def _build_matrix(cls, chunks, vocab):
        """Har bir chunk uchun vektor matritsasini quradi."""
        if not vocab:
            return np.zeros((0, 0), dtype=float)

        matrix = []
        for chunk in chunks:
            vector = cls._term_frequency(chunk["body"], vocab)
            matrix.append(vector)
        return np.vstack(matrix) if matrix else np.zeros((0, len(vocab)), dtype=float)

    @staticmethod
    def _cosine_similarity(left, right):
        """Ikki vektor orasidagi o'xshashlik darajasini hisoblaydi."""
        left_norm = np.linalg.norm(left)
        right_norm = np.linalg.norm(right)
        if left_norm == 0 or right_norm == 0:
            return 0.0
        return float(np.dot(left, right) / (left_norm * right_norm))

    def _embed_query(self, query, vocab):
        """Foydalanuvchi savolini bir xil vektor bo'shliqqa o'giradi."""
        if not vocab:
            return np.zeros(0, dtype=float)
        return self._term_frequency(query, vocab)

    def save(self):
        """Vektor indeksi va chunk ma'lumotlarini rag_index.json fayliga yozadi."""
        payload = {
            "vocab": self.vocab,
            "chunks": [{"title": chunk["title"], "body": chunk["body"]} for chunk in self.chunks],
            "matrix": self.matrix.tolist(),
        }
        self.index_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def _load_from_disk(self):
        """Oldin saqlangan vektor indeksini diskdan qayta yuklaydi."""
        payload = json.loads(self.index_path.read_text(encoding="utf-8"))
        self.vocab = payload.get("vocab", [])
        self.chunks = payload.get("chunks", [])
        matrix = np.array(payload.get("matrix", []), dtype=float)
        self.matrix = matrix if matrix.size else np.zeros((0, len(self.vocab)), dtype=float)

    def retrieve(self, query, top_k=3):
        """Savolga eng mos keladigan chunklarni topib qaytaradi.

        Bu usul vektorlar orasidagi kosinus o'xshashligini hisoblab, eng yuqori
        ball olgan chunklarni tanlaydi.
        """
        query_tokens = tokenize(query)
        if not query_tokens:
            return []

        query_vector = self._embed_query(query, self.vocab)
        if len(self.vocab) == 0 or self.matrix.size == 0:
            return []

        similarities = []
        for index, chunk in enumerate(self.chunks):
            sim = self._cosine_similarity(self.matrix[index], query_vector)
            if sim > 0:
                similarities.append({
                    "title": chunk["title"],
                    "body": chunk["body"],
                    "score": sim,
                })

        similarities.sort(key=lambda item: item["score"], reverse=True)
        return similarities[:top_k]


class RAGKnowledgeBase:
    """Markdown faylni o'qib, chunklarga ajratib, lokal vektor indeksini yaratadi.

    Bu klass loyiha ma'lumotlarini RAG tizimi uchun tayyorlaydi: chunklarni
    yuklaydi, vektor storega kiritadi va foydalanuvchi savoliga mos kontekstni
    tayyorlaydi.
    """

    def __init__(self, knowledge_base_path=None, index_path=None):
        """Ma'lumotlar bazasi va indeks fayllari yo'lini belgilaydi."""
        self.path = Path(knowledge_base_path) if knowledge_base_path else BASE_DIR / "muslim_agent_rag_knowledge_base.md"
        self.index_path = Path(index_path) if index_path else BASE_DIR / "rag_index.json"
        self.chunks = self._load_chunks()
        self.vector_store = SimpleVectorStore(self.chunks, index_path=self.index_path)

    def _load_chunks(self):
        """Markdown fayldan "## CHUNK " orqali ajratilgan bo'limlarni o'qib oladi."""
        if not self.path.exists():
            return []

        text = self.path.read_text(encoding="utf-8")
        sections = []
        for section in text.split("## CHUNK "):
            if not section.strip():
                continue
            lines = section.strip().splitlines()
            title = lines[0].strip() if lines else "Chunk"
            body = "\n".join(lines)
            sections.append({"title": title, "body": body})
        return sections

    def retrieve(self, query, top_k=3):
        """Savolga mos keladigan maxsus chunklarni topib qaytaradi."""
        return self.vector_store.retrieve(query, top_k=top_k)

    def build_prompt(self, user_input):
        """Topilgan chunklar asosida prompt yaratadi.

        Bu prompt modelga yuboriladi va javobning ishonchliligi oshadi,
        chunki model savolga haqiqiy ma'lumotlarni o'qigan holda javob beradi.
        """
        matches = self.retrieve(user_input, top_k=3)
        if not matches:
            return user_input

        context = "\n\n".join(
            f"--- {match['title']} ---\n{match['body'][:1400]}"
            for match in matches
        )

        return (
            "Sizga quyidagi RAG bilimlar bazasi konteksti beriladi. "
            "Bu kontekstdan faqat tegishli ma'lumotlarni ishlatib javob bering. "
            "Agar ma'lumot yetarli bo'lmasa, buni ayting va xulosaga kelmang.\n\n"
            f"Knowledge base context:\n{context}\n\nUser question: {user_input}"
        )
