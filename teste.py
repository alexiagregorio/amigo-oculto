import random

# Lista com os nomes dos participantes do jogo
participantes = ["Alexia", "Sérgio", "Paula", "Antonio", "João", "Ariane"]

# Embaralha a lista para sortear os amigos secretos
amigos_secretos = random.sample(participantes, len(participantes))

# Garante que ninguém tire a si próprio e não haja amigos secretos repetidos
for i in range(len(amigos_secretos)):
    # Se o participante atual tirar a si próprio
    while amigos_secretos[i] == participantes[i]:
        # Embaralha a lista novamente
        amigos_secretos = random.sample(participantes, len(participantes))
        # E recomeça o loop
        i = 0

    # Se o amigo secreto já tiver sido sorteado
    if amigos_secretos.index(amigos_secretos[i]) < i:
        # Embaralha a lista novamente
        amigos_secretos = random.sample(participantes, len(participantes))
        # E recomeça o loop
        i = 0

# Imprime na tela o nome do amigo secreto de cada participante
for i in range(len(amigos_secretos)):
    print(participantes[i] + " tirou " + amigos_secretos[i] + " como amigo secreto!")