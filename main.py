from facade.facade import Facade

if __name__ == '__main__':
    print("_______________CVC_TURISMO_SYSTEM________________")
    print("PERSONALIZE SEU PACOTE DE VIAJENS")
    nome_resp = input("Insira seu Nome:")
    cpf_resp = input("Insira seu CPF")

    while True:
        print("Escolha a classe do VOO:")
        print("economica - executiva - primeira classe")
        classe_voo_resp = input("Insira a Classe do VOO:")

        if classe_voo_resp not in ['economica', 'executiva', 'primeira classse']:
            print("Classe de voo inválida! Insira uma das seguintes opções: economica, executiva, primeira classe")
            continue

        assento_resp = input("Escolha o assento:")
        if len(assento_resp) < 2 or not assento_resp[:-1].isdigit() or assento_resp[-1] not in 'ABCDEF':
            print("Invalido! Escolha o assento no formato, '1A'")
            continue

        fileira = int(assento_resp[:-1])
        if fileira < 1 or fileira > 32:
            print("Número de fileira deve estar entre 1 e 32")
            continue

        print("Escolha o tipo de Quarto\nsimples - executivo - presidencial")
        tipo_quarto_resp = input("Escolha o tipo de Quarto:").strip().lower()
        if tipo_quarto_resp not in ['simples', 'executivo', 'presidencial']:
            print("Insira uma das seguintes opções: 'simples', 'executivo', 'presidencial'")
            continue

        try:
            pessoas_resp = int(input("Quantas pessoas vão se hospedar?").strip())
            if pessoas_resp < 1:
                print("Número de pessoas inválido! Deve ser pelo menos 1.")
                continue
        except ValueError:
            print("Entrada inválida! Insira um número válido de pessoas.")
            continue

        tipo_carro_resp = input("Escolha o tipo de Carro:\neconomico - executivo - luxo\n")
        if tipo_carro_resp not in ['economico',  'executivo'  'luxo']:
            print("Tipo de Carro Invalidp! Insira uma das opções: economico - executivo - luxo")
            continue

        tipo_pagamento_resp = input("Escolha o tipo de Pagamento:\n pix - boleto - debito - credito\n")
        if tipo_pagamento_resp not in ['pix', 'boleto', 'debito', 'credito']:
            print("Forma de Pagamento Invalida! Insira uma das opções: pix, boleto, debito, credito")
            continue

        break


    pacote = Facade()
    pacote.comprar_pacote(
        nome = nome_resp,
        cpf = cpf_resp,
        classe_voo = classe_voo_resp,
        assento = assento_resp,
        quarto = tipo_quarto_resp,
        pessoas = pessoas_resp,
        carro = tipo_carro_resp,
        pagamento = tipo_pagamento_resp
    )