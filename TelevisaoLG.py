class Televisao:
  def __init__(self):
    self.marca = "LG"
    self.volume = 0
    
  def aumentar_volume(self):
    if self.volume < 10:
      self.volume = self.volume + 1
    
  def diminuir_volume(self):
    if self.volume > 0:
      self.volume = self.volume - 1
    
tv = Televisao()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
