import sqlite3

def conectar():
    return sqlite3.connect("academia.db")


def criar_tabelas():

    conexao = conectar()
    cursor = conexao.cursor()

    # Tabela Alunos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        matricula TEXT,
        peso REAL,
        altura REAL
    )
    """)

    # Tabela Instrutores
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS instrutores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        cref TEXT
    )
    """)

    conexao.commit()
    conexao.close()


# ==========================
# ALUNOS
# ==========================

def inserir_aluno(nome, email, telefone, matricula, peso, altura):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO alunos
    (nome,email,telefone,matricula,peso,altura)
    VALUES (?,?,?,?,?,?)
    """, (nome, email, telefone, matricula, peso, altura))

    conexao.commit()
    conexao.close()


def listar_alunos_db():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_aluno(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM alunos WHERE id=?",
        (id,)
    )

    aluno = cursor.fetchone()

    conexao.close()

    return aluno


def atualizar_aluno_db(
    id,
    nome,
    email,
    telefone,
    matricula,
    peso,
    altura
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE alunos
    SET nome=?,
        email=?,
        telefone=?,
        matricula=?,
        peso=?,
        altura=?
    WHERE id=?
    """,
    (
        nome,
        email,
        telefone,
        matricula,
        peso,
        altura,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_aluno(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM alunos WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# ==========================
# INSTRUTORES
# ==========================

def inserir_instrutor(nome, email, telefone, cref):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO instrutores
    (nome,email,telefone,cref)
    VALUES (?,?,?,?)
    """, (nome, email, telefone, cref))

    conexao.commit()
    conexao.close()


def listar_instrutores():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM instrutores")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def excluir_instrutor(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM instrutores WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()