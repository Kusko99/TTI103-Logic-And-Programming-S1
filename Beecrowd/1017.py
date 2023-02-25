tempo_viagem = int(input())
velocidade_media = int(input())
consumo = 12
distancia = velocidade_media/tempo_viagem
litros = consumo*distancia
print(f"{litros:.3f}")