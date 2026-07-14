from functools import wraps

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import database


# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

app = Flask(__name__)

app.secret_key = "academia_poo_2026"

database.criar_tabelas()


# ==========================================================
# LOGIN
# ==========================================================

USUARIO = "admin"
SENHA = "123456"


def login_required(func):
    """
    Protege as páginas do sistema.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "usuario" not in session:

            flash(
                "Faça login para acessar o sistema.",
                "warning"
            )

            return redirect(url_for("login"))

        return func(*args, **kwargs)

    return wrapper


# ==========================================================
# LOGIN
# ==========================================================

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form.get("usuario")

        senha = request.form.get("senha")

        if usuario == USUARIO and senha == SENHA:

            session["usuario"] = usuario

            flash(
                "Login realizado com sucesso.",
                "success"
            )

            return redirect(
                url_for("dashboard")
            )

        flash(
            "Usuário ou senha inválidos.",
            "danger"
        )

    return render_template("login.html")


# ==========================================================
# LOGOUT
# ==========================================================

@app.route("/logout")
@login_required
def logout():

    session.clear()

    flash(
        "Logout realizado com sucesso.",
        "info"
    )

    return redirect(
        url_for("login")
    )

# ==========================================================
# DASHBOARD
# ==========================================================

@app.route("/dashboard")
@login_required
def dashboard():

    alunos = database.listar_alunos()

    instrutores = database.listar_instrutores()

    exercicios = database.listar_exercicios()

    treinos = database.listar_treinos()

    planos = database.listar_planos()

    pagamentos = database.listar_pagamentos()

    avaliacoes = database.listar_avaliacoes()

    agendamentos = database.listar_agendamentos()

    return render_template(

        "dashboard.html",

        total_alunos=len(alunos),

        total_instrutores=len(instrutores),

        total_exercicios=len(exercicios),

        total_treinos=len(treinos),

        total_planos=len(planos),

        total_pagamentos=len(pagamentos),

        total_avaliacoes=len(avaliacoes),

        total_agendamentos=len(agendamentos)

    )

# ==========================================================
# ERROS
# ==========================================================

@app.errorhandler(404)
def erro404(error):

    return render_template(
        "404.html"
    ), 404


@app.errorhandler(500)
def erro500(error):

    return render_template(
        "500.html"
    ), 500

# ==========================================================
# ALUNOS
# ==========================================================

@app.route("/alunos")
@login_required
def listar_alunos():

    alunos = database.listar_alunos()

    return render_template(
        "alunos/listar.html",
        alunos=alunos
    )


@app.route("/alunos/novo", methods=["GET", "POST"])
@login_required
def novo_aluno():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        matricula = request.form["matricula"]
        peso = request.form["peso"]
        altura = request.form["altura"]

        sucesso = database.inserir_aluno(
            nome,
            email,
            telefone,
            matricula,
            peso,
            altura
        )

        if sucesso:

            flash(
                "Aluno cadastrado com sucesso!",
                "success"
            )

            return redirect(
                url_for("listar_alunos")
            )

        flash(
            "Erro ao cadastrar aluno.",
            "danger"
        )

    return render_template(
        "alunos/form.html"
    )

@app.route("/alunos/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_aluno(id):

    aluno = database.buscar_aluno(id)

    if not aluno:

        flash(
            "Aluno não encontrado.",
            "warning"
        )

        return redirect(
            url_for("listar_alunos")
        )

    if request.method == "POST":

        sucesso = database.atualizar_aluno(

            id,

            request.form["nome"],

            request.form["email"],

            request.form["telefone"],

            request.form["matricula"],

            request.form["peso"],

            request.form["altura"]

        )

        if sucesso:

            flash(
                "Aluno atualizado com sucesso.",
                "success"
            )

            return redirect(
                url_for("listar_alunos")
            )

        flash(
            "Erro ao atualizar aluno.",
            "danger"
        )

    return render_template(
        "alunos/form.html",
        aluno=aluno
    )

@app.route("/alunos/excluir/<int:id>")
@login_required
def excluir_aluno(id):

    sucesso = database.excluir_aluno(id)

    if sucesso:

        flash(
            "Aluno removido com sucesso.",
            "info"
        )

    else:

        flash(
            "Erro ao remover aluno.",
            "danger"
        )

    return redirect(
        url_for("listar_alunos")
    )

@app.route("/alunos/<int:id>")
@login_required
def detalhes_aluno(id):

    aluno = database.buscar_aluno(id)

    if not aluno:

        flash(
            "Aluno não encontrado.",
            "warning"
        )

        return redirect(
            url_for("listar_alunos")
        )

    treinos = database.buscar_treinos_aluno(id)

    pagamentos = database.buscar_pagamentos_aluno(id)

    plano = database.buscar_plano_do_aluno(id)

    agendamentos = database.buscar_agendamentos_aluno(id)

    documentos = database.buscar_documentos_aluno(id)

    return render_template(

        "alunos/detalhes.html",

        aluno=aluno,

        treinos=treinos,

        pagamentos=pagamentos,

        plano=plano,

        agendamentos=agendamentos,

        documentos=documentos

    )

@app.route("/alunos/buscar")
@login_required
def buscar_alunos():

    pesquisa = request.args.get("q", "").strip().lower()

    alunos = database.listar_alunos()

    resultado = []

    for aluno in alunos:

        if (
            pesquisa in aluno["nome"].lower()
            or
            pesquisa in aluno["matricula"].lower()
        ):

            resultado.append(aluno)

    return render_template(
        "alunos/listar.html",
        alunos=resultado,
        pesquisa=pesquisa
    )

# ==========================================================
# INSTRUTORES
# ==========================================================

@app.route("/instrutores")
@login_required
def listar_instrutores():

    instrutores = database.listar_instrutores()

    return render_template(
        "instrutores/listar.html",
        instrutores=instrutores
    )

@app.route("/instrutores/novo", methods=["GET", "POST"])
@login_required
def novo_instrutor():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        cref = request.form["cref"]
        especialidade = request.form["especialidade"]

        sucesso = database.inserir_instrutor(
            nome,
            email,
            telefone,
            cref,
            especialidade
        )

        if sucesso:

            flash(
                "Instrutor cadastrado com sucesso!",
                "success"
            )

            return redirect(
                url_for("listar_instrutores")
            )

        flash(
            "Erro ao cadastrar instrutor.",
            "danger"
        )

    return render_template(
        "instrutores/form.html"
    )

@app.route("/instrutores/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_instrutor(id):

    instrutor = database.buscar_instrutor(id)

    if not instrutor:

        flash(
            "Instrutor não encontrado.",
            "warning"
        )

        return redirect(
            url_for("listar_instrutores")
        )

    if request.method == "POST":

        sucesso = database.atualizar_instrutor(

            id,

            request.form["nome"],

            request.form["email"],

            request.form["telefone"],

            request.form["cref"],

            request.form["especialidade"]

        )

        if sucesso:

            flash(
                "Instrutor atualizado com sucesso.",
                "success"
            )

            return redirect(
                url_for("listar_instrutores")
            )

        flash(
            "Erro ao atualizar instrutor.",
            "danger"
        )

    return render_template(
        "instrutores/form.html",
        instrutor=instrutor
    )

@app.route("/instrutores/excluir/<int:id>")
@login_required
def excluir_instrutor(id):

    sucesso = database.excluir_instrutor(id)

    if sucesso:

        flash(
            "Instrutor removido com sucesso.",
            "info"
        )

    else:

        flash(
            "Erro ao remover instrutor.",
            "danger"
        )

    return redirect(
        url_for("listar_instrutores")
    )

@app.route("/instrutores/<int:id>")
@login_required
def detalhes_instrutor(id):

    instrutor = database.buscar_instrutor(id)

    if not instrutor:

        flash(
            "Instrutor não encontrado.",
            "warning"
        )

        return redirect(
            url_for("listar_instrutores")
        )

    treinos = database.buscar_treinos_instrutor(id)

    return render_template(

        "instrutores/detalhes.html",

        instrutor=instrutor,

        treinos=treinos

    )

@app.route("/instrutores/buscar")
@login_required
def buscar_instrutores():

    pesquisa = request.args.get("q", "").strip().lower()

    instrutores = database.listar_instrutores()

    resultado = []

    for instrutor in instrutores:

        if (
            pesquisa in instrutor["nome"].lower()
            or
            pesquisa in instrutor["cref"].lower()
            or
            pesquisa in instrutor["especialidade"].lower()
        ):
            resultado.append(instrutor)

    return render_template(
        "instrutores/listar.html",
        instrutores=resultado,
        pesquisa=pesquisa
    )

# ==========================================================
# EXERCÍCIOS
# ==========================================================

@app.route("/exercicios")
@login_required
def listar_exercicios():

    exercicios = database.listar_exercicios()

    return render_template(
        "exercicios/listar.html",
        exercicios=exercicios
    )

@app.route("/exercicios/novo", methods=["GET", "POST"])
@login_required
def novo_exercicio():

    if request.method == "POST":

        sucesso = database.inserir_exercicio(

            request.form["nome"],
            request.form["grupo_muscular"],
            int(request.form["series"]),
            int(request.form["repeticoes"])

        )

        if sucesso:

            flash(
                "Exercício cadastrado com sucesso!",
                "success"
            )

            return redirect(
                url_for("listar_exercicios")
            )

        flash(
            "Erro ao cadastrar exercício.",
            "danger"
        )

    return render_template("exercicios/form.html")

@app.route("/exercicios/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_exercicio(id):

    exercicio = database.buscar_exercicio(id)

    if not exercicio:

        flash(
            "Exercício não encontrado.",
            "warning"
        )

        return redirect(
            url_for("listar_exercicios")
        )

    if request.method == "POST":

        sucesso = database.atualizar_exercicio(

            id,

            request.form["nome"],

            request.form["grupo_muscular"],

            int(request.form["series"]),

            int(request.form["repeticoes"])

        )

        if sucesso:

            flash(
                "Exercício atualizado com sucesso.",
                "success"
            )

            return redirect(
                url_for("listar_exercicios")
            )

        flash(
            "Erro ao atualizar exercício.",
            "danger"
        )

    return render_template(
        "exercicios/form.html",
        exercicio=exercicio
    )

@app.route("/exercicios/excluir/<int:id>")
@login_required
def excluir_exercicio(id):

    sucesso = database.excluir_exercicio(id)

    if sucesso:

        flash(
            "Exercício removido.",
            "info"
        )

    else:

        flash(
            "Erro ao remover exercício.",
            "danger"
        )

    return redirect(
        url_for("listar_exercicios")
    )

@app.route("/exercicios/buscar")
@login_required
def buscar_exercicios():

    pesquisa = request.args.get("q", "").strip().lower()

    exercicios = database.listar_exercicios()

    resultado = []

    for exercicio in exercicios:

        if (
            pesquisa in exercicio["nome"].lower()
            or
            pesquisa in exercicio["grupo_muscular"].lower()
        ):
            resultado.append(exercicio)

    return render_template(
        "exercicios/listar.html",
        exercicios=resultado,
        pesquisa=pesquisa
    )

# ==========================================================
# TREINOS
# ==========================================================

@app.route("/treinos")
@login_required
def listar_treinos():

    treinos = database.listar_treinos()

    return render_template(
        "treinos/listar.html",
        treinos=treinos
    )

@app.route("/treinos/novo", methods=["GET", "POST"])
@login_required
def novo_treino():

    alunos = database.listar_alunos()
    instrutores = database.listar_instrutores()

    if request.method == "POST":

        sucesso = database.inserir_treino(

            request.form["nome"],

            request.form["descricao"],

            request.form["aluno_id"],

            request.form["instrutor_id"]

        )

        if sucesso:

            flash(
                "Treino criado com sucesso!",
                "success"
            )

            return redirect(
                url_for("listar_treinos")
            )

        flash(
            "Erro ao criar treino.",
            "danger"
        )

    return render_template(

        "treinos/form.html",

        alunos=alunos,

        instrutores=instrutores

    )

@app.route("/treinos/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_treino(id):

    treino = database.buscar_treino(id)

    if not treino:

        flash(
            "Treino não encontrado.",
            "warning"
        )

        return redirect(url_for("listar_treinos"))

    alunos = database.listar_alunos()
    instrutores = database.listar_instrutores()

    if request.method == "POST":

        sucesso = database.atualizar_treino(

            id,

            request.form["nome"],

            request.form["descricao"],

            request.form["aluno_id"],

            request.form["instrutor_id"]

        )

        if sucesso:

            flash(
                "Treino atualizado com sucesso!",
                "success"
            )

            return redirect(
                url_for("listar_treinos")
            )

    return render_template(

        "treinos/form.html",

        treino=treino,

        alunos=alunos,

        instrutores=instrutores

    )

@app.route("/treinos/excluir/<int:id>")
@login_required
def excluir_treino(id):

    sucesso = database.excluir_treino(id)

    if sucesso:

        flash(
            "Treino removido.",
            "info"
        )

    else:

        flash(
            "Erro ao remover treino.",
            "danger"
        )

    return redirect(
        url_for("listar_treinos")
    )

# ==========================================================
# TREINO x EXERCÍCIOS
# ==========================================================

@app.route("/treinos/<int:treino_id>/exercicios")
@login_required
def treino_exercicios(treino_id):

    treino = database.buscar_treino(treino_id)

    exercicios = database.buscar_exercicios_treino(treino_id)

    todos = database.listar_exercicios()

    return render_template(

        "treinos/exercicios.html",

        treino=treino,

        exercicios=exercicios,

        todos=todos

    )


@app.route("/treinos/<int:treino_id>/adicionar", methods=["POST"])
@login_required
def adicionar_exercicio_treino(treino_id):

    sucesso = database.adicionar_exercicio_treino(

        treino_id,

        request.form["exercicio_id"]

    )

    if sucesso:

        flash(

            "Exercício adicionado ao treino.",

            "success"

        )

    else:

        flash(

            "Erro ao adicionar exercício.",

            "danger"

        )

    return redirect(

        url_for(

            "treino_exercicios",

            treino_id=treino_id

        )

    )


@app.route("/treinos/<int:treino_id>/remover/<int:exercicio_id>")
@login_required
def remover_exercicio_treino(treino_id, exercicio_id):

    database.remover_exercicio_treino(

        treino_id,

        exercicio_id

    )

    flash(

        "Exercício removido.",

        "info"

    )

    return redirect(

        url_for(

            "treino_exercicios",

            treino_id=treino_id

        )

    )

# ==========================================================
# PLANOS
# ==========================================================

@app.route("/planos")
@login_required
def listar_planos():

    planos = database.listar_planos()

    return render_template(

        "planos/listar.html",

        planos=planos

    )


@app.route("/planos/novo", methods=["GET","POST"])
@login_required
def novo_plano():

    if request.method == "POST":

        database.inserir_plano(
            request.form["nome"],
            float(request.form["valor"]),
            int(request.form["duracao"])
        )

        return redirect(url_for("listar_planos"))

    return render_template("planos/form.html", plano=None)


@app.route("/planos/editar/<int:id>", methods=["GET","POST"])
@login_required
def editar_plano(id):

    plano = database.buscar_plano(id)

    if request.method == "POST":

        database.atualizar_plano(

            id,

            request.form["nome"],

            request.form["valor"],

            request.form["duracao"]

        )

        flash(

            "Plano atualizado.",

            "success"

        )

        return redirect(

            url_for("listar_planos")

        )

    return render_template(

        "planos/form.html",

        plano=plano

    )


@app.route("/planos/excluir/<int:id>")
@login_required
def excluir_plano(id):

    database.excluir_plano(id)

    flash(

        "Plano removido.",

        "info"

    )

    return redirect(

        url_for("listar_planos")

    )

# ==========================================================
# PAGAMENTOS
# ==========================================================

@app.route("/pagamentos")
@login_required
def listar_pagamentos():

    pagamentos = database.listar_pagamentos()

    return render_template(
        "pagamentos/listar.html",
        pagamentos=pagamentos
    )


@app.route("/pagamentos/novo", methods=["GET","POST"])
@login_required
def novo_pagamento():

    alunos = database.listar_alunos()

    planos = database.listar_planos()

    if request.method == "POST":

        sucesso = database.inserir_pagamento(

            request.form["aluno_id"],

            request.form["plano_id"],

            request.form["valor"],

            request.form["data"],

            request.form["status"]

        )

        if sucesso:

            flash(

                "Pagamento registrado.",

                "success"

            )

            return redirect(

                url_for("listar_pagamentos")

            )

    return render_template(

        "pagamentos/form.html",

        alunos=alunos,

        planos=planos

    )


@app.route("/pagamentos/excluir/<int:id>")
@login_required
def excluir_pagamento(id):

    database.excluir_pagamento(id)

    flash(

        "Pagamento removido.",

        "info"

    )

    return redirect(

        url_for("listar_pagamentos")

    )

# ==========================================================
# AVALIAÇÕES FÍSICAS
# ==========================================================

def calcular_imc(peso, altura):
    try:
        peso = float(peso)
        altura = float(altura)

        if altura <= 0:
            return 0

        return round(peso / (altura ** 2), 2)

    except:
        return 0


@app.route("/avaliacoes")
@login_required
def listar_avaliacoes():

    avaliacoes = database.listar_avaliacoes()

    return render_template(
        "avaliacoes/listar.html",
        avaliacoes=avaliacoes
    )


@app.route("/avaliacoes/nova", methods=["GET", "POST"])
@login_required
def nova_avaliacao():

    alunos = database.listar_alunos()
    instrutores = database.listar_instrutores()

    if request.method == "POST":

        peso = request.form["peso"]
        altura = request.form["altura"]

        imc = calcular_imc(peso, altura)

        sucesso = database.inserir_avaliacao(

            request.form["aluno_id"],

            request.form["instrutor_id"],

            peso,

            altura,

            imc,

            request.form["percentual_gordura"],

            request.form["observacoes"]

        )

        if sucesso:

            flash(
                "Avaliação cadastrada com sucesso.",
                "success"
            )

            return redirect(url_for("listar_avaliacoes"))

    return render_template(
        "avaliacoes/form.html",
        alunos=alunos,
        instrutores=instrutores
    )

@app.route("/avaliacoes/excluir/<int:id>")
@login_required
def excluir_avaliacao(id):

    database.excluir_avaliacoes(id)

    flash(
        "Avaliação excluída com sucesso.",
        "success"
    )

    return redirect(url_for("listar_avaliacoes"))
    
# ==========================================================
# DOCUMENTOS
# ==========================================================

@app.route("/documentos")
@login_required
def listar_documentos():

    documentos = database.listar_documentos()

    return render_template(
        "documentos/listar.html",
        documentos=documentos
    )


@app.route("/documentos/novo", methods=["GET", "POST"])
@login_required
def novo_documento():

    alunos = database.listar_alunos()

    if request.method == "POST":

        sucesso = database.inserir_documento(

            request.form["aluno_id"],

            request.form["tipo"],

            request.form["arquivo"]

        )

        if sucesso:

            flash(
                "Documento cadastrado.",
                "success"
            )

            return redirect(url_for("listar_documentos"))

    return render_template(
        "documentos/form.html",
        alunos=alunos
    )

# ==========================================================
# HORÁRIOS
# ==========================================================

@app.route("/horarios")
@login_required
def listar_horarios():

    horarios = database.listar_horarios()

    return render_template(
        "horarios/listar.html",
        horarios=horarios
    )


@app.route("/horarios/novo", methods=["GET","POST"])
@login_required
def novo_horario():

    if request.method == "POST":

        sucesso = database.inserir_horario(

            request.form["data"],

            request.form["hora"],

            1

        )

        if sucesso:

            flash(
                "Horário cadastrado.",
                "success"
            )

            return redirect(url_for("listar_horarios"))

    return render_template(
        "horarios/form.html"
    )

# ==========================================================
# AGENDAMENTOS
# ==========================================================

@app.route("/agendamentos")
@login_required
def listar_agendamentos():

    agendamentos = database.listar_agendamentos()

    return render_template(
        "agendamentos/listar.html",
        agendamentos=agendamentos
    )


@app.route("/agendamentos/novo", methods=["GET","POST"])
@login_required
def novo_agendamento():

    if request.method == "POST":

        data = request.form["data"]
        hora = request.form["hora"]

        database.inserir_horarios(data, hora, 1)

        horario = database.executar(
            "SELECT id FROM horarios ORDER BY id DESC LIMIT 1",
            fetchone=True
        )

        database.inserir_agendamentos(
            request.form["aluno_id"],
            request.form["instrutor_id"],
            horario["id"],
            request.form["status"]
        )

        return redirect(url_for("listar_agendamentos"))

    alunos = database.listar_alunos()
    instrutores = database.listar_instrutores()

    return render_template(
        "agendamentos/form.html",
        alunos=alunos,
        instrutores=instrutores,
        agendamento=None
    )

@app.route("/agendamentos/excluir/<int:id>")
@login_required
def excluir_agendamento(id):

    database.excluir_agendamento(id)

    flash(
        "Agendamento removido.",
        "info"
    )

    return redirect(
        url_for("listar_agendamentos")
    )

# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)