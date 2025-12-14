from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentarNome(self):
        print(f"Eu sou o(a) {self.nome}!")

    @abstractmethod
    def fazerSom(self):
        pass

    @abstractmethod
    def mover(self):
        pass
        
    
class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        print("Som: ROAARRR!")

    def mover(self):
        print("Movimento: Correndo rapidamente sobre quatro patas.")


class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        print("Som: FUUUUUUUM! (Tromba)!")

    def mover(self):
        print("Movimento: Caminhando lentamente")


class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        print("Som: Tsssssss!")

    def mover(self):
        print("Movimento: Rastejando pelo chão.")

def apresentar(animal: Animal):
    print("-" * 30)
    print(f"Classe: {type(animal).__name__}")

    animal.apresentarNome()
    animal.fazerSom()
    animal.mover


if __name__ == "__main__":
    simba = Leao("Simba")
    dumbo = Elefante("Dumbo")
    nagini = Cobra("Nagini")

    zoologico = [simba, dumbo, nagini]

    print("--- VISITANDO O ZOOLÓGICO ---")
    
    for bicho in zoologico:
        apresentar(bicho)