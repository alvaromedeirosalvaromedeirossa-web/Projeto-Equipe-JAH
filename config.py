import os

# Pasta raiz do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Banco de dados SQLite
DATABASE = os.path.join(BASE_DIR, "academia.db")

# Chave secreta do Flask
SECRET_KEY = "academia_ifpb_2026"

# Pasta para uploads de documentos
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

# Extensões permitidas para upload
ALLOWED_EXTENSIONS = {
    "pdf",
    "png",
    "jpg",
    "jpeg",
    "doc",
    "docx"
}