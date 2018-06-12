'''

PYTHON

Cores no terminal - python


EXEMPLO DE COMO USAR

print("\033[4;34;40mOla, Mundo\n033[m")

Style:

0: nenhum
1: negrito
4: sublinhado
7: invertido

text:

30: branco
31: vermelho
32: verde
33: amarelo
34: azul
35: rocho
36: verde claro
37: cinza

back:

40: branco
41: vermelho
42: verde
43: amarelo
44: azul
45: rocho
46: verde claro
47: cinza

'''

# Escrevendo Ola mundo (Sem nenhuma fonte, texto branco, fundo vermelho)

print("\033[0;30;41;m Ola mundo \033[m")

# Escrevendo Ola mundo (fonte negrito, texto verde, fundo branco)

print("\033[1;32;40;m Ola mundo \033[m")

# Escrevendo Ola mundo (fonte sublinhado, texto rocho, fundo amarelo)


print("\033[4;35;43;m Ola mundo \033[m")

# Escrevendo Ola mundo (fonte invertido, texto preto, fundo branco)


print("\033[7;30;m Ola mundo \033[m")

# Imprimindo informações com cores diferentes

a = 6
b = 3

print("Os valores são  \033[0;34;0;m{} \033[m e \033[0;31;0;m{}".format(a, b))
