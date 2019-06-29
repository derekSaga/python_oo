class Veiculo():

    def __init__(self, cor, tipo_combustivel, potencia):

        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def abastecer(self, qtd_combustivel=0):
        """
        :type qtd_combustivel: float
        RECEBE COMO PARAMETRO A QUANTIDADE DE COMBUSTÍVEL E INCREMENTA O ATRIBUTO qtd_combustivel DO OBJETO VEICULO
        """
        self.qtd_combustivel = + qtd_combustivel

    def ligado(self):
        if self.is_ligado:
            print("O veiculo já está ligado !")
        else:
            self.is_ligado = True
            print('O veiculo foi ligado !')

    def desligado(self):
        if self.is_ligado == False:
            print('O veiculo já está desligado !')
        else:
            self.is_ligado = False
            print('O veiculo foi desligado !')

    def acelerar(self, velocidade=10):
        """
        :param velocidade: int
        :return: None
        """
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print('O veiculo precisa estar ligado para ser acelerado !')