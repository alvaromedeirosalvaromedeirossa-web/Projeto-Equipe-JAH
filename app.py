from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# LOGIN PADRÃO
loginPadrao = "admin"
senhaPadrao = "123"

# Listas na memória para simular o Banco de Dados (Evita erros ao testar)
lista_alunos = [
    # Exemplo: [id, nome, email, telefone, matricula, peso, altura]
    [1, "João Silva", "joao@email.com", "912345678", "MAT101", 80.0, 1.80]
]
lista_instrutores = [
    # Exemplo: [id, nome, email, telefone, cref]
    [1, "Carlos Treinador", "carlos@email.com", "987654321", "CREF1234"]
]

# ID autoincremento para as simulações
proximo_id_aluno = 2
proximo_id_instrutor = 2

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
    return render_template("alunos.html", alunos=lista_alunos)

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
    lista_alunos.append([proximo_id_aluno, nome, email, telefone, matricula, peso, altura])
    proximo_id_aluno += 1
    
    return redirect(url_for('listar_alunos'))

# 3. Abrir página de Edição de Aluno
@app.route("/editar_aluno/<int:id>")
def editar_aluno(id):
    # Procura o aluno pelo ID na nossa lista
    aluno_encontrado = None
    for aluno in lista_alunos:
        if aluno[0] == id:
            aluno_encontrado = aluno
            break
            
    if aluno_encontrado:
        return render_template("editar_aluno.html", aluno=aluno_encontrado)
    return redirect(url_for('listar_alunos'))

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
    for aluno in lista_alunos:
        if aluno[0] == id:
            aluno[1] = nome
            aluno[2] = email
            aluno[3] = telefone
            aluno[4] = matricula
            aluno[5] = peso
            aluno[6] = altura
            break
            
    return redirect(url_for('listar_alunos'))

# 5. Excluir Aluno
@app.route("/excluir_aluno/<int:id>")
def excluir_aluno(id):
    global lista_alunos
    # Filtra a lista removendo o aluno com o ID selecionado
    lista_alunos = [aluno for aluno in lista_alunos if aluno[0] != id]
    return redirect(url_for('listar_alunos'))


# ------------------ ROTAS DE INSTRUTORES ------------------

# 1. Listar Instrutores e abrir página de cadastro
@app.route("/instrutores")
def listar_instrutores():
    return render_template("instrutores.html", instrutores=lista_instrutores)

# 2. Cadastrar Instrutor
@app.route("/cadastrar_instrutor", methods=['POST'])
def cadastrar_instrutor():
    global proximo_id_instrutor
    
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    cref = request.form.get("cref")
    
    # Adiciona na lista simulada de instrutores
    lista_instrutores.append([proximo_id_instrutor, nome, email, telefone, cref])
    proximo_id_instrutor += 1
    
    return redirect(url_for('listar_instrutores'))

# 3. Excluir Instrutor
@app.route("/excluir_instrutor/<int:id>")
def excluir_instrutor(id):
    global lista_instrutores
    # Filtra a lista removendo o instrutor com o ID selecionado
    lista_instrutores = [i for i in lista_instrutores if i[0] != id]
    return redirect(url_for('listar_instrutores'))


if __name__ == '__main__':
    app.run(debug=True)