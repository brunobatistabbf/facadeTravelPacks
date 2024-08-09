from components.passagem_area import PassagemArea
from components.reserva_hotel import Hotel
from components.aluguel_automovel import AluguelCarro
from components.pagamento import Pagamento
class Facade:
    def __init__(self):
        self.passagem = PassagemArea()
        self.hotel = Hotel()
        self.carro = AluguelCarro()
        self.pagamento = Pagamento()

    def comprar_pacote(self, nome: str, cpf: str, classe_voo: str, assento: str, quarto: str, pessoas: int, carro: str, pagamento: str):
        print(f"\n Pacote de Viagem para {nome}")
        preco_passagem = self.passagem.reserva_assento(classe_voo, assento)
        preco_hotel = self.hotel.reservar_quarto(quarto, pessoas)
        preco_carro = self.carro.alugar_carro(carro)

        valor = preco_passagem + preco_hotel + preco_carro
        valor_final = self.pagamento.processar_pagamento(valor, pagamento)

        print(f"\nDetalhes da sua Compra:")
        print(f"Passagem: {classe_voo}, Assento: {assento}")
        print(f"Hotel: {quarto} para {pessoas} pessoas")
        print(f"Carro: {carro}")
        print(f"Valor Total(com descontos/acrescimos): R${valor_final:.2f}")
