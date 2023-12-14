from flask import Flask, render_template, request, redirect, session, flash


app = Flask(__name__)
app.secret_key = 'Senai'

class cadsport:
    def __init__(self, nome, jogo, posicao, ranking):

        self.nome = nome
        self.jogo = jogo
        self.posicao = posicao
        self.ranking = ranking

lista = []


@app.route('/Sport')
def sport():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Sport.html', Titulo="Os competidores: ", ListaSport=lista)

@app.route('/cadastro')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Cadastro.html', Titulo = "Cadastro dos jogadores")

@app.route('/criar', methods=['POST'])
def criar():
    if 'salvar' in request.form:
        nome = request.form['nome']
        jogo = request.form['jogo']
        posicao = request.form['posicao']
        ranking = request.form['ranking']
        obj = cadsport(nome,jogo,posicao,ranking)

        lista.append(obj)
        return redirect('/Sport')
    elif 'deslogar' in request.form:
        session.clear()
        return redirect('/')

@app.route('/excluir/<nomesport>', methods=['GET', 'DELETE'])
def excluir(nomesport):
    for i, spt in enumerate(lista):
        if spt.nome == nomesport:
            lista.pop(i)
            break

    return redirect('/Sport')

@app.route('/editar/<nomesport>', methods=['GET'])
def editar(nomesport):
    for i, spt in enumerate(lista):
        if spt.nome == nomesport:
            return render_template("Editar.html", sport=spt, Titulo="Alterar")

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    nome = request.form['nome']
    for i, spt in enumerate(lista):
        if spt.nome == nome:
            spt.nome = request.form['nome']
            spt.jogo = request.form['jogo']
            spt.posicao = request.form['posicao']
            spt.ranking = request.form['ranking']
    return redirect('/Sport')

@app.route('/')
def login():
    session.clear()
    return render_template('Login.html', Titulo='Faça Login')

@app.route('/autenticar', methods= ['POST'])
def autenticar():
    if request.form['usuario']== 'Bruno' and request.form ['senha']=='123':
        session ['Usuario_Logado'] = request.form['usuario']
        flash ('Usuario Logado com Sucesso')
        return redirect('/cadastro')
    else:
        flash('Usuario não encontrado')
        return redirect('/')


if __name__ == '__main__':
    app.run()