class Abajur_com_intensidade:
  def __ini__ (self):
    self.__lampada = False # False = Apagado      True = Acesa
    self.__intensidade = 0 # Terá os valores: 0, 1, 2 ou 3

  def __liga_desliga_lampada(self):
    if self.__intensidade == 0:
      self.____lampada = False
    else:
      self.__lampada = True
  
  def __controla_intensidade(self):
    self.__intensidade = __intensidade + 1
    if self.__intensidade == 4:
      self.__intensidade = 0

  def tocar_botao(self):
    if input("Tocar Botão [Enter]") == "":
      return True
    return False
    
  def mostrar_status(self):
    print("Status")
    print(" -", self.__lampada)
    print(" -", self.__intensidade)

  def acoes(self):
    self.__controla_intensidade()
    self.__liga_desliga_lampada()
    
abajur = Abajur_com_intensidade()
while True:
  if abajur.tocar_botao():
    abajur.acoes()

  abajur.mostrar_status()
