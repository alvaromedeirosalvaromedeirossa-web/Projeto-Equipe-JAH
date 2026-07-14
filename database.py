import sqlite3
from pathlib import Path
from models.aluno import Aluno

DB_PATH = Path(__file__).with_name("academia.db")


def conectar():
    """
    Cria uma conexão com o banco de dados SQLite.
    """

    conexao = sqlite3.connect(DB_PATH)

    # Permite acessar as colunas pelo nome, ex.: aluno["nome"]
    conexao.row_factory = sqlite3.Row

    # Ativa as chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")

    return conexao


def executar(sql, parametros=(), fetch=False, fetchone=False):
    """
    Executa um comando SQL e gerencia automaticamente
    a conexão com o banco de dados.

    Parâmetros:
        sql (str): Comando SQL.
        parametros (tuple): Parâmetros do comando.
        fetch (bool): Retorna todos os registros.
        fetchone (bool): Retorna apenas um registro.
    """

    conexao = conectar()

    try:
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)

        conexao.commit()

        if fetchone:
            return cursor.fetchone()

        if fetch:
            return cursor.fetchall()

        return True

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
        return None

    finally:
        conexao.close()


def criar_tabelas():

    conexao = conectar()
    cursor = conexao.cursor()

    # ===========================
    # TABELA ALUNOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        telefone TEXT,
        matricula TEXT NOT NULL UNIQUE,
        peso REAL,
        altura REAL
    )
    """)

    # ===========================
    # TABELA INSTRUTORES
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS instrutores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        telefone TEXT,
        cref TEXT NOT NULL UNIQUE,
        especialidade TEXT
    )
    """)

    # ===========================
    # TABELA EXERCÍCIOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        grupo_muscular TEXT NOT NULL,
        series INTEGER NOT NULL,
        repeticoes INTEGER NOT NULL
    )
    """)

    # ===========================
    # TABELA TREINOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treinos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        aluno_id INTEGER NOT NULL,
        instrutor_id INTEGER NOT NULL,

        FOREIGN KEY (aluno_id)
            REFERENCES alunos(id)
            ON DELETE CASCADE,

        FOREIGN KEY (instrutor_id)
            REFERENCES instrutores(id)
            ON DELETE CASCADE
    )
    """)

    # ===========================
    # TREINO x EXERCÍCIOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treino_exercicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        treino_id INTEGER NOT NULL,
        exercicio_id INTEGER NOT NULL,

        UNIQUE (treino_id, exercicio_id),

        FOREIGN KEY (treino_id)
            REFERENCES treinos(id)
            ON DELETE CASCADE,

        FOREIGN KEY (exercicio_id)
            REFERENCES exercicios(id)
            ON DELETE CASCADE
    )
    """)

    # ===========================
    # PLANOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS planos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        valor REAL NOT NULL,
        duracao INTEGER NOT NULL
    )
    """)

    # ===========================
    # PAGAMENTOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        plano_id INTEGER NOT NULL,
        valor REAL NOT NULL,
        data TEXT NOT NULL,
        status TEXT NOT NULL,

        FOREIGN KEY (aluno_id)
            REFERENCES alunos(id)
            ON DELETE CASCADE,

        FOREIGN KEY (plano_id)
            REFERENCES planos(id)
            ON DELETE CASCADE
    )
    """)

    # ===========================
    # DOCUMENTOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        arquivo TEXT NOT NULL,

        FOREIGN KEY (aluno_id)
            REFERENCES alunos(id)
            ON DELETE CASCADE
    )
    """)

    # ===========================
    # AVALIAÇÕES
    # ===========================
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

        FOREIGN KEY (aluno_id)
            REFERENCES alunos(id)
            ON DELETE CASCADE,

        FOREIGN KEY (instrutor_id)
            REFERENCES instrutores(id)
            ON DELETE CASCADE
    )
    """)

    # ===========================
    # HORÁRIOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS horarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        disponivel INTEGER NOT NULL
    )
    """)

    # ===========================
    # AGENDAMENTOS
    # ===========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        instrutor_id INTEGER NOT NULL,
        horario_id INTEGER NOT NULL,
        status TEXT NOT NULL,

        FOREIGN KEY (aluno_id)
            REFERENCES alunos(id)
            ON DELETE CASCADE,

        FOREIGN KEY (instrutor_id)
            REFERENCES instrutores(id)
            ON DELETE CASCADE,

        FOREIGN KEY (horario_id)
            REFERENCES horarios(id)
            ON DELETE CASCADE
    )
    """)

    # ===========================
    # ÍNDICES
    # ===========================

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_aluno_matricula
    ON alunos(matricula)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_aluno_email
    ON alunos(email)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_instrutor_cref
    ON instrutores(cref)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_treino_aluno
    ON treinos(aluno_id)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_pagamento_aluno
    ON pagamentos(aluno_id)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_agendamento_aluno
    ON agendamentos(aluno_id)
    """)

    conexao.commit()
    conexao.close()


# ==========================
# Todos os CRUDs
# ==========================

# Alunos

def inserir_aluno(nome, email, telefone, matricula, peso, altura):

    sql = """
        INSERT INTO alunos
        (nome, email, telefone, matricula, peso, altura)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    return executar(
        sql,
        (nome, email, telefone, matricula, peso, altura)
    )


def listar_alunos():

    sql = """
        SELECT *
        FROM alunos
        ORDER BY nome
    """

    return executar(sql, fetch=True)


def buscar_aluno(id):

    sql = """
        SELECT *
        FROM alunos
        WHERE id = ?
    """

    return executar(sql, (id,), fetchone=True)


def atualizar_aluno(id, nome, email, telefone, matricula, peso, altura):

    sql = """
        UPDATE alunos
        SET
            nome=?,
            email=?,
            telefone=?,
            matricula=?,
            peso=?,
            altura=?
        WHERE id=?
    """

    return executar(
        sql,
        (
            nome,
            email,
            telefone,
            matricula,
            peso,
            altura,
            id
        )
    )


def excluir_aluno(id):

    sql = """
        DELETE FROM alunos
        WHERE id=?
    """

    return executar(sql, (id,))


# INSTRUTORES

def inserir_instrutor(nome, email, telefone, cref, especialidade):

    sql = """
        INSERT INTO instrutores
        (nome, email, telefone, cref, especialidade)
        VALUES (?, ?, ?, ?, ?)
    """

    return executar(
        sql,
        (
            nome,
            email,
            telefone,
            cref,
            especialidade
        )
    )


def listar_instrutores():

    sql = """
        SELECT *
        FROM instrutores
        ORDER BY nome
    """

    return executar(sql, fetch=True)


def buscar_instrutor(id):

    sql = """
        SELECT *
        FROM instrutores
        WHERE id=?
    """

    return executar(sql, (id,), fetchone=True)


def atualizar_instrutor(id,
                        nome,
                        email,
                        telefone,
                        cref,
                        especialidade):

    sql = """

        UPDATE instrutores

        SET

            nome=?,
            email=?,
            telefone=?,
            cref=?,
            especialidade=?

        WHERE id=?

    """

    return executar(
        sql,
        (
            nome,
            email,
            telefone,
            cref,
            especialidade,
            id
        )
    )


def excluir_instrutor(id):

    sql = """
        DELETE
        FROM instrutores
        WHERE id=?
    """

    return executar(sql, (id,))


# Exercícios

def inserir_exercicio(nome,
                      grupo_muscular,
                      series,
                      repeticoes):

    sql = """

        INSERT INTO exercicios

        (nome, grupo_muscular, series, repeticoes)

        VALUES (?, ?, ?, ?)

    """

    return executar(
        sql,
        (
            nome,
            grupo_muscular,
            series,
            repeticoes
        )
    )


def listar_exercicios():

    sql = """

        SELECT *

        FROM exercicios

        ORDER BY nome

    """

    return executar(sql, fetch=True)


def buscar_exercicio(id):

    sql = """

        SELECT *

        FROM exercicios

        WHERE id=?

    """

    return executar(sql, (id,), fetchone=True)


def atualizar_exercicio(id,
                        nome,
                        grupo_muscular,
                        series,
                        repeticoes):

    sql = """

        UPDATE exercicios

        SET

            nome=?,
            grupo_muscular=?,
            series=?,
            repeticoes=?

        WHERE id=?

    """

    return executar(
        sql,
        (
            nome,
            grupo_muscular,
            series,
            repeticoes,
            id
        )
    )


def excluir_exercicio(id):

    sql = """

        DELETE

        FROM exercicios

        WHERE id=?

    """

    return executar(sql, (id,))


# treinos

def inserir_treino(nome,
                   descricao,
                   aluno_id,
                   instrutor_id):

    sql = """

        INSERT INTO treinos

        (nome, descricao, aluno_id, instrutor_id)

        VALUES (?, ?, ?, ?)

    """

    return executar(
        sql,
        (
            nome,
            descricao,
            aluno_id,
            instrutor_id
        )
    )


def listar_treinos():

    sql = """

        SELECT *

        FROM treinos

        ORDER BY nome

    """

    return executar(sql, fetch=True)


def buscar_treino(id):

    sql = """

        SELECT *

        FROM treinos

        WHERE id=?

    """

    return executar(sql, (id,), fetchone=True)


def atualizar_treino(id,
                     nome,
                     descricao,
                     aluno_id,
                     instrutor_id):

    sql = """

        UPDATE treinos

        SET

            nome=?,
            descricao=?,
            aluno_id=?,
            instrutor_id=?

        WHERE id=?

    """

    return executar(
        sql,
        (
            nome,
            descricao,
            aluno_id,
            instrutor_id,
            id
        )
    )


def excluir_treino(id):

    sql = """

        DELETE

        FROM treinos

        WHERE id=?

    """

    return executar(sql, (id,))


# Avaliaçoes

def inserir_avaliacoes(
    aluno_id,
    instrutor_id,
    peso,
    altura,
    imc,
    percentual_gordura,
    observacoes
):

    sql = """

        INSERT INTO avaliacoes

        (
            aluno_id,
            instrutor_id,
            peso,
            altura,
            imc,
            percentual_gordura,
            observacoes
        )

        VALUES (?,?,?,?,?,?,?)

    """

    return executar(
        sql,
        (
            aluno_id,
            instrutor_id,
            peso,
            altura,
            imc,
            percentual_gordura,
            observacoes
        )
    )


def listar_avaliacoes():

    return executar(

        """

        SELECT *

        FROM avaliacoes

        ORDER BY id DESC

        """,

        fetch=True

    )


def buscar_avaliacoes(id):

    return executar(

        """

        SELECT *

        FROM avaliacoes

        WHERE id=?

        """,

        (id,),

        fetchone=True

    )


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

    sql = """

        UPDATE avaliacoes

        SET

            aluno_id=?,

            instrutor_id=?,

            peso=?,

            altura=?,

            imc=?,

            percentual_gordura=?,

            observacoes=?

        WHERE id=?

    """

    return executar(

        sql,

        (

            aluno_id,

            instrutor_id,

            peso,

            altura,

            imc,

            percentual_gordura,

            observacoes,

            id

        )

    )


def excluir_avaliacoes(id):

    return executar(

        """

        DELETE

        FROM avaliacoes

        WHERE id=?

        """,

        (id,)

    )


# Plano

def inserir_plano(nome, valor, duracao):

    sql = """

        INSERT INTO planos

        (nome, valor, duracao)

        VALUES (?, ?, ?)

    """

    return executar(
        sql,
        (
            nome,
            valor,
            duracao
        )
    )


def listar_planos():

    sql = """

        SELECT *

        FROM planos

        ORDER BY nome

    """

    return executar(sql, fetch=True)


def buscar_plano(id):

    sql = """

        SELECT *

        FROM planos

        WHERE id=?

    """

    return executar(sql, (id,), fetchone=True)


def atualizar_plano(id,
                    nome,
                    valor,
                    duracao):

    sql = """

        UPDATE planos

        SET

            nome=?,
            valor=?,
            duracao=?

        WHERE id=?

    """

    return executar(
        sql,
        (
            nome,
            valor,
            duracao,
            id
        )
    )


def excluir_plano(id):

    sql = """

        DELETE

        FROM planos

        WHERE id=?

    """

    return executar(sql, (id,))


# Pagamentos

def inserir_pagamento(aluno_id,
                      plano_id,
                      valor,
                      data,
                      status):

    sql = """

        INSERT INTO pagamentos

        (aluno_id, plano_id, valor, data, status)

        VALUES (?, ?, ?, ?, ?)

    """

    return executar(
        sql,
        (
            aluno_id,
            plano_id,
            valor,
            data,
            status
        )
    )


def listar_pagamentos():

    sql = """

        SELECT *

        FROM pagamentos

        ORDER BY id DESC

    """

    return executar(sql, fetch=True)


def buscar_pagamento(id):

    sql = """

        SELECT *

        FROM pagamentos

        WHERE id=?

    """

    return executar(sql, (id,), fetchone=True)


def atualizar_pagamento(id,
                        aluno_id,
                        plano_id,
                        valor,
                        data,
                        status):

    sql = """

        UPDATE pagamentos

        SET

            aluno_id=?,
            plano_id=?,
            valor=?,
            data=?,
            status=?

        WHERE id=?

    """

    return executar(
        sql,
        (
            aluno_id,
            plano_id,
            valor,
            data,
            status,
            id
        )
    )


def excluir_pagamento(id):

    sql = """

        DELETE FROM pagamentos

        WHERE id=?

    """

    return executar(sql, (id,))


# Documentos

def inserir_documentos(aluno_id, tipo, arquivo):

    sql = """

        INSERT INTO documentos

        (aluno_id, tipo, arquivo)

        VALUES (?, ?, ?)

    """

    return executar(
        sql,
        (
            aluno_id,
            tipo,
            arquivo
        )
    )


def listar_documentos():

    return executar(

        """

        SELECT *

        FROM documentos

        ORDER BY id DESC

        """,

        fetch=True

    )


def buscar_documentos(id):

    return executar(

        """

        SELECT *

        FROM documentos

        WHERE id=?

        """,

        (id,),

        fetchone=True

    )


def atualizar_documentos(
    id,
    aluno_id,
    tipo,
    arquivo
):

    sql = """

        UPDATE documentos

        SET

            aluno_id=?,

            tipo=?,

            arquivo=?

        WHERE id=?

    """

    return executar(

        sql,

        (

            aluno_id,

            tipo,

            arquivo,

            id

        )

    )


def excluir_documentos(id):

    return executar(

        """

        DELETE

        FROM documentos

        WHERE id=?

        """,

        (id,)

    )


# Horários

def inserir_horarios(data, hora, disponivel):

    sql = """

        INSERT INTO horarios

        (data, hora, disponivel)

        VALUES (?, ?, ?)

    """

    return executar(
        sql,
        (
            data,
            hora,
            disponivel
        )
    )


def listar_horarios():

    return executar(

        """

        SELECT *

        FROM horarios

        ORDER BY data, hora

        """,

        fetch=True

    )


def buscar_horarios(id):

    return executar(

        """

        SELECT *

        FROM horarios

        WHERE id=?

        """,

        (id,),

        fetchone=True

    )


def atualizar_horarios(
    id,
    data,
    hora,
    disponivel
):

    sql = """

        UPDATE horarios

        SET

            data=?,

            hora=?,

            disponivel=?

        WHERE id=?

    """

    return executar(

        sql,

        (

            data,

            hora,

            disponivel,

            id

        )

    )


def excluir_horarios(id):

    return executar(

        """

        DELETE

        FROM horarios

        WHERE id=?

        """,

        (id,)

    )


# Agendamentos

def inserir_agendamentos(aluno_id, instrutor_id, horario_id, status):

    sql = """

        INSERT INTO agendamentos

        (aluno_id, instrutor_id, horario_id, status)

        VALUES (?, ?, ?, ?)

    """

    return executar(
        sql,
        (
            aluno_id,
            instrutor_id,
            horario_id,
            status
        )
    )


def listar_agendamentos():

    sql = """

        SELECT

            a.id,
            a.aluno_id,
            a.instrutor_id,
            h.data,
            h.hora,
            a.status

        FROM agendamentos a

        JOIN horarios h
            ON a.horario_id = h.id

        ORDER BY h.data, h.hora

    """

    return executar(sql, fetch=True)

def buscar_agendamentos(id):

    return executar(

        """

        SELECT *

        FROM agendamentos

        WHERE id=?

        """,

        (id,),

        fetchone=True

    )


def atualizar_agendamentos(
    id,
    aluno_id,
    instrutor_id,
    horario_id,
    status
):

    sql = """

        UPDATE agendamentos

        SET

            aluno_id=?,

            instrutor_id=?,

            horario_id=?,

            status=?

        WHERE id=?

    """

    return executar(

        sql,

        (

            aluno_id,

            instrutor_id,

            horario_id,

            status,

            id

        )

    )


def excluir_agendamentos(id):

    return executar(

        """

        DELETE

        FROM agendamentos

        WHERE id=?

        """,

        (id,)

    )

# ==========================
# HORÁRIOS DISPONÍVEIS
# ==========================

def buscar_horarios_disponiveis():

    sql = """

        SELECT *

        FROM horarios

        WHERE disponivel = 1

        ORDER BY data, hora

    """

    return executar(sql, fetch=True)


# Treino x Exercícios

def inserir_treino_exercicios(treino_id, exercicio_id):

    sql = """

        INSERT INTO treino_exercicios

        (treino_id, exercicio_id)

        VALUES (?, ?)

    """

    return executar(
        sql,
        (
            treino_id,
            exercicio_id
        )
    )


def listar_treino_exercicios():

    return executar(

        """

        SELECT *

        FROM treino_exercicios

        ORDER BY id DESC

        """,

        fetch=True

    )


def buscar_treino_exercicios(id):

    return executar(

        """

        SELECT *

        FROM treino_exercicios

        WHERE id=?

        """,

        (id,),

        fetchone=True

    )


def atualizar_treino_exercicios(
    id,
    treino_id,
    exercicio_id
):

    sql = """

        UPDATE treino_exercicios

        SET

            treino_id=?,

            exercicio_id=?

        WHERE id=?

    """

    return executar(

        sql,

        (

            treino_id,

            exercicio_id,

            id

        )

    )


def excluir_treino_exercicios(id):

    return executar(

        """

        DELETE

        FROM treino_exercicios

        WHERE id=?

        """,

        (id,)

    )


def buscar_treinos_aluno(aluno_id):

    return executar(

        """

        SELECT *

        FROM treinos

        WHERE aluno_id=?

        ORDER BY nome

        """,

        (aluno_id,),

        fetch=True

    )


def buscar_pagamentos_aluno(aluno_id):

    return executar(

        """

        SELECT *

        FROM pagamentos

        WHERE aluno_id=?

        ORDER BY data DESC

        """,

        (aluno_id,),

        fetch=True

    )


def buscar_plano_do_aluno(aluno_id):

    return executar(

        """

        SELECT *

        FROM planos

        ORDER BY id

        LIMIT 1

        """,

        fetchone=True

    )


def buscar_agendamentos_aluno(aluno_id):

    return executar(

        """

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

        """,

        (aluno_id,),

        fetch=True

    )


# ==========================================================
# FUNÇÕES DE COMPATIBILIDADE
# ==========================================================

# ---------- AVALIAÇÕES ----------

def inserir_avaliacao(aluno_id, instrutor_id, peso, altura, imc,
                      percentual_gordura, observacoes):
    return inserir_avaliacoes(
        aluno_id,
        instrutor_id,
        peso,
        altura,
        imc,
        percentual_gordura,
        observacoes
    )


def buscar_avaliacao(id):
    return buscar_avaliacoes(id)


def atualizar_avaliacao(id, aluno_id, instrutor_id, peso, altura,
                        imc, percentual_gordura, observacoes):
    return atualizar_avaliacoes(
        id,
        aluno_id,
        instrutor_id,
        peso,
        altura,
        imc,
        percentual_gordura,
        observacoes
    )


def excluir_avaliacao(id):
    return excluir_avaliacoes(id)


# ---------- DOCUMENTOS ----------

def inserir_documento(aluno_id, tipo, arquivo):
    return inserir_documentos(
        aluno_id,
        tipo,
        arquivo
    )


def buscar_documento(id):
    return buscar_documentos(id)


def atualizar_documento(id, aluno_id, tipo, arquivo):
    return atualizar_documentos(
        id,
        aluno_id,
        tipo,
        arquivo
    )


def excluir_documento(id):
    return excluir_documentos(id)


# ---------- HORÁRIOS ----------

def inserir_horario(data, hora, disponivel):
    return inserir_horarios(
        data,
        hora,
        disponivel
    )


def buscar_horario(id):
    return buscar_horarios(id)


def atualizar_horario(id, data, hora, disponivel):
    return atualizar_horarios(
        id,
        data,
        hora,
        disponivel
    )


def excluir_horario(id):
    return excluir_horarios(id)


# ---------- AGENDAMENTOS ----------

def inserir_agendamento(aluno_id, instrutor_id,
                        horario_id, status):
    return inserir_agendamentos(
        aluno_id,
        instrutor_id,
        horario_id,
        status
    )


def buscar_agendamento(id):
    return buscar_agendamentos(id)


def atualizar_agendamento(id, aluno_id,
                          instrutor_id,
                          horario_id,
                          status):
    return atualizar_agendamentos(
        id,
        aluno_id,
        instrutor_id,
        horario_id,
        status
    )


def excluir_agendamento(id):
    return excluir_agendamentos(id)

