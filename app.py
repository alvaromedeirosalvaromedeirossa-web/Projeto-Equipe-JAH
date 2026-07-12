from flask import Flask, render_template, request, redirect, url_for
import database as db
from models.aluno import Aluno
from models.instrutor import Instrutor
from models.exercicio import Exercicio
from models.treino import Treino
from models.avaliacaoFisica import AvaliacaoFisica
from models.plano import Plano
from models.pagamento import Pagamento
from models.documento import Documento
from models.horario import Horario
from models.agendamento import Agendamento
from models.treinoExercicio import TreinoExercicio

app = Flask(__name__)
app.secret_key = "academia123"
db.criar_tabelas()

LOGIN = "admin"
SENHA = "123"

@app.route("/")
def home(): return render_template("index.html")

@app.route("/autenticar", methods=["POST"])
def autenticar():
    if request.form.get("usuario") == LOGIN and request.form.get("senha") == SENHA:
        return redirect(url_for("painel"))
    return render_template("index.html", mensagem="Login ou senha inválidos.")

@app.route("/autentica", methods=["POST"])
def informacoes_pessoais():
    return render_template("Informações Pessoais.html", plano_escolhido=request.form.get("plano"), preco_escolhido=request.form.get("preco"), periodo_escolhido=request.form.get("periodo"))

@app.route("/painel")
def painel():
    return render_template("painel.html", total_alunos=len(db.listar_alunos_db()), total_instrutores=len(db.listar_instrutores()), total_treinos=len(db.listar_treinos()))

@app.route("/sair")
def sair(): return redirect(url_for("home"))

# ===========================
# ALUNOS
# ===========================
@app.route("/alunos")
def listar_alunos():
    return render_template("alunos.html", alunos=db.listar_alunos_db())

@app.route("/cadastrar_aluno", methods=["POST"])
def cadastrar_aluno():
    obj = Aluno(None, request.form.get('nome'), request.form.get('email'), request.form.get('telefone'), request.form.get('matricula'), request.form.get('peso'), request.form.get('altura'))
    db.inserir_aluno(obj.nome, obj.email, obj.telefone, obj.matricula, obj.peso, obj.altura)
    return redirect(url_for("listar_alunos"))

@app.route("/editar_aluno/<int:id>")
def editar_aluno(id):
    obj = db.buscar_aluno(id)
    return render_template("editar_aluno.html", aluno=obj)

@app.route("/atualizar_aluno/<int:id>", methods=["POST"])
def atualizar_aluno_rota(id):
    obj = Aluno(id, request.form.get('nome'), request.form.get('email'), request.form.get('telefone'), request.form.get('matricula'), request.form.get('peso'), request.form.get('altura'))
    db.atualizar_aluno_db(id, obj.nome, obj.email, obj.telefone, obj.matricula, obj.peso, obj.altura)
    return redirect(url_for("listar_alunos"))

@app.route("/excluir_aluno/<int:id>")
def excluir_aluno_rota(id):
    db.excluir_aluno(id)
    return redirect(url_for("listar_alunos"))

# ===========================
# INSTRUTORES
# ===========================
@app.route("/instrutores")
def listar_instrutores():
    return render_template("instrutores.html", instrutores=db.listar_instrutores())

@app.route("/cadastrar_instrutor", methods=["POST"])
def cadastrar_instrutor():
    obj = Instrutor(None, request.form.get('nome'), request.form.get('email'), request.form.get('telefone'), request.form.get('cref'), request.form.get('especialidade'))
    db.inserir_instrutor(obj.nome, obj.email, obj.telefone, obj.cref, obj.especialidade)
    return redirect(url_for("listar_instrutores"))

@app.route("/editar_instrutor/<int:id>")
def editar_instrutor(id):
    obj = db.buscar_instrutor(id)
    return render_template("editar_instrutor.html", instrutor=obj)

@app.route("/atualizar_instrutor/<int:id>", methods=["POST"])
def atualizar_instrutor_rota(id):
    obj = Instrutor(id, request.form.get('nome'), request.form.get('email'), request.form.get('telefone'), request.form.get('cref'), request.form.get('especialidade'))
    db.atualizar_instrutor(id, obj.nome, obj.email, obj.telefone, obj.cref, obj.especialidade)
    return redirect(url_for("listar_instrutores"))

@app.route("/excluir_instrutor/<int:id>")
def excluir_instrutor_rota(id):
    db.excluir_instrutor(id)
    return redirect(url_for("listar_instrutores"))

# ===========================
# EXERCICIOS
# ===========================
@app.route("/exercicios")
def listar_exercicios():
    return render_template("exercicios.html", exercicios=db.listar_exercicios())

@app.route("/cadastrar_exercicio", methods=["POST"])
def cadastrar_exercicio():
    obj = Exercicio(None, request.form.get('nome'), request.form.get('grupo_muscular'), request.form.get('series'), request.form.get('repeticoes'))
    db.inserir_exercicios(obj.nome, obj.grupo_muscular, obj.series, obj.repeticoes)
    return redirect(url_for("listar_exercicios"))

@app.route("/editar_exercicio/<int:id>")
def editar_exercicio(id):
    obj = db.buscar_exercicios(id)
    return render_template("editar_exercicio.html", exercicio=obj)

@app.route("/atualizar_exercicio/<int:id>", methods=["POST"])
def atualizar_exercicio_rota(id):
    obj = Exercicio(id, request.form.get('nome'), request.form.get('grupo_muscular'), request.form.get('series'), request.form.get('repeticoes'))
    db.atualizar_exercicios(id, obj.nome, obj.grupo_muscular, obj.series, obj.repeticoes)
    return redirect(url_for("listar_exercicios"))

@app.route("/excluir_exercicio/<int:id>")
def excluir_exercicio_rota(id):
    db.excluir_exercicios(id)
    return redirect(url_for("listar_exercicios"))

# ===========================
# TREINOS
# ===========================
@app.route("/treinos")
def listar_treinos():
    return render_template("treinos.html", treinos=db.listar_treinos())

@app.route("/cadastrar_treino", methods=["POST"])
def cadastrar_treino():
    obj = Treino(None, request.form.get('nome'), request.form.get('descricao'), request.form.get('aluno_id'), request.form.get('instrutor_id'))
    db.inserir_treinos(obj.nome, obj.descricao, obj.aluno_id, obj.instrutor_id)
    return redirect(url_for("listar_treinos"))

@app.route("/editar_treino/<int:id>")
def editar_treino(id):
    obj = db.buscar_treinos(id)
    return render_template("editar_treino.html", treino=obj)

@app.route("/atualizar_treino/<int:id>", methods=["POST"])
def atualizar_treino_rota(id):
    obj = Treino(id, request.form.get('nome'), request.form.get('descricao'), request.form.get('aluno_id'), request.form.get('instrutor_id'))
    db.atualizar_treinos(id, obj.nome, obj.descricao, obj.aluno_id, obj.instrutor_id)
    return redirect(url_for("listar_treinos"))

@app.route("/excluir_treino/<int:id>")
def excluir_treino_rota(id):
    db.excluir_treinos(id)
    return redirect(url_for("listar_treinos"))

# ===========================
# AVALIACOES
# ===========================
@app.route("/avaliacoes")
def listar_avaliacoes():
    return render_template("avaliacoes.html", avaliacoes=db.listar_avaliacoes())

@app.route("/cadastrar_avaliacao", methods=["POST"])
def cadastrar_avaliacao():
    obj = AvaliacaoFisica(None, request.form.get('aluno_id'), request.form.get('instrutor_id'), request.form.get('peso'), request.form.get('altura'), request.form.get('imc'), request.form.get('percentual_gordura'), request.form.get('observacoes'))
    db.inserir_avaliacoes(obj.aluno_id, obj.instrutor_id, obj.peso, obj.altura, obj.imc, obj.percentual_gordura, obj.observacoes)
    return redirect(url_for("listar_avaliacoes"))

@app.route("/editar_avaliacao/<int:id>")
def editar_avaliacao(id):
    obj = db.buscar_avaliacoes(id)
    return render_template("editar_avaliacao.html", avaliacao=obj)

@app.route("/atualizar_avaliacao/<int:id>", methods=["POST"])
def atualizar_avaliacao_rota(id):
    obj = AvaliacaoFisica(id, request.form.get('aluno_id'), request.form.get('instrutor_id'), request.form.get('peso'), request.form.get('altura'), request.form.get('imc'), request.form.get('percentual_gordura'), request.form.get('observacoes'))
    db.atualizar_avaliacoes(id, obj.aluno_id, obj.instrutor_id, obj.peso, obj.altura, obj.imc, obj.percentual_gordura, obj.observacoes)
    return redirect(url_for("listar_avaliacoes"))

@app.route("/excluir_avaliacao/<int:id>")
def excluir_avaliacao_rota(id):
    db.excluir_avaliacoes(id)
    return redirect(url_for("listar_avaliacoes"))

# ===========================
# PLANOS
# ===========================
@app.route("/planos")
def listar_planos():
    return render_template("planos.html", planos=db.listar_planos())

@app.route("/cadastrar_plano", methods=["POST"])
def cadastrar_plano():
    obj = Plano(None, request.form.get('nome'), request.form.get('valor'), request.form.get('duracao'))
    db.inserir_planos(obj.nome, obj.valor, obj.duracao)
    return redirect(url_for("listar_planos"))

@app.route("/editar_plano/<int:id>")
def editar_plano(id):
    obj = db.buscar_planos(id)
    return render_template("editar_plano.html", plano=obj)

@app.route("/atualizar_plano/<int:id>", methods=["POST"])
def atualizar_plano_rota(id):
    obj = Plano(id, request.form.get('nome'), request.form.get('valor'), request.form.get('duracao'))
    db.atualizar_planos(id, obj.nome, obj.valor, obj.duracao)
    return redirect(url_for("listar_planos"))

@app.route("/excluir_plano/<int:id>")
def excluir_plano_rota(id):
    db.excluir_planos(id)
    return redirect(url_for("listar_planos"))

# ===========================
# PAGAMENTOS
# ===========================
@app.route("/pagamentos")
def listar_pagamentos():
    return render_template("pagamentos.html", pagamentos=db.listar_pagamentos())

@app.route("/cadastrar_pagamento", methods=["POST"])
def cadastrar_pagamento():
    obj = Pagamento(None, request.form.get('aluno_id'), request.form.get('plano_id'), request.form.get('valor'), request.form.get('data'), request.form.get('status'))
    db.inserir_pagamentos(obj.aluno_id, obj.plano_id, obj.valor, obj.data, obj.status)
    return redirect(url_for("listar_pagamentos"))

@app.route("/editar_pagamento/<int:id>")
def editar_pagamento(id):
    obj = db.buscar_pagamentos(id)
    return render_template("editar_pagamento.html", pagamento=obj)

@app.route("/atualizar_pagamento/<int:id>", methods=["POST"])
def atualizar_pagamento_rota(id):
    obj = Pagamento(id, request.form.get('aluno_id'), request.form.get('plano_id'), request.form.get('valor'), request.form.get('data'), request.form.get('status'))
    db.atualizar_pagamentos(id, obj.aluno_id, obj.plano_id, obj.valor, obj.data, obj.status)
    return redirect(url_for("listar_pagamentos"))

@app.route("/excluir_pagamento/<int:id>")
def excluir_pagamento_rota(id):
    db.excluir_pagamentos(id)
    return redirect(url_for("listar_pagamentos"))

# ===========================
# DOCUMENTOS
# ===========================
@app.route("/documentos")
def listar_documentos():
    return render_template("documentos.html", documentos=db.listar_documentos())

@app.route("/cadastrar_documento", methods=["POST"])
def cadastrar_documento():
    obj = Documento(None, request.form.get('aluno_id'), request.form.get('tipo'), request.form.get('arquivo'))
    db.inserir_documentos(obj.aluno_id, obj.tipo, obj.arquivo)
    return redirect(url_for("listar_documentos"))

@app.route("/editar_documento/<int:id>")
def editar_documento(id):
    obj = db.buscar_documentos(id)
    return render_template("editar_documento.html", documento=obj)

@app.route("/atualizar_documento/<int:id>", methods=["POST"])
def atualizar_documento_rota(id):
    obj = Documento(id, request.form.get('aluno_id'), request.form.get('tipo'), request.form.get('arquivo'))
    db.atualizar_documentos(id, obj.aluno_id, obj.tipo, obj.arquivo)
    return redirect(url_for("listar_documentos"))

@app.route("/excluir_documento/<int:id>")
def excluir_documento_rota(id):
    db.excluir_documentos(id)
    return redirect(url_for("listar_documentos"))

# ===========================
# HORARIOS
# ===========================
@app.route("/horarios")
def listar_horarios():
    return render_template("horarios.html", horarios=db.listar_horarios())

@app.route("/cadastrar_horario", methods=["POST"])
def cadastrar_horario():
    obj = Horario(None, request.form.get('data'), request.form.get('hora'), request.form.get('disponivel'))
    db.inserir_horarios(obj.data, obj.hora, obj.disponivel)
    return redirect(url_for("listar_horarios"))

@app.route("/editar_horario/<int:id>")
def editar_horario(id):
    obj = db.buscar_horarios(id)
    return render_template("editar_horario.html", horario=obj)

@app.route("/atualizar_horario/<int:id>", methods=["POST"])
def atualizar_horario_rota(id):
    obj = Horario(id, request.form.get('data'), request.form.get('hora'), request.form.get('disponivel'))
    db.atualizar_horarios(id, obj.data, obj.hora, obj.disponivel)
    return redirect(url_for("listar_horarios"))

@app.route("/excluir_horario/<int:id>")
def excluir_horario_rota(id):
    db.excluir_horarios(id)
    return redirect(url_for("listar_horarios"))

# ===========================
# AGENDAMENTOS
# ===========================
@app.route("/agendamentos")
def listar_agendamentos():
    return render_template("agendamentos.html", agendamentos=db.listar_agendamentos())

@app.route("/cadastrar_agendamento", methods=["POST"])
def cadastrar_agendamento():
    obj = Agendamento(None, request.form.get('aluno_id'), request.form.get('instrutor_id'), request.form.get('horario_id'), request.form.get('status'))
    db.inserir_agendamentos(obj.aluno_id, obj.instrutor_id, obj.horario_id, obj.status)
    return redirect(url_for("listar_agendamentos"))

@app.route("/editar_agendamento/<int:id>")
def editar_agendamento(id):
    obj = db.buscar_agendamentos(id)
    return render_template("editar_agendamento.html", agendamento=obj)

@app.route("/atualizar_agendamento/<int:id>", methods=["POST"])
def atualizar_agendamento_rota(id):
    obj = Agendamento(id, request.form.get('aluno_id'), request.form.get('instrutor_id'), request.form.get('horario_id'), request.form.get('status'))
    db.atualizar_agendamentos(id, obj.aluno_id, obj.instrutor_id, obj.horario_id, obj.status)
    return redirect(url_for("listar_agendamentos"))

@app.route("/excluir_agendamento/<int:id>")
def excluir_agendamento_rota(id):
    db.excluir_agendamentos(id)
    return redirect(url_for("listar_agendamentos"))

# ===========================
# TREINO_EXERCICIOS
# ===========================
@app.route("/treino_exercicios")
def listar_treino_exercicios():
    return render_template("treino_exercicios.html", treino_exercicios=db.listar_treino_exercicios())

@app.route("/cadastrar_treino_exercicio", methods=["POST"])
def cadastrar_treino_exercicio():
    obj = TreinoExercicio(None, request.form.get('treino_id'), request.form.get('exercicio_id'))
    db.inserir_treino_exercicios(obj.treino_id, obj.exercicio_id)
    return redirect(url_for("listar_treino_exercicios"))

@app.route("/editar_treino_exercicio/<int:id>")
def editar_treino_exercicio(id):
    obj = db.buscar_treino_exercicios(id)
    return render_template("editar_treino_exercicio.html", treino_exercicio=obj)

@app.route("/atualizar_treino_exercicio/<int:id>", methods=["POST"])
def atualizar_treino_exercicio_rota(id):
    obj = TreinoExercicio(id, request.form.get('treino_id'), request.form.get('exercicio_id'))
    db.atualizar_treino_exercicios(id, obj.treino_id, obj.exercicio_id)
    return redirect(url_for("listar_treino_exercicios"))

@app.route("/excluir_treino_exercicio/<int:id>")
def excluir_treino_exercicio_rota(id):
    db.excluir_treino_exercicios(id)
    return redirect(url_for("listar_treino_exercicios"))

if __name__ == "__main__":
    app.run(debug=True)
