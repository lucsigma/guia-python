
import streamlit as st

# Dicionário com explicações sobre Python e exemplos de código
python_guia = {
    "dicionário": {
        "explicação": "Um dicionário em Python é uma coleção de pares chave-valor. Exemplo:\nmeu_dict = {'nome': 'João', 'idade': 25}",
        "exemplo": """# Exemplo de dicionário
meu_dict = {'nome': 'João', 'idade': 25}
print(meu_dict['nome'])  # Saída: João"""
    },
    "lista": {
        "explicação": "Uma lista é uma coleção ordenada e mutável de elementos. Exemplo:\nminha_lista = [1, 2, 3, 4]",
        "exemplo": """# Exemplo de lista
minha_lista = [1, 2, 3, 4]
minha_lista.append(5)  # Adiciona o número 5 à lista
print(minha_lista)  # Saída: [1, 2, 3, 4, 5]"""
    },
    "tupla": {
        "explicação": "Uma tupla é uma coleção ordenada e imutável. Exemplo:\nminha_tupla = (1, 2, 3)",
        "exemplo": """# Exemplo de tupla
minha_tupla = (1, 2, 3)
print(minha_tupla[0])  # Saída: 1"""
    },
    "if": {
        "explicação": "A estrutura if é usada para fazer decisões em Python. Exemplo:\nif x > 10:\n    print('Maior que 10')",
        "exemplo": """# Exemplo de if
x = 15
if x > 10:
    print('Maior que 10')  # Saída: Maior que 10"""
    },
    "funções": {
        "explicação": "Funções em Python permitem reutilizar código. Exemplo:\ndef saudacao(nome):\n    return f'Olá, {nome}!'\nprint(saudacao('Lucio'))",
        "exemplo": """# Exemplo de função
def saudacao(nome):
    return f'Olá, {nome}!'
print(saudacao('caio'))  # Saída: Olá, caio!"""
    },
    "variáveis": {
        "explicação": "Variáveis são usadas para armazenar valores. Exemplo:\nidade = 25",
        "exemplo": """# Exemplo de variável
idade = 25
print(idade)  # Saída: 25"""
    },
    "tipos de dados": {
        "explicação": "Em Python, os principais tipos de dados são: inteiro (int), flutuante (float), string (str), e booleano (bool). Exemplo:\nnumero = 10 # int\naltura = 1.75 # float",
        "exemplo": """# Exemplo de tipos de dados
numero = 10  # int
altura = 1.75  # float
nome = 'João'  # str
verdadeiro = True  # bool
print(numero, altura, nome, verdadeiro)  # Saída: 10 1.75 João True"""
    },
    "for": {
        "explicação": "O loop for é usado para iterar sobre uma sequência (como uma lista ou tupla). Exemplo:\nfor i in range(5):\n    print(i)",
        "exemplo": """# Exemplo de loop for
for i in range(5):
    print(i)  # Saída: 0 1 2 3 4"""
    },
    "while": {
        "explicação": "O loop while é usado para repetir um bloco de código enquanto uma condição for verdadeira. Exemplo:\nwhile x < 10:\n    x += 1",
        "exemplo": """# Exemplo de loop while
x = 0
while x < 5:
    print(x)
    x += 1  # Saída: 0 1 2 3 4"""
    },
    "input": {
        "explicação": "A função input() é usada para capturar a entrada do usuário. Exemplo:\nnome = input('Qual seu nome? ')",
        "exemplo": """# Exemplo de input
nome = input('Qual seu nome? ')
print(f'Olá, {nome}!')"""
    },
    "comentários": {
        "explicação": "Comentários são usados para explicar o código e são ignorados na execução. Exemplo:\n# Este é um comentário",
        "exemplo": """# Exemplo de comentário
# Este código imprime uma mensagem de saudação
print('Olá, Mundo!')  # Este comentário está ao lado do código"""
    },
    "exemplo de código": {
        "explicação": "Exemplo completo utilizando variáveis, listas, loops e funções.",
        "exemplo": """# Exemplo de código com variáveis, listas, loops e funções

# Função para calcular a média de uma lista de números
def calcular_media(lista):
    soma = sum(lista)  # Soma todos os elementos da lista
    media = soma / len(lista)  # Divide a soma pelo número de elementos
    return media

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Exibindo a média
print("A média dos números é:", calcular_media(numeros))

# Usando loop for para exibir cada número da lista
for numero in numeros:
    print(f"Número: {numero}")"""
    },
    "classes": {
        "explicação": "Classes são usadas para criar objetos com atributos e métodos. Exemplo:\nclass Carro:\n    def _init_(self, marca):\n        self.marca = marca\ncarro = Carro('Fusca')",
        "exemplo": """# Exemplo de classe
class Carro:
    def _init_(self, marca):
        self.marca = marca

carro = Carro('Fusca')
print(carro.marca)  # Saída: Fusca"""
    },
    "módulos": {
        "explicação": "Módulos são arquivos que contêm código Python. Você pode importar módulos para reutilizar código. Exemplo:\nimport math\nprint(math.sqrt(16))",
        "exemplo": """# Exemplo de módulo
import math
print(math.sqrt(16))  # Saída: 4.0"""
    },
    "exceções": {
        "explicação": "O tratamento de exceções é usado para lidar com erros em tempo de execução. Exemplo:\ntry:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Erro de divisão por zero')",
        "exemplo": """# Exemplo de exceção
try:
    x = 1 / 0
except ZeroDivisionError:
    print('Erro de divisão por zero')  # Saída: Erro de divisão por zero"""
    }
}

# Interface com Streamlit
def app():
    st.title("Guia Python")

    st.write("Escolha um tópico para aprender mais:")

    topic = st.selectbox("Selecione um tópico:", list(python_guia.keys()))

    if topic:
        st.subheader(f"Explicação de {topic}:")
        st.write(python_guia[topic]["explicação"])

        st.subheader("Exemplo de código:")
        st.code(python_guia[topic]["exemplo"])

if "main":
    app()