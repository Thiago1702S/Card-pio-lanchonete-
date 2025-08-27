import time
print('Olá, seja bem vindo!')
time.sleep(1)
print('\n>>> CARDÁPIO <<<')
time.sleep(1)
cardapio = {
    1: ("XBURGUER", 20.00),
    2: ("XSALADA", 25.00),
    3: ("XEGG", 30.00),
    4: ("XBACON", 35.00),
    5: ("XTUDO", 40.00),
    6: ("SUCO NATURAL", 15.00),
    7: ("REFRIGERANTE", 10.00),
    8: ("CERVEJA", 14.00)
}
total = 0

while True:
    print('''
>>> LANCHES <<<

Escolha seu lanche :
[1] XBURGUER(S) R$ 20.00
[2] XSALADA(S): R$ 25.00
[3] XEEG(S): R$ 30.00
[4] XBACON(S): R$ 35.00
[5] XTUDO(S): R$ 40.00
[0] FINALIZAR PEDIDO''')

    opção = int(input('DIGITE O NÚMERO DE SUA OPÇÃO: '))

    if opção == 0:
        break
    if opção in cardapio:
        qnt = int(input('QUANTIDADE:'))
        produto, preço = cardapio[opção]
        subtotal = preço * qnt
        total += subtotal
        print(f'>>> {qnt}x {produto} adicionado(s). Subtotal: R$ {subtotal:.2f}<<<')
    else:
        print("Opção inválida, tente novamente!")
    print('''    
    
\n=== BEBIDAS ===
[6] SUCO(S) NATURAL R$ 15.00
[7] REFRIGERANTE(S) R$ 10.00
[8] CERVEJA(S) R$ 14.00
[0] FINALIZAR PEDIDO''')

    opção = int(input('DIGITE O NÚMERO DE SUA OPÇÃO: '))

    if opção == 0:
        break
    if opção in cardapio:
        qnt = int(input('QUANTIDADE:'))
        produto, preço = cardapio[opção]
        subtotal = preço * qnt

        total += subtotal
        print(f'>>> {qnt}x {produto} adicionado(s). Subtotal: R$ {subtotal:.2f}<<<')
    else:
        print("Opção inválida, tente novamente!")

print(f"\n=== RESUMO DO PEDIDO ===")
print(f"Subtotal: R$ {total:.2f}")

taxa_servico = total * 0.10
total_com_taxa = total + taxa_servico

cupons = {
    "DESC10": 0.10,  # 10% de desconto
    "DESC20": 0.20,  # 20% de desconto
    "FRETEGRATIS": 0.05  # exemplo: 5% desconto
}

cupom = input("Digite seu cupom de desconto (ou pressione ENTER para pular): ").upper()

if cupom in cupons:
    desconto = total_com_taxa * cupons[cupom]
    total -= desconto
    print(f"Cupom '{cupom}' aplicado! Você ganhou {cupons[cupom]*100:.0f}% de desconto (-R$ {desconto:.2f})")
else:
    print("Cupom inválido ou não informado.")


print(f"Taxa de serviço (10%): R$ {taxa_servico:.2f}")
print(f"TOTAL A PAGAR: R$ {total_com_taxa:.2f}")

pagamento = int(input('''Como deseja pagar?
[1] dinheiro/pix
[2] cartão débito/crédito
OPÇÃO : '''))
if pagamento == 1:
    valor_pago = (input("Informe o valor que você vai pagar: R$ "))
    valor_pago = valor_pago.replace(",", ".")  # substitui vírgula por ponto
    valor_pago = float(valor_pago)

    if valor_pago >= total:
       troco = valor_pago - total_com_taxa
       time.sleep(1)
       print(f'Troco: R$ {troco:.2f}')
       time.sleep(1)
       print('>>>OBRIGADO PELA PREFERÊNCIA <<<')
    else:
        falta = total - valor_pago
        print(f"Valor insuficiente! Ainda faltam R$ {falta:.2f}")
    
if pagamento == 2:
    cre_deb = int(input('[1] Débito\n[2] Crédito\nOpção: '))
    if cre_deb == 1 or cre_deb == 2:
        print('Insira ou aproxime seu cartão...')
        time.sleep(2)
        print(">>> Pagamento aprovado! Obrigado pela preferência! <<<")
    else:
        print('OPÇÃO INVÁLIDA! tente novamente!')
