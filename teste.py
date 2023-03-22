import random

# Lista com os nomes dos participantes do jogo
participantes = ["Alexia", "João", "Maria", "Pedro", "Lucas", "Julia"]

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
    
#Neste exemplo, o módulo random é usado para embaralhar a lista de participantes e sortear os amigos secretos.

#Após embaralhar a lista de amigos secretos, um loop for é usado para garantir que ninguém tire a si próprio e que não haja amigos secretos repetidos.

#Para verificar se um participante tirou a si próprio, o loop verifica se o nome do amigo secreto correspondente é igual ao nome do participante na posição atual do loop. Se for esse o caso, o loop inteiro é reiniciado a partir do início.

#Para verificar se um amigo secreto já foi sorteado anteriormente, o loop usa o método index para procurar o índice do amigo secreto atual na lista de amigos secretos. Se esse índice for menor que a posição atual do loop, significa que o amigo secreto já foi sorteado anteriormente e o loop inteiro é reiniciado.

#Finalmente, outro loop for é usado para imprimir o nome do amigo secreto correspondente a cada participante na tela.