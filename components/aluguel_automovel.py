class AluguelCarro:
    def alugar_carro(self, carro: str) -> float:
        precos = {
            "economico": 150.00,
            "executivo": 150.00 * 2,
            "luxo": 150 * 4
        }

        print(f"Carro {carro} alugado")
        return precos[carro]