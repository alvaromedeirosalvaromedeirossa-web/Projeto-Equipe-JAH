from flask import Flask, render_template, request, redirect, url_for
from database import *

app = Flask(__name__)
app.secret_key = "academia123"

criar_tabelas()

# ===========================
# LOGIN
# ===========================

LOGIN = "admin"
SENHA = "123"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/autenticar", methods=["POST"])
def autenticar():

    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == LOGIN and senha == SENHA:
        return redirect(url_for("painel"))

    return render_template(
        "index.html",
        mensagem="Login ou senha inválidos."
    )


# ===========================
# PAINEL
# ===========================

@app.route("/painel")
def painel():
    return render_template("painel.html")


@app.route("/sair")
def sair():
    return redirect(url_for("home"))


# ===========================
# ALUNOS
# ===========================

@app.route("/alunos")
def listar_alunos():

    alunos = listar_alunos_db()

    return render_template(
        "alunos.html",
        alunos=alunos
    )


@app.route("/cadastrar_aluno", methods=["POST"])
def cadastrar_aluno():

    inserir_aluno(

        request.form.get("nome"),
        request.form.get("email"),
        request.form.get("telefone"),
        request.form.get("matricula"),
        request.form.get("peso"),
        request.form.get("altura")

    )

    return redirect(url_for("listar_alunos"))


@app.route("/editar_aluno/<int:id>")
def editar_aluno(id):

    aluno = buscar_aluno(id)

    return render_template(
        "editar_aluno.html",
        aluno=aluno
    )


@app.route("/atualizar_aluno/<int:id>", methods=["POST"])
def atualizar_aluno(id):

    atualizar_aluno_db(

        id,

        request.form.get("nome"),
        request.form.get("email"),
        request.form.get("telefone"),
        request.form.get("matricula"),
        request.form.get("peso"),
        request.form.get("altura")

    )

    return redirect(url_for("listar_alunos"))


@app.route("/excluir_aluno/<int:id>")
def excluir_aluno_rota(id):

    excluir_aluno(id)

    return redirect(url_for("listar_alunos"))


# ===========================
# INSTRUTORES
# ===========================

@app.route("/instrutores")
def pagina_instrutores():

    instrutores = listar_instrutores()

    return render_template("instrutores.html", instrutores=instrutores)


@app.route("/cadastrar_instrutor", methods=["POST"])
def cadastrar_instrutor():

    inserir_instrutor(

        request.form.get("nome"),
        request.form.get("email"),
        request.form.get("telefone"),
        request.form.get("cref"),
        request.form.get("especialidade")

    )

    return redirect(url_for("listar_instrutores"))


@app.route("/editar_instrutor/<int:id>")
def editar_instrutor(id):

    instrutor = buscar_instrutor(id)

    return render_template(

        "editar_instrutor.html",

        instrutor=instrutor

    )


@app.route("/atualizar_instrutor/<int:id>", methods=["POST"])
def atualizar_instrutor(id):

    atualizar_instrutor(

        id,

        request.form.get("nome"),
        request.form.get("email"),
        request.form.get("telefone"),
        request.form.get("cref"),
        request.form.get("especialidade")

    )

    return redirect(url_for("listar_instrutores"))


@app.route("/excluir_instrutor/<int:id>")
def excluir_instrutor_rota(id):

    excluir_instrutor(id)

    return redirect(url_for("listar_instrutores"))


# ===========================
# EXERCÍCIOS
# ===========================

@app.route("/exercicios")
def listar_exercicios():

    exercicios = listar_exercicios()

    return render_template(
        "exercicios.html",
        exercicios=exercicios
    )


@app.route("/cadastrar_exercicio", methods=["POST"])
def cadastrar_exercicio():

    inserir_exercicios(
        request.form.get("nome"),
        request.form.get("grupo_muscular"),
        request.form.get("series"),
        request.form.get("repeticoes")
    )

    return redirect(url_for("listar_exercicios"))


@app.route("/editar_exercicio/<int:id>")
def editar_exercicio(id):

    exercicio = buscar_exercicios(id)

    return render_template(
        "editar_exercicio.html",
        exercicio=exercicio
    )


@app.route("/atualizar_exercicio/<int:id>", methods=["POST"])
def atualizar_exercicio(id):

    atualizar_exercicios(
        id,
        request.form.get("nome"),
        request.form.get("grupo_muscular"),
        request.form.get("series"),
        request.form.get("repeticoes")
    )

    return redirect(url_for("listar_exercicios"))


@app.route("/excluir_exercicio/<int:id>")
def excluir_exercicio_rota(id):

    excluir_exercicios(id)

    return redirect(url_for("listar_exercicios"))


# ===========================
# TREINOS
# ===========================

@app.route("/treinos")
def pagina_treinos():

    treinos = listar_treinos()

    alunos = listar_alunos_db()

    instrutores = listar_instrutores()

    return render_template(
        "treinos.html",
        treinos=treinos,
        alunos=alunos,
        instrutores=instrutores
    )


@app.route("/cadastrar_treino", methods=["POST"])
def cadastrar_treino():

    inserir_treinos(
        request.form.get("nome"),
        request.form.get("descricao"),
        request.form.get("aluno_id"),
        request.form.get("instrutor_id")
    )

    return redirect(url_for("listar_treinos"))


@app.route("/editar_treino/<int:id>")
def editar_treino(id):

    treino = buscar_treinos(id)

    alunos = listar_alunos_db()

    instrutores = listar_instrutores()

    return render_template(
        "editar_treino.html",
        treino=treino,
        alunos=alunos,
        instrutores=instrutores
    )


@app.route("/atualizar_treino/<int:id>", methods=["POST"])
def atualizar_treino(id):

    atualizar_treinos(
        id,
        request.form.get("nome"),
        request.form.get("descricao"),
        request.form.get("aluno_id"),
        request.form.get("instrutor_id")
    )

    return redirect(url_for("listar_treinos"))


@app.route("/excluir_treino/<int:id>")
def excluir_treino_rota(id):

    excluir_treinos(id)

    return redirect(url_for("listar_treinos"))


# ===========================
# AVALIAÇÕES
# ===========================

@app.route("/avaliacoes")
def pagina_avaliacoes():

    avaliacoes = listar_avaliacoes()
    alunos = listar_alunos_db()
    instrutores = listar_instrutores()

    return render_template(
        "avaliacoes.html",
        avaliacoes=avaliacoes,
        alunos=alunos,
        instrutores=instrutores
    )


@app.route("/cadastrar_avaliacao", methods=["POST"])
def cadastrar_avaliacao():

    inserir_avaliacoes(
        request.form.get("aluno_id"),
        request.form.get("instrutor_id"),
        request.form.get("peso"),
        request.form.get("altura"),
        request.form.get("imc"),
        request.form.get("percentual_gordura"),
        request.form.get("observacoes")
    )

    return redirect(url_for("listar_avaliacoes"))


@app.route("/editar_avaliacao/<int:id>")
def editar_avaliacao(id):

    avaliacao = buscar_avaliacoes(id)

    alunos = listar_alunos_db()
    instrutores = listar_instrutores()

    return render_template(
        "editar_avaliacao.html",
        avaliacao=avaliacao,
        alunos=alunos,
        instrutores=instrutores
    )


@app.route("/atualizar_avaliacao/<int:id>", methods=["POST"])
def atualizar_avaliacao(id):

    atualizar_avaliacoes(
        id,
        request.form.get("aluno_id"),
        request.form.get("instrutor_id"),
        request.form.get("peso"),
        request.form.get("altura"),
        request.form.get("imc"),
        request.form.get("percentual_gordura"),
        request.form.get("observacoes")
    )

    return redirect(url_for("listar_avaliacoes"))


@app.route("/excluir_avaliacao/<int:id>")
def excluir_avaliacao_rota(id):

    excluir_avaliacoes(id)

    return redirect(url_for("listar_avaliacoes"))


# ===========================
# PLANOS
# ===========================

@app.route("/planos")
def pagina_planos():

    planos = listar_planos()

    return render_template(
        "planos.html",
        planos=planos
    )


@app.route("/cadastrar_plano", methods=["POST"])
def cadastrar_plano():

    inserir_planos(
        request.form.get("nome"),
        request.form.get("valor"),
        request.form.get("duracao")
    )

    return redirect(url_for("listar_planos"))


@app.route("/editar_plano/<int:id>")
def editar_plano(id):

    plano = buscar_planos(id)

    return render_template(
        "editar_plano.html",
        plano=plano
    )


@app.route("/atualizar_plano/<int:id>", methods=["POST"])
def atualizar_plano(id):

    atualizar_planos(
        id,
        request.form.get("nome"),
        request.form.get("valor"),
        request.form.get("duracao")
    )

    return redirect(url_for("listar_planos"))


@app.route("/excluir_plano/<int:id>")
def excluir_plano_rota(id):

    excluir_planos(id)

    return redirect(url_for("listar_planos"))


# ===========================
# PAGAMENTOS
# ===========================

@app.route("/pagamentos")
def pagina_pagamentos():

    pagamentos = listar_pagamentos()

    alunos = listar_alunos_db()

    planos = listar_planos()

    return render_template(
        "pagamentos.html",
        pagamentos=pagamentos,
        alunos=alunos,
        planos=planos
    )


@app.route("/cadastrar_pagamento", methods=["POST"])
def cadastrar_pagamento():

    inserir_pagamentos(
        request.form.get("aluno_id"),
        request.form.get("plano_id"),
        request.form.get("valor"),
        request.form.get("data"),
        request.form.get("status")
    )

    return redirect(url_for("listar_pagamentos"))


@app.route("/editar_pagamento/<int:id>")
def editar_pagamento(id):

    pagamento = buscar_pagamentos(id)

    alunos = listar_alunos_db()

    planos = listar_planos()

    return render_template(
        "editar_pagamento.html",
        pagamento=pagamento,
        alunos=alunos,
        planos=planos
    )


@app.route("/atualizar_pagamento/<int:id>", methods=["POST"])
def atualizar_pagamento(id):

    atualizar_pagamentos(
        id,
        request.form.get("aluno_id"),
        request.form.get("plano_id"),
        request.form.get("valor"),
        request.form.get("data"),
        request.form.get("status")
    )

    return redirect(url_for("listar_pagamentos"))


@app.route("/excluir_pagamento/<int:id>")
def excluir_pagamento_rota(id):

    excluir_pagamentos(id)

    return redirect(url_for("listar_pagamentos"))


# ===========================
# DOCUMENTOS
# ===========================

@app.route("/documentos")
def pagina_documentos():

    documentos = listar_documentos()
    alunos = listar_alunos_db()

    return render_template(
        "documentos.html",
        documentos=documentos,
        alunos=alunos
    )


@app.route("/cadastrar_documento", methods=["POST"])
def cadastrar_documento():

    inserir_documentos(
        request.form.get("aluno_id"),
        request.form.get("tipo"),
        request.form.get("arquivo")
    )

    return redirect(url_for("listar_documentos"))


@app.route("/editar_documento/<int:id>")
def editar_documento(id):

    documento = buscar_documentos(id)

    alunos = listar_alunos_db()

    return render_template(
        "editar_documento.html",
        documento=documento,
        alunos=alunos
    )


@app.route("/atualizar_documento/<int:id>", methods=["POST"])
def atualizar_documento(id):

    atualizar_documentos(
        id,
        request.form.get("aluno_id"),
        request.form.get("tipo"),
        request.form.get("arquivo")
    )

    return redirect(url_for("listar_documentos"))


@app.route("/excluir_documento/<int:id>")
def excluir_documento_rota(id):

    excluir_documentos(id)

    return redirect(url_for("listar_documentos"))


# ===========================
# HORÁRIOS
# ===========================

@app.route("/horarios")
def pagina_horarios():

    horarios = listar_horarios()

    return render_template(
        "horarios.html",
        horarios=horarios
    )


@app.route("/cadastrar_horario", methods=["POST"])
def cadastrar_horario():

    inserir_horarios(
        request.form.get("data"),
        request.form.get("hora"),
        request.form.get("disponivel")
    )

    return redirect(url_for("listar_horarios"))


@app.route("/editar_horario/<int:id>")
def editar_horario(id):

    horario = buscar_horarios(id)

    return render_template(
        "editar_horario.html",
        horario=horario
    )


@app.route("/atualizar_horario/<int:id>", methods=["POST"])
def atualizar_horario(id):

    atualizar_horarios(
        id,
        request.form.get("data"),
        request.form.get("hora"),
        request.form.get("disponivel")
    )

    return redirect(url_for("listar_horarios"))


@app.route("/excluir_horario/<int:id>")
def excluir_horario_rota(id):

    excluir_horarios(id)

    return redirect(url_for("listar_horarios"))


# ===========================
# AGENDAMENTOS
# ===========================

@app.route("/agendamentos")
def pagina_agendamentos():

    agendamentos = listar_agendamentos()
    alunos = listar_alunos_db()
    instrutores = listar_instrutores()
    horarios = listar_horarios()

    return render_template(
        "agendamentos.html",
        agendamentos=agendamentos,
        alunos=alunos,
        instrutores=instrutores,
        horarios=horarios
    )


@app.route("/cadastrar_agendamento", methods=["POST"])
def cadastrar_agendamento():

    inserir_agendamentos(
        request.form.get("aluno_id"),
        request.form.get("instrutor_id"),
        request.form.get("horario_id"),
        request.form.get("status")
    )

    return redirect(url_for("listar_agendamentos"))


@app.route("/editar_agendamento/<int:id>")
def editar_agendamento(id):

    agendamento = buscar_agendamentos(id)

    alunos = listar_alunos_db()
    instrutores = listar_instrutores()
    horarios = listar_horarios()

    return render_template(
        "editar_agendamento.html",
        agendamento=agendamento,
        alunos=alunos,
        instrutores=instrutores,
        horarios=horarios
    )


@app.route("/atualizar_agendamento/<int:id>", methods=["POST"])
def atualizar_agendamento(id):

    atualizar_agendamentos(
        id,
        request.form.get("aluno_id"),
        request.form.get("instrutor_id"),
        request.form.get("horario_id"),
        request.form.get("status")
    )

    return redirect(url_for("listar_agendamentos"))


@app.route("/excluir_agendamento/<int:id>")
def excluir_agendamento_rota(id):

    excluir_agendamentos(id)

    return redirect(url_for("listar_agendamentos"))


# ===========================
# TREINO X EXERCÍCIOS
# ===========================

@app.route("/treino_exercicios")
def pagina_treino_exercicios():

    relacoes = listar_treino_exercicios()
    treinos = listar_treinos()
    exercicios = listar_exercicios()

    return render_template(
        "treino_exercicios.html",
        relacoes=relacoes,
        treinos=treinos,
        exercicios=exercicios
    )


@app.route("/cadastrar_treino_exercicio", methods=["POST"])
def cadastrar_treino_exercicio():

    inserir_treino_exercicios(
        request.form.get("treino_id"),
        request.form.get("exercicio_id")
    )

    return redirect(url_for("listar_treino_exercicios"))


@app.route("/editar_treino_exercicio/<int:id>")
def editar_treino_exercicio(id):

    relacao = buscar_treino_exercicios(id)

    treinos = listar_treinos()
    exercicios = listar_exercicios()

    return render_template(
        "editar_treino_exercicio.html",
        relacao=relacao,
        treinos=treinos,
        exercicios=exercicios
    )


@app.route("/atualizar_treino_exercicio/<int:id>", methods=["POST"])
def atualizar_treino_exercicio(id):

    atualizar_treino_exercicios(
        id,
        request.form.get("treino_id"),
        request.form.get("exercicio_id")
    )

    return redirect(url_for("listar_treino_exercicios"))


@app.route("/excluir_treino_exercicio/<int:id>")
def excluir_treino_exercicio_rota(id):

    excluir_treino_exercicios(id)

    return redirect(url_for("listar_treino_exercicios"))


if __name__ == "__main__":
    app.run(debug=True)