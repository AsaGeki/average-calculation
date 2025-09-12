class Aluno:
    def __init__(self, nome="", n1=0, n2=0):
        self.nome = nome
        self._n1 = n1
        self._n2 = n2
    
    def get_nome(self, nome):
        return nome
    def get_n1(self, n1):
        return n1
    def get_n2(self, n2):
        return n2
    def set_nome(self, nome):
        self.nome = nome
    def set_n1(self, nota):
        self._n1 = nota
    def set_n2(self, nota):
        self._n2 = nota

    def calc(self):
        return (self._n1 + self._n2) / 2

    def show(self):
        return f'nome: {self.nome}\nmédia: {self.calc():.2f}'
