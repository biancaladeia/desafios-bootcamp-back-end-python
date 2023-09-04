# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

# Definir a classe carro
class Carro:

  # Inicializar os atributos do carro
  def __init__(self, cor, modelo):
    self.ligado = False # O carro começa desligado
    self.cor = cor # Atribuir a cor do carro
    self.modelo = modelo # Atribuir o modelo do carro
    self.velocidade = 0 # O carro começa parado

  # Definir o método para ligar o carro
  def liga(self):
    if self.ligado: # Se o carro já está ligado
      print(f"O {self.modelo} {self.cor} já está ligado.")
    else: # Se o carro está desligado
      self.ligado = True # Mudar o estado do carro para ligado
      print(f"O {self.modelo} {self.cor} foi ligado.")

  # Definir o método para desligar o carro
  def desliga(self):
    if self.ligado: # Se o carro está ligado
      self.ligado = False # Mudar o estado do carro para desligado
      self.velocidade = 0 # Zerar a velocidade do carro
      print(f"O {self.modelo} {self.cor} foi desligado.")
    else: # Se o carro já está desligado
      print(f"O {self.modelo} {self.cor} já está desligado.")

  # Definir o método para acelerar o carro
  def acelera(self, incremento):
    if self.ligado: # Se o carro está ligado
      self.velocidade += incremento # Aumentar a velocidade do carro pelo incremento
      print(f"O {self.modelo} {self.cor} acelerou para {self.velocidade} km/h.")
    else: # Se o carro está desligado
      print(f"O {self.modelo} {self.cor} está desligado e não pode acelerar.")

  # Definir o método para desacelerar o carro
  def desacelera(self, decremento):
    if self.ligado: # Se o carro está ligado
      if self.velocidade > 0: # Se o carro tem velocidade positiva
        self.velocidade -= decremento # Diminuir a velocidade do carro pelo decremento
        if self.velocidade < 0: # Se a velocidade ficou negativa
          self.velocidade = 0 # Ajustar a velocidade para zero
        print(f"O {self.modelo} {self.cor} desacelerou para {self.velocidade} km/h.")
      else: # Se o carro já está parado
        print(f"O {self.modelo} {self.cor} já está parado.")
    else: # Se o carro está desligado
      print(f"O {self.modelo} {self.cor} está desligado e não pode desacelerar.")


# Crie uma instância da classe carro.
meu_carro = Carro("prata", "Fit")


# Faça o carro "andar" utilizando os métodos da sua classe.

# Ligar o carro
meu_carro.liga()
# Acelerar o carro em 10 km/h
meu_carro.acelera(10)
# Acelerar o carro em mais 20 km/h
meu_carro.acelera(20)


# Faça o carro "parar" utilizando os métodos da sua classe.

# Desacelerar o carro em 30 km/h
meu_carro.desacelera(30)
# Desligar o carro
meu_carro.desliga()


