from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.__id = id
        self.__tipo = tipo
        self.__horaEntrada = 0

    def setEntrada(self, horaEntrada: int):
        self.__horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self.__horaEntrada
    
    def getTipo(self) -> str:
        return self.__tipo
    
    def getId(self) -> str:
        return self.__id
    
    @abstractmethod
    def calcularValor(self, horaSaida: int) -> float:
        pass

    def __str__(self):
        return f"{self.__tipo:_>10} : {self.__id:_>10} : {self.__horaEntrada}"
        

class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")

    def calcularValor(self, horaSaida: int) -> float:
        return 3.00

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        return tempo / 20.0
    
class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        valor = tempo / 10.0
        if valor < 5.00:
            return 5.00
        return valor


class Estacionamento:
    def __init__(self):
        self.__veiculos = []
        self.__horaAtual = 0

    def __procurarVeiculo(self, id: str) -> int:
        for i, v in enumerate(self.__veiculos):
            if v.getId() == id:
                return i
        return -1
    
    def estacionar(self, veiculo: Veiculo):
        if self.__procurarVeiculo(veiculo.getId()) != -1:
            print(f"fail: veiculo {veiculo.getId()} ja esta no estacionamento")
            return
        
        veiculo.setEntrada(self.__horaAtual)
        self.__veiculos.append(veiculo)

    def passarTempo(self, tempo: int):
        self.__horaAtual += tempo
    
    def sair(self, id: str):
        pos = self.__procurarVeiculo(id)
        if pos == -1:
            print(f"fail: veiculo {id} nao esta no estacionamento")
            return
        
        veiculo = self.__veiculos[pos]
        valor = veiculo.calcularValor(self.__horaAtual)

        print(f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} saiu {self.__horaAtual}. Pagar R$ {valor:.2f}")
        del self.__veiculos[pos]

    def __str__(self):
        output = ""
        for v in self.__veiculos:
            output += str(v) + "\n"

        output += f"Hora atual: {self.__horaAtual}"
        return output
        

def main():
    estacionamento = Estacionamento()

    while True:
        try:
            line = input()
        except EOFError:
            break

        print(f"${line}")
        args = line.split()

        if len(args) == 0:
            continue

        cmd = args[0]

        if cmd == "end":
            break

        elif cmd == "show":
            print(estacionamento)

        elif cmd == "tempo":
            tempo = int(args[1])
            estacionamento.passarTempo(tempo)

        elif cmd == "estacionar":
            tipo = args[1]
            placa = args[2]

            veiculo = None
            if tipo == "bike":
                veiculo = Bike(placa)

            elif tipo == "moto":
                veiculo = Moto(placa)

            elif tipo == "carro":
                veiculo = Carro(placa)

            if veiculo:
                estacionamento.estacionar(veiculo)

        elif cmd == "sair" or cmd == "pagar":
            placa = args[1]
            estacionamento.sair(placa)


if __name__ == "__main__":
    main()