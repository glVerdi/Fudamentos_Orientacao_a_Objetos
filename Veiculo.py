class Veiculo:
  def __init__(self, marca, modelo):
    self.__marca = marca
    self.__modelo = model
  def acelerar(self):
    print(f"""Acelerando: {self.marca}""")
    def frear(self):
    print(f"""Freando: {self.marca}""")
class Carro(Veiculo):
  def acionar_limpador_parabrisa(self):
    print(f"O {self.modelo} {self.marca} com limpador de parabrisa acionado.")
class Moto(Veiculo):
  def empinar(self):
    print(f"A moto {self.marca} {self.modelo} está empinando.")
