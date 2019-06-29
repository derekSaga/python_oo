import veiculo


class Carro(veiculo.Veiculo):
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia):
        super().__init__(cor, tipo_combustivel, potencia)
        """ESSA CLASSE É UTILIZADA PARA INSTANCIAR NOVOS CARROS"""
        self.qtd_portas = qtd_portas

    def __del__(self):
        print('CARRO REMOVIDO DA MEMÓRIA')
