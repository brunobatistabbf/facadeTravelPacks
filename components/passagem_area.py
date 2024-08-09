class PassagemArea:
    def reserva_assento(self, classe_voo: str, assento: str) -> float:
        precos = {
            "economica": 500,
            "executiva": 500 * 2.5,
            "primeira_classe": 500 * 4
        }

        print(f"Assento: {assento} na classe {classe_voo} reservado")
        return precos[classe_voo]

