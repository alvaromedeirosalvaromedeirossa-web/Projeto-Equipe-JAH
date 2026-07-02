from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
from database import *
criar_tabelas()

# LOGIN PADRÃO
loginPadrao = "admin"
senhaPadrao = "123"

# ------------------ HOME ------------------
@app.route('/')
def home():
    return render_template("index.html") 

@app.route("/autenticar", methods=['POST'])
def autenticarUsuario():
    global senhaPadrao

    login = request.form.get("usuario")
    senha = request.form.get("senha")
    
    if login == loginPadrao and senha == senhaPadrao:
        msg = "Você está autenticado!"
        return render_template("painel.html", mensagem=msg)
    else:
        msg = "Login ou senha incorretos"
        return render_template("index.html", mensagem=msg)

@app.route("/autentica", methods=['POST'])
def InformacoesPessoais():
    plano_selecionado = request.form.get("plano")
    preco_selecionado = request.form.get("preco")
    periodo_selecionado = request.form.get("periodo")
    
    return render_template(
        "Informações Pessoais.html", 
        plano_escolhido=plano_selecionado,
        preco_escolhido=preco_selecionado,
        periodo_escolhido=periodo_selecionado
    )

# ------------------ PAINEL ------------------
@app.route("/painel")
def painel():
    return render_template("painel.html")

@app.route("/sair")
def sair():
    # Redireciona o usuário de volta para a página inicial do site
    return redirect("/")
# ------------------ ROTAS DE ALUNOS ------------------

# 1. Listar Alunos e abrir página de cadastro
@app.route("/alunos")
def listar_alunos():
    alunos = listar_alunos_db()
    return render_template("alunos.html", alunos=alunos)

# 2. Cadastrar Aluno
@app.route("/cadastrar_aluno", methods=['POST'])
def cadastrar_aluno():
    global proximo_id_aluno
    
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    matricula = request.form.get("matricula")
    peso = request.form.get("peso")
    altura = request.form.get("altura")
    
    # Adiciona na lista simulada
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

# 3. Abrir página de Edição de Aluno
@app.route("/editar_aluno/<int:id>")
def editar_aluno(id):
    # Procura o aluno pelo ID na nossa lista
    aluno = buscar_aluno(id)

    return render_template("editar_aluno.html", aluno=aluno)

# 4. Salvar Alterações do Aluno (Atualizar)
@app.route("/atualizar_aluno/<int:id>", methods=['POST'])
def atualizar_aluno(id):
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    matricula = request.form.get("matricula")
    peso = request.form.get("peso")
    altura = request.form.get("altura")
    
    # Atualiza o aluno correspondente
    atualizar_aluno_db(
        id,
        nome,
        email,
        telefone,
        matricula,
        peso,
        altura
    )

# 5. Excluir Aluno
@app.route("/excluir_aluno/<int:id>")
def excluir_aluno(id):
    global lista_alunos
    # Filtra a lista removendo o aluno com o ID selecionado
    excluir_aluno(id)


# ------------------ ROTAS DE INSTRUTORES ------------------

# 1. Listar Instrutores e abrir página de cadastro
@app.route("/instrutores")
def listar_instrutores():
    instrutores = listar_instrutores_db()
    return render_template("instrutores.html", instrutores=instrutores)

# 2. Cadastrar Instrutor
@app.route("/cadastrar_instrutor", methods=['POST'])
def cadastrar_instrutor():
    global proximo_id_instrutor
    
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    cref = request.form.get("cref")
    
    # Adiciona na lista simulada de instrutores
    @app.route("/cadastrar_instrutor", methods=["POST"])
    def cadastrar_instrutor():

        inserir_instrutor(
            request.form.get("nome"),
            request.form.get("email"),
            request.form.get("telefone"),
            request.form.get("matricula"),
            request.form.get("peso"),
            request.form.get("altura")
            )

# 3. Excluir Instrutor
@app.route("/excluir_instrutor/<int:id>")
def excluir_instrutor(id):
    global lista_instrutores
    # Filtra a lista removendo o instrutor com o ID selecionado
    excluir_instrutor(id)


if __name__ == '__main__':
    app.run(debug=True)