class Hotel:
    def reservar_quarto(self, quarto: str, pessoas: int) -> float:
        precos = {
            "simples": 200.00,
            "executivo": 200.00 * 1.5,
            "presidencial": 200.00 * 4.5
        }

        preco_total = precos[quarto] * pessoas
        print(f"Quarto {quarto} reservado para {pessoas} pessoas")
        return preco_total