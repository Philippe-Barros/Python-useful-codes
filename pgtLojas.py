print('{:=^40}'.format(' LOJAS GUANABARA ')) # : centralizar; = símbolo; Nº qtd de espaços desejados
preco = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista em dinheiro/débito')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    desconto = preco - ((preco * 10) / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco, desconto))
elif opcao == 2:
    desconto = preco - ((preco * 5) / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco, desconto))
elif opcao == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS. Totalizando R$ {:.2f} no final'.format(parcela, preco))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    precoJuros = preco + ((preco * 20) / 100)
    parcelaJuros = precoJuros / parcela
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(parcela, parcelaJuros))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, precoJuros))
else:
    print('ERRO! Opção inválida!')
