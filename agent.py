import anthropic
from termcolor import colored

from config import API_KEY, MAX_TOKENS, MODEL, require_api_key
from file_tools import append_file, build_project_context, list_dir, read_file, resolve_path, write_file
from rag_store import RAGKnowledgeBase


class MuslimAgent:
    """A small terminal-based AI assistant with file tools and a lightweight RAG layer."""

    def __init__(self):
        # Validate the configuration before creating the Anthropic client.
        require_api_key()
        self.client = anthropic.Anthropic(api_key=API_KEY)
        self.conversation = []
        self.rag_store = RAGKnowledgeBase()
        self.system_prompt = """
        Siz Muslim Agent bo'lsangiz. Quyidagi qoidalarga rioya qiling:
        - Savol va javobni aniq, tushunarli qilib bering.
        - O'zbek tilida javob bering.
        - Faylni ochish va yozish kerak bo'lsa, /read, /write, /append, /ls buyruqlaridan foydalaning.
        - Agar biror narsa noma'lum bo'lsa, buni ayting.
        - Agar foydalanuvchi loyihani tushuntirishni so'rasa, dastur katalogini ko'rib, muhim fayllarni o'qib asosli javob bering.
        """

    def get_message(self):
        """Prompt the user for input and normalize it."""
        return input(colored("Enter your message: ", "green")).strip()

    def process_command(self, user_input):
        """Handle simple slash commands used for file interaction."""
        if user_input.startswith("/read "):
            target = user_input[len("/read "):].strip()
            return read_file(target)

        if user_input.startswith("/write "):
            payload = user_input[len("/write "):].strip()
            if " || " in payload:
                file_path, content = payload.split(" || ", 1)
            else:
                file_path = payload
                content = input(colored("Yangi fayl matnini kiriting: ", "green"))
            return write_file(file_path, content)

        if user_input.startswith("/append "):
            payload = user_input[len("/append "):].strip()
            if " || " in payload:
                file_path, content = payload.split(" || ", 1)
            else:
                file_path = payload
                content = input(colored("Qo'shiladigan matnni kiriting: ", "green"))
            return append_file(file_path, content)

        if user_input.startswith("/ls"):
            rest = user_input[3:].strip()
            target = rest or "."
            return list_dir(target)

        return None

    def should_inspect_project(self, user_input):
        """Detect whether the user is asking for a project-level explanation."""
        text = user_input.lower()
        project_questions = [
            "how does this project work",
            "what does this project do",
            "what is this project",
            "explain this project",
            "projectni tushuntir",
            "loyihani tushuntir",
            "how this project works",
            "how does this app work",
            "explain the project",
            "what is the app",
        ]
        return any(phrase in text for phrase in project_questions)

    def run_inference(self, prompt_text=None):
        """Send the current prompt to the Claude model with the configured system prompt."""
        messages = self.conversation.copy()
        if prompt_text is not None:
            messages.append({"role": "user", "content": prompt_text})

        return self.client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=self.system_prompt,
            messages=messages,
        )

    def display_response(self, response):
        """Render the text blocks from the model response."""
        for content in response.content:
            if getattr(content, "type", None) == "text":
                print(colored("\nMuslim Agent: ", "blue", attrs=["bold"]) + content.text)

    def run(self):
        """Main interactive loop for the agent."""
        print(colored("\nChat with the Muslim Agent.", "cyan", attrs=["bold"]))
        print("Type 'exit' to quit. File commands: /read, /write, /append, /ls\n")

        while True:
            try:
                user_input = self.get_message()
                if not user_input:
                    continue

                if user_input.lower() in ["exit", "quit"]:
                    print(colored("\nMuslim Agent stopped.", "yellow"))
                    break

                tool_result = self.process_command(user_input)
                if tool_result is not None:
                    print(colored("\nTool result:", "yellow"))
                    print(tool_result)
                    continue

                prompt = user_input
                if self.should_inspect_project(user_input):
                    project_context = build_project_context()
                    project_prompt = (
                        "Sizga loyiha haqida ma'lumot beruvchi kontekst beriladi. "
                        "Ushbu kontekstni o'qib, savolga javob bering. "
                        "Agar kerak bo'lsa, muhim fayllar va ularning vazifasini ko'rsating.\n\n"
                        f"Project context:\n{project_context}\n\nQuestion: {user_input}"
                    )
                    rag_prompt = self.rag_store.build_prompt(user_input)
                    prompt = (
                        "Sizga loyiha va RAG konteksti berildi. "
                        "Ikkalasidan tegishli ma'lumotlarni birlashtirib javob bering.\n\n"
                        f"{rag_prompt}\n\n{project_prompt}"
                    )
                else:
                    prompt = self.rag_store.build_prompt(user_input)

                response = self.run_inference(prompt)
                self.conversation.append({"role": "user", "content": user_input})
                assistant_text = "".join(
                    block.text for block in response.content if getattr(block, "type", None) == "text"
                )
                self.conversation.append({"role": "assistant", "content": assistant_text})
                self.display_response(response)
                print()

            except FileNotFoundError as error:
                print(colored(f"File error: {error}", "red"))
            except anthropic.APIConnectionError as error:
                print(colored(f"Connection error: {error}", "red"))
            except anthropic.APIStatusError as error:
                print(colored(f"API Error ({error.status_code}): {error}", "red"))
            except KeyboardInterrupt:
                print(colored("\n\nMuslim Agent stopped.", "yellow"))
                break
            except Exception as error:
                print(colored(f"Unexpected error: {error}", "red"))
