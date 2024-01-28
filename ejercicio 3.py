class Personaje:
  def __init__(self, velMov, velAtaque, ataque):
    self.velMov = velMov
    self.velAtaque = velAtaque
    self.ataque = ataque

  def __str__(self):
    return f"Habilidades: velMov={self.velMov} velAtaque={self.velAtaque} ataque={self.ataque}"
  
  def __add__(self, otro):

    def fusion(primero, segundo):
      return ((primero + segundo) / 2)**2

    return(Personaje(fusion(self.velMov, otro.velMov), fusion(self.velAtaque, otro.velAtaque), fusion(self.ataque, otro.ataque)))

primero = Personaje(1, 2, 3)
segundo = Personaje(3, 2, 1) 

print(primero + segundo)
  