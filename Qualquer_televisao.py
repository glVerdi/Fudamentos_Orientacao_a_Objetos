class Qualquer_televisao:
  def __init__(self, marca):
    self.marca = marca
    self.volume = 0
    
  def aumentar_volume(self): # método fica dentro da classe
    if self.volume < 10:
      self.volume = self.volume + 1
    
  def diminuir_volume(self): # método fica dentro da classe
    if self.volume > 0:
      self.volume = self.volume - 1

  def visualizar_atributos(self): # método fica dentro da classe
    print("TV Marca:, self.marca)
    print("---Volume:", self.volume)
      
def ler_marca_tv(): # Função fica fora da classe 
    return input("Entre com a Marca da Tv: ")

tv_sala.Qualquer_televisao(ler_marca_tv())
tv_dormitorio.Qualquer_televisao(ler_marca_tv())

tv_sala..visualizar_atributos()
tv_dormitorio.aumentar_volume()
tv_dormitorio.aumentar_volume()
tv_dormitorio.aumentar_volume()
tv_dormitorio.diminuir_volume()
tv_dormitorio.visualizar_atributos()
