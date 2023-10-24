velocidade = int(input('Quantos KM você estava?: '))
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
    print('Não levou multa!')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou uma multa leve!')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou uma multa grave!')
elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravíssima!')