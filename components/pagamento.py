"""
0.90 10%
0.95 5%d
1.039 acrescimo
"""
class Pagamento:
    def processar_pagamento(self, valor: float, pagamento: str) -> float:
        descontos = {
            "pix":0.90,
            "boleto":0.95,
            "debito":1.00,
            "credito":1.00
        }
        acrescimos = {
            "credito": 1.039
        }

        if pagamento == 'credito':
            parcelas = int(input("Pagamento em quantas Parcelas?"))
            final = valor * descontos[pagamento]
            for i in range(parcelas - 1):
                final = final * acrescimos[pagamento]
        else:
            final = valor * descontos[pagamento]

        print(f"Pagamento realizado!!!")
        print(f"Via {pagamento}")
        return final