# pegando a biblioteca random
import random

# INICIANDO AS VARIAVÉIS QUE SERÃO UTILIZADAS 
frase_alvo = "METHINKS IT IS LIKE A WEASEL"
frase_mais_parecida = ''
score = 0
maior_score = 0
frase_pai = []
geracao = 0

# GERANDO A PRIMEIRA FRASE QUE DARÁ ORIGEM À PRIMEIRA GERAÇÃO DE 100 FILHAS
for i in range(28):

    frase_pai.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ "))

# LOOP RESPONSÁVEL POR VERIFICAR A NECESSIDADE DE CONTINUAR A GERAÇÃO
# DE FRASES FILHAS
while maior_score < 28:

    geracao += 1

    # LOOP RESPONSÁVEL POR GERAR AS FRASES FILHAS
    for filha in range(100):

        frase_filha = ''

        # LOOP RESPONSÁVEL POR GERAR UMA ÚNICA FILHA
        # E FAZER A CONTAGEM DE PONTUAÇÃO(SCORE)
        for j in range(28):

            numero_aleatorio = random.randint(1, 100)

            if numero_aleatorio <= 5:

                frase_filha += random.choice(
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

            else:

                frase_filha += frase_pai[j]

            if frase_filha[j] == frase_alvo[j]:

                score += 1

        if maior_score < score:

            frase_mais_parecida = frase_filha
            maior_score = score

        if maior_score == 28:

            break

        print(frase_filha, end="; ")
        print("Geração:", end=" ")
        print(geracao, end="; ")
        print("Filha: " + str(filha), end="; ")
        print("Score: " + str(score))
        score = 0

    frase_pai = frase_mais_parecida
    
# EXPOSIÇÃO DO RESULTADO OBTIDO
print(frase_mais_parecida, end="; ")
print("Geração:", end=" ")
print(geracao, end="; ")
print("Filha: " + str(filha), end="; ")
print("Score: " + str(score))
