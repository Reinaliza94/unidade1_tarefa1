from flask import Flask
app = Flask (__name__)

# Crie uma rota que retorne a mensagem "Seja bem-vindo(a)!"

@app.route("/")
def index():
    return "Seja bem-vindo(a)!"

# Crie uma rota que receba como parâmetro o nome do usuário e retorne a mensagem "Olá, [nome do usuário]!"

@app.route("/resultado/<nome>")
def resultado(nome):
    return f"Olá, {nome}!"

# Crie uma rota que receba como parametro nome, formação acadêmica, experiência profissional e retorne uma mensagem com essas informações.

@app.route("/autor/<nome>/<formacao>/<experiencia>")
def autor(nome, formacao, experiencia):
    return f"Nome: {nome}, Formação Acadêmica: {formacao}, Experiência Profissional: {experiencia}"

app.run(debug=True)