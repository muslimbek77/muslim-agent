from pathlib import Path

from config import BASE_DIR


def resolve_path(raw_path):
    """Resolve a user-provided relative or absolute path into a project-safe path."""
    if not raw_path:
        raise ValueError("Fayl yo'li berilmadi.")

    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = (BASE_DIR / path).resolve()
    return path


def read_file(file_path):
    """Read UTF-8 text from a file and return its content."""
    path = resolve_path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Fayl topilmadi: {path}")
    return path.read_text(encoding="utf-8")


def write_file(file_path, content):
    """Write a file, creating parent directories when needed."""
    path = resolve_path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return f"Fayl yozildi: {path}"


def append_file(file_path, content):
    """Append text to the end of a file."""
    path = resolve_path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(content)
    return f"Matn qo'shildi: {path}"


def list_dir(dir_path="."):
    """Return the contents of a directory as a sorted list of names."""
    path = resolve_path(dir_path)
    if not path.exists():
        raise FileNotFoundError(f"Katalog topilmadi: {path}")
    return "\n".join(sorted(p.name for p in path.iterdir()))


def collect_project_files(root=None, max_files=30):
    """Collect project files while ignoring common local/cache folders."""
    root = Path(root).resolve() if root else BASE_DIR
    skip_dirs = {".git", ".venv", "venv", "__pycache__", ".idea", ".mypy_cache", ".pytest_cache"}

    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in skip_dirs for part in path.parts):
            continue
        files.append(path.relative_to(root).as_posix())
        if len(files) >= max_files:
            break
    return files


def build_project_context(root=None):
    """Create a compact project context summary from relevant project files."""
    root = Path(root).resolve() if root else BASE_DIR
    files = collect_project_files(root=root)
    important_names = [
        "README.md",
        "README",
        "main.py",
        "requirements.txt",
        "pyproject.toml",
        "package.json",
        ".env.example",
    ]

    project_context = [
        f"Project root: {root}",
        "Top-level project files:",
        "\n".join(f"- {f}" for f in files),
        "",
        "Important file contents:",
    ]

    for name in important_names:
        for candidate in [root / name, *root.glob(f"**/{name}")]:
            if candidate.exists() and candidate.is_file():
                try:
                    content = candidate.read_text(encoding="utf-8")
                except Exception:
                    continue
                rel = candidate.relative_to(root)
                project_context.append(f"\n--- {rel} ---\n{content[:1200]}")
                break

    main_file = root / "main.py"
    if main_file.exists():
        project_context.append(f"\n--- main.py ---\n{main_file.read_text(encoding='utf-8')[:1500]}")

    return "\n".join(project_context)[:6000]
