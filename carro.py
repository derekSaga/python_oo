class Carro():
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia):
        """
        ESSA CLASSE É UTILIZADA PARA INSTANCIAR NOVOS CARROS
        :type acelerar: int
        :type qtd_combustivel: float
        :type cor: object
        :type qtd_portas: object
        :type tipo_combustivel: object
        """
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        print('CARRO REMOVIDO DA MEMÓRIA')

    def abastecer(self, qtd_combustivel=0):
        """
        :type qtd_combustivel: float
        RECEBE COMO PARAMETRO A QUANTIDADE DE COMBUSTÍVEL E INCREMENTA O ATRIBUTO qtd_combustivel DO OBJETO CARRO
        """
        self.qtd_combustivel = + qtd_combustivel

    def ligado(self):
        if self.is_ligado:
            print("O carro já está ligado !")
        else:
            self.is_ligado = True
            print('O carro foi ligado !')

    def desligado(self):
        if self.is_ligado == False:
            print('O carro já está desligado !')
        else:
            self.is_ligado = False
            print('O carro foi desligado !')

    def acelerar(self, velocidade=10):
        """

        :param velocidade: int
        :return: None
        """
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print('O carro precisa estar ligado para ser acelerado !')