from facade.facade import Facade

if __name__ == '__main__':
    print("_______________CVC_TURISMO_SYSTEM________________")
    print("PERSONALIZE SEU PACOTE DE VIAJENS")
    nome_resp = input("Insira seu Nome:")
    cpf_resp = input("Insira seu CPF")
    print("Escolha a classe do VOO:")
    print("economica - executiva - primeira classe")
    classe_voo_resp = input("Insira a Classe do VOO:")
    print()
    assento_resp = input("Escolha o assento:")
    print()
    print("Escolha o tipo de Quarto\nsimples - executivo - presidencial")
    tipo_quarto_resp = input("Escolha o tipo de Quarto:")
    pessoas_resp = int(input("Quantas pessoas vão se hospedar?"))
    tipo_carro_resp = input("Escolha o tipo de Carro:\neconomico - executivo - luxo\n")
    tipo_pagamento_resp = input("Escolha o tipo de Pagamento:\n pix - boleto - debito - credito\n")

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