import sqlite3
from pathlib import Path
from models.aluno import Aluno
from models.plano import Plano
from models.pagamento import Pagamento
from models.treino import Treino
from models.agendamento import Agendamento

DB_PATH = Path(__file__).with_name("academia.db")

def conectar():
    conexao = sqlite3.connect(DB_PATH)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


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
        matricula TEXT NOT NULL,
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
        cref TEXT NOT NULL,
        especialidade TEXT
    )
    """)

    # Tabela Execícios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        grupo_muscular TEXT NOT NULL,
        series INTEGER NOT NULL,
        repeticoes INTEGER NOT NULL
    )
    """)

    # Tabela Treinos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treinos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        aluno_id INTEGER NOT NULL,
        instrutor_id INTEGER NOT NULL,

        FOREIGN KEY (aluno_id) REFERENCES alunos(id),
        FOREIGN KEY (instrutor_id) REFERENCES instrutores(id)
    )
    """)

    # Tabela Treino x Exercícios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treino_exercicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        treino_id INTEGER NOT NULL,
        exercicio_id INTEGER NOT NULL,
        UNIQUE (treino_id, exercicio_id),
        FOREIGN KEY (treino_id) REFERENCES treinos(id),
        FOREIGN KEY (exercicio_id) REFERENCES exercicios(id)
    )
    """)

    # Tabela planos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS planos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        valor REAL NOT NULL,
        duracao INTEGER NOT NULL
    )
    """)

    # Tabela Pagamentos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        plano_id INTEGER NOT NULL,
        valor REAL NOT NULL,
        data TEXT NOT NULL,
        status TEXT NOT NULL,

        FOREIGN KEY (aluno_id) REFERENCES alunos(id),
        FOREIGN KEY (plano_id) REFERENCES planos(id)
    )
    """)

    # tabela Documentos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        arquivo TEXT NOT NULL,

        FOREIGN KEY (aluno_id) REFERENCES alunos(id)
    )
    """)

    # Tabela Avalição Física
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS avaliacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        instrutor_id INTEGER NOT NULL,
        peso REAL NOT NULL,
        altura REAL NOT NULL,
        imc REAL,
        percentual_gordura REAL,
        observacoes TEXT,

        FOREIGN KEY (aluno_id) REFERENCES alunos(id),
        FOREIGN KEY (instrutor_id) REFERENCES instrutores(id)
    )
    """)

    # Tabela Horários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS horarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        disponivel INTEGER NOT NULL
    )
    """)

    # Tabela Agendamentos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        instrutor_id INTEGER NOT NULL,
        horario_id INTEGER NOT NULL,
        status TEXT NOT NULL,

        FOREIGN KEY (aluno_id) REFERENCES alunos(id),
        FOREIGN KEY (instrutor_id) REFERENCES instrutores(id),
        FOREIGN KEY (horario_id) REFERENCES horarios(id)
    )
    """)

    conexao.commit()
    conexao.close()


# ==========================
# Todos os CRUDs
# ==========================

# Alunos

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


def buscar_aluno_por_matricula(matricula):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM alunos WHERE matricula=?",
        (matricula,)
    )

    resultado = cursor.fetchone()

    conexao.close()

    if resultado is None:
        return None

    return Aluno(
        resultado[0],
        resultado[1],
        resultado[2],
        resultado[3],
        resultado[4],
        resultado[5],
        resultado[6]
    )


def excluir_aluno(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM alunos WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# INSTRUTORES

def inserir_instrutor(nome, email, telefone, cref, especialidade):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO instrutores
    (nome,email,telefone,cref,especialidade)
    VALUES (?,?,?,?,?)
    """, (nome, email, telefone, cref, especialidade))

    conexao.commit()
    conexao.close()


def listar_instrutores():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM instrutores")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_instrutor(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM instrutores WHERE id=?",
        (id,)
    )

    instrutor = cursor.fetchone()

    conexao.close()

    return instrutor


def atualizar_instrutor(
    id,
    nome,
    email,
    telefone,
    cref,
    especialidade
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE instrutores
    SET nome=?,
        email=?,
        telefone=?,
        cref=?,
        especialidade=?
    WHERE id=?
    """,
    (
        nome,
        email,
        telefone,
        cref,
        especialidade,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_instrutor(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM instrutores WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# Exercícios

def inserir_exercicios(nome, grupo_muscular, series, repeticoes):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO exercicios
    (nome,grupo_muscular,series,repeticoes)
    VALUES (?,?,?,?)
    """, (nome, grupo_muscular, series, repeticoes))

    conexao.commit()
    conexao.close()


def listar_exercicios():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM exercicios")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_exercicios(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM exercicios WHERE id=?",
        (id,)
    )

    exercicios = cursor.fetchone()

    conexao.close()

    return exercicios


def atualizar_exercicios(
    id,
    nome,
    grupo_muscular,
    series,
    repeticoes
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE exercicios
    SET nome=?,
        grupo_muscular=?,
        series=?,
        repeticoes=?
    WHERE id=?
    """,
    (
        nome,
        grupo_muscular,
        series,
        repeticoes,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_exercicios(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM exercicios WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# treinos

def inserir_treinos(nome, descricao, aluno_id, instrutor_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO treinos
    (nome,descricao,aluno_id,instrutor_id)
    VALUES (?,?,?,?)
    """, (nome, descricao, aluno_id, instrutor_id))

    conexao.commit()
    conexao.close()


def listar_treinos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM treinos")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_treinos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM treinos WHERE id=?",
        (id,)
    )

    treino = cursor.fetchone()

    conexao.close()

    return treino


def atualizar_treinos(
    id,
    nome,
    descricao,
    aluno_id,
    instrutor_id
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE treinos
    SET nome=?,
        descricao=?,
        aluno_id=?,
        instrutor_id=?
    WHERE id=?
    """,
    (
        nome,
        descricao,
        aluno_id,
        instrutor_id,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_treinos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM treinos WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# Avaliaçoes

def inserir_avaliacoes(aluno_id, instrutor_id, peso, altura, imc, percentual_gordura, observacoes):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO avaliacoes
    (aluno_id,instrutor_id,peso,altura,imc,percentual_gordura,observacoes)
    VALUES (?,?,?,?,?,?,?)
    """, (aluno_id, instrutor_id, peso, altura, imc, percentual_gordura, observacoes))

    conexao.commit()
    conexao.close()


def listar_avaliacoes():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM avaliacoes")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_avaliacoes(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM avaliacoes WHERE id=?",
        (id,)
    )

    avaliacao = cursor.fetchone()

    conexao.close()

    return avaliacao


def atualizar_avaliacoes(
    id,
    aluno_id,
    instrutor_id,
    peso,
    altura,
    imc,
    percentual_gordura,
    observacoes
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE avaliacoes
    SET aluno_id=?,
        instrutor_id=?,
        peso=?,
        altura=?,
        imc=?,
        percentual_gordura=?,
        observacoes=?
    WHERE id=?
    """,
    (
        aluno_id,
        instrutor_id,
        peso,
        altura,
        imc,
        percentual_gordura,
        observacoes,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_avaliacoes(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM avaliacoes WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# Plano

def inserir_planos(nome, valor, duracao):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO planos
    (nome,valor,duracao)
    VALUES (?,?,?)
    """, (nome, valor, duracao))

    conexao.commit()
    conexao.close()


def listar_planos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM planos")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_planos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM planos WHERE id=?",
        (id,)
    )

    planos = cursor.fetchone()

    conexao.close()

    return planos


def atualizar_planos(
    id,
    nome,
    valor,
    duracao
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE planos
    SET nome=?,
        valor=?,
        duracao=?
    WHERE id=?
    """,
    (
        nome,
        valor,
        duracao,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_planos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM planos WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# Pagamentos

def inserir_pagamentos(aluno_id, plano_id, valor, data, status):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO pagamentos
    (aluno_id,plano_id,valor,data,status)
    VALUES (?,?,?,?,?)
    """, (aluno_id, plano_id, valor, data, status))

    conexao.commit()
    conexao.close()


def listar_pagamentos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pagamentos")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_pagamentos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM pagamentos WHERE id=?",
        (id,)
    )

    pagamentos = cursor.fetchone()

    conexao.close()

    return pagamentos


def atualizar_pagamentos(
    id,
    aluno_id,
    plano_id,
    valor,
    data,
    status
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE pagamentos
    SET aluno_id=?,
        plano_id=?,
        valor=?,
        data=?,
        status=?
    WHERE id=?
    """,
    (
        aluno_id,
        plano_id,
        valor,
        data,
        status,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_pagamentos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM pagamentos WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# Documentos

def inserir_documentos(aluno_id, tipo, arquivo):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO documentos
    (aluno_id, tipo, arquivo)
    VALUES (?,?,?)
    """, (aluno_id, tipo, arquivo))

    conexao.commit()
    conexao.close()


def listar_documentos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM documentos")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_documentos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM documentos WHERE id=?",
        (id,)
    )

    documentos = cursor.fetchone()

    conexao.close()

    return documentos


def atualizar_documentos(
    id,
    aluno_id,
    tipo,
    arquivo
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE documentos
    SET aluno_id=?,
        tipo=?,
        arquivo=?
    WHERE id=?
    """,
    (
        aluno_id,
        tipo,
        arquivo,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_documentos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM documentos WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# Horários

def inserir_horarios(data, hora, disponivel):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO horarios
    (data,hora,disponivel)
    VALUES (?,?,?)
    """, (data, hora, disponivel))

    conexao.commit()
    conexao.close()


def listar_horarios():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM horarios")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_horarios(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM horarios WHERE id=?",
        (id,)
    )

    horarios = cursor.fetchone()

    conexao.close()

    return horarios


def atualizar_horarios(
    id,
    data,
    hora,
    disponivel
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE horarios
    SET data=?,
        hora=?,
        disponivel=?
    WHERE id=?
    """,
    (
        data,
        hora,
        disponivel,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_horarios(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM horarios WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# Agendamentos

def inserir_agendamentos(aluno_id, instrutor_id, horario_id, status):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO agendamentos
    (aluno_id,instrutor_id,horario_id,status)
    VALUES (?,?,?,?)
    """, (aluno_id, instrutor_id, horario_id, status))

    conexao.commit()
    conexao.close()


def listar_agendamentos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM agendamentos")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_agendamentos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM agendamentos WHERE id=?",
        (id,)
    )

    agendamentos = cursor.fetchone()

    conexao.close()

    return agendamentos


def atualizar_agendamentos(
    id,
    aluno_id,
    instrutor_id,
    horario_id,
    status
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE agendamentos
    SET aluno_id=?,
        instrutor_id=?,
        horario_id=?,
        status=?
    WHERE id=?
    """,
    (
        aluno_id,
        instrutor_id,
        horario_id,
        status,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_agendamentos(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM agendamentos WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


# Treino x Exercícios

def inserir_treino_exercicios(treino_id, exercicio_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO treino_exercicios
    (treino_id,exercicio_id)
    VALUES (?,?)
    """, (treino_id, exercicio_id))

    conexao.commit()
    conexao.close()


def listar_treino_exercicios():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM treino_exercicios")

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_treino_exercicios(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM treino_exercicios WHERE id=?",
        (id,)
    )

    treino_exercicios = cursor.fetchone()

    conexao.close()

    return treino_exercicios


def atualizar_treino_exercicios(
    id,
    treino_id,
    exercicio_id
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE treino_exercicios
    SET treino_id=?,
        exercicio_id=?
    WHERE id=?
    """,
    (
        treino_id,
        exercicio_id,
        id
    ))

    conexao.commit()
    conexao.close()


def excluir_treino_exercicios(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM treino_exercicios WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()


def buscar_plano_do_aluno(aluno_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM planos
        ORDER BY id
        LIMIT 1
    """)

    plano = cursor.fetchone()

    conexao.close()

    return plano


def buscar_pagamentos_aluno(aluno_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM pagamentos

        WHERE aluno_id = ?

        ORDER BY id DESC

    """,(aluno_id,))

    pagamentos = []

    for p in cursor.fetchall():

        pagamentos.append(

            Pagamento(
                p[0],
                p[1],
                p[2],
                p[3],
                p[4],
                p[5]
            )

        )

    conn.close()

    return pagamentos


def buscar_treinos_aluno(aluno_id):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM treinos

        WHERE aluno_id = ?

    """,(aluno_id,))

    lista=[]

    for t in cursor.fetchall():

        lista.append(

            Treino(
                t[0],
                t[1],
                t[2],
                t[3],
                t[4]
            )

        )

    conn.close()

    return lista


def buscar_agendamentos_aluno(aluno_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""

        SELECT

            h.data,
            h.hora,
            i.nome,
            a.status

        FROM agendamentos a

        INNER JOIN horarios h
            ON a.horario_id = h.id

        INNER JOIN instrutores i
            ON a.instrutor_id = i.id

        WHERE a.aluno_id=?

        ORDER BY h.data,h.hora

    """,(aluno_id,))

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_aluno_por_matricula(matricula):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM alunos WHERE matricula=?",
        (matricula,)
    )

    resultado = cursor.fetchone()

    conexao.close()

    if resultado:

        return Aluno(
            resultado[0],
            resultado[1],
            resultado[2],
            resultado[3],
            resultado[4],
            resultado[5],
            resultado[6]
        )

    return None


def buscar_treinos_aluno(aluno_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM treinos
        WHERE aluno_id=?
    """, (aluno_id,))

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_pagamentos_aluno(aluno_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM pagamentos
        WHERE aluno_id=?
    """, (aluno_id,))

    dados = cursor.fetchall()

    conexao.close()

    return dados


def buscar_plano_do_aluno(aluno_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM planos
        LIMIT 1
    """)

    plano = cursor.fetchone()

    conexao.close()

    return plano


def buscar_agendamentos_aluno(aluno_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""

        SELECT
            h.data,
            h.hora,
            i.nome,
            a.status

        FROM agendamentos a

        JOIN horarios h
            ON a.horario_id = h.id

        JOIN instrutores i
            ON a.instrutor_id = i.id

        WHERE a.aluno_id=?

        ORDER BY h.data, h.hora

    """, (aluno_id,))

    dados = cursor.fetchall()

    conexao.close()

    return dados