import numpy as np

print('Questão 1\n')
# Questão 1
# a
x = np.array(
    [-1.3, np.sqrt(3), (1+2+3)*4/5 ]
)
print('a) x = {}'.format(x))

# b
newElement = np.abs(x[1])
x = np.insert(x, 3, newElement)
print('b) x = {}'.format(x))

# c
y = np.array([
    [1, 2, 3, 4]
])
print('c) y = {}'.format(y))

# d
# i. x+y
print('d)\ti. x + y = {}'.format(x + y))

# ii. x-y
print('\tii. x - y = {}'.format(x - y))

# iii. y’ (transposto)
yt = np.transpose(y)
print('\tiii. y’ = {}'.format(yt))

# iv. x*y (elemento a elemento)
print('\tiv. x * y = {}'.format(x * y))

# v. x*y’ (elemento a elemento)
v = x * yt
print('\tv. x * y’ = {}'.format(v))

# vi. x.*y (np.dot)
print('\tvi. x .* y = {}'.format(np.dot(x, y[0])))

# vii. x./y (divisão elemento por elemento)
print('\tvii. x ./ y = {}'.format(np.divide(x, y)))

# viii. x.^y (exponencial elemento a elemento)
print('\tviii. x .^ y = {}'.format(np.power(x, y)))

# ix. z = [x y] (concatenação de matrizes)
z = np.concatenate(
    (x, y[0])
)
print('\tix. z = [x y] = {}'.format(z))

# ----------------------------------------------------------
print('\nQuestão 2\n')
# Questão 2
# a
a = np.arange(0, 10, 2)
print('a) {}'.format(a))

# b
b = np.arange(1, 5)
print('b) {}'.format(b))

# c
c = v.shape
print('c) {}'.format(c))

# d
v2 = np.linspace(0, 10, 6, dtype=int)
print('d) v2 = {}'.format(v2))

# ----------------------------------------------------------
print('\nQuestão 3\n')
# Questão 3
# a
v3 = np.random.rand(1, 1000)
print('a) {}'.format(v3))

# b
mean = np.mean(v3)
std = np.std(v3)
print('b) Média: {}\tDesvio Padrão: {}'.format(mean, std))

# c (Crie um vetor 0<x<2*pi ??)
x = np.random.rand(1, 100) * np.pi
print('c) {}'.format(x))

# d
import matplotlib.pyplot as plt
plt.plot(np.arange(0,100), np.sin(x[0]))
plt.title('Questão 3, letra d')
plt.ylabel('sin(x)')
plt.show()

# e
m = np.linspace(1, 1, 1000, dtype=int)
print('e) m = {}'.format(m))

# f
print('f) length of m = {}'.format(m.size))

# ----------------------------------------------------------
# Questão 4

# Exemplo de arquivo tipo script
# script1: desenha o grafico f(x) = sin(x)*exp(x), -2*pi < x < 2*pi
x = np.arange(-2*np.pi, 2*np.pi, 0.1) # cria o array de valores do eixo x
y = np.sin(x) * np.exp(x) # cria o array de valores do eixo y
plt.plot(x, y) # traça o gráfico de x, y
plt.title('Questão 4\nGráfico exemplo') # seta um título para o gráfico
plt.show() # mostra o gráfico

# ----------------------------------------------------------
# Questão 5

def func1(inicio, incremento, fim):
    x = np.arange(inicio, fim, incremento)
    y = np.sin(x) * np.exp(x)
    plt.plot(x, y)
    plt.title('Questão 5\nGráfico exemplo - II')
    plt.show()

func1(0, 2, 100)

# ----------------------------------------------------------
# Questão 6

