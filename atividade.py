class Pessoa():
    def _init_(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.parado = True
        self.comendo = False
        self.andando = False
        self.falando = False

    def parar(self):
        if self.parado == False:
            self.parado = True
            self.comendo = False
            self.andando = False
            self.falando = False
            print(self.nome, "está parado")
        else:
            print(self.nome, "já está parado")

    def comer(self):
        if self.comendo == False:
            self.parado = False
            self.comendo = True
            self.andando = False
            self.falando = False
            print(self.nome, "está comendo")
        else:
            print(self.nome, "já está comendo")

    def andar(self):
        if self.andando == False:
            self.parado = False
            self.comendo = False
            self.andando = True
            self.falando = False
            print(self.nome, "está andando")
        else:
            print(self.nome, "já está andando")

    def falar(self):
        if self.falando == False:
            self.parado = False
            self.comendo = False
            self.andando = False
            self.falando = True
            print(self.nome, "está falando")
        else:
            print(self.nome, "já está falando")
