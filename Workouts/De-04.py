import random 

numero = int(input('Digita um numero de 0 a 5 que estou pensando agora.  R: '))
sorte = random.randint(0, 5)

if numero == sorte:
    print('UAU!! Você tem muita sorte. Eu tava pensando no {} mesmo!'.format(sorte))
else:
    print('hmm... Sinto muito. O que eu estava pensando era o {}!'.format(sorte))
