def autenticacao(usuario, senha):
    if usuario == 'admim' and senha == '123':
        return True
    else:
        return False
retorno = autenticacao('admin','456')
print(retorno)