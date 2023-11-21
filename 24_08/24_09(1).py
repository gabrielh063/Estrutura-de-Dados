opcao = 1
bd_estoque =[]
while opcao !=3:
    print('='*10)
    print('1 Adicionar')
    print('2 Consultar Estoque')
    print('3 Sair')
    opcao = int(input('Opcao >>>>> '))
    if opcao == 1:
        print('Adicionar')
        codigo = int(input('Codigo'))
        nome = input('Nome; ')
        descricao = input('Descricao: ')
        preco = float(input('Preco: '))
        produto = ['codigo','nome','descricao','preco']
        bd_estoque.append(produto)
        print('adicionado com sucesso')
    elif opcao ==2:
        print('Mostrar Estoque')
        print(bd_estoque)
        for prod in bd_estoque:
            print(prod[0], end='\t')
            print(prod[1], end='\t')
            print(prod[2], end='\t')
            print(prod[3])
    elif opcao == 3:
        print('Saindo')
    else:
        print('Opcao incorreta')