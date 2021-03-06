# -*- coding: utf-8 -*-
"""ia-202201-jogo-da-velha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t1mNPqdxMlbRWa_vslCfE8wOOd4vCT6f
"""

# Função para impressão do tabuleiro
def imprime_tabuleiro(t):
  s = '''
  {} | {} | {}
--------------
  {} | {} | {}
--------------
  {} | {} | {}'''

  t2 = [i if i else ' ' for i in t]
  
  print (s.format(*t2))

# Função para impressão das casas disponíveis
def imprime_casas_disponiveis(t):
  s = '''
  {} | {} | {}
--------------
  {} | {} | {}
--------------
  {} | {} | {}'''

  t2 = [i if not t[i] else ' ' for i in range(len(t))]
  
  print (s.format(*t2))

# Retorna as casas disponíveis
def casas_disponiveis(t):
  return [i for i in range(len(t)) if not t[i]]

# Verifica se há um vencedor
def verifica_vencedor(t, jogadas_vencedoras):
  for j in jogadas_vencedoras:
    if (t[j[0]] == t[j[1]]) and (t[j[0]] == t[j[2]]) and t[j[0]]:
      return t[j[0]]

  return None

# Inicializações
import numpy as np
from time import sleep
from google.colab import output

jogadas_vencedoras = [
  # Linhas
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  
  # Colunas
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  
  # Diagonais
  [0, 4, 8],
  [2, 4, 6]
]

# Jogada player (humano)
def joga_humano(tabuleiro, vencedoras, disponiveis, simbolo):
  jogada = int(input('Informe a casa desejada:'))
  while jogada not in disponiveis:
    print ('Casa inválida!')
    jogada = int(input('Informe a casa desejada:'))
  return jogada

# Jogada CPU (primeira livre)
def joga_primeira_livre(tabuleiro, vencedoras, disponiveis, simbolo):
  return disponiveis[0]

# Jogada CPU (última livre)
def joga_ultima_livre(tabuleiro, vencedoras, disponiveis, simbolo):
  return disponiveis[-1]

# Jogada Aleatória
def joga_aleatoria(tabuleiro, vencedoras, disponiveis, simbolo):
  return np.random.choice(disponiveis)

# Mistura os algoritmos
def joga_aleatoria_2(tabuleiro, vencedoras, disponiveis, simbolo):
  funcoes = [joga_primeira_livre, joga_ultima_livre, joga_aleatoria]
  funcao = np.random.choice(funcoes)
  return funcao(tabuleiro, vencedoras, disponiveis)

# Jogada defensiva
def joga_defensiva(tabuleiro, vencedoras, disponiveis, simbolo):
  # TODO
  pass

# Jogo
def executa_jogo(jogadas_vencedoras):
  jogador_vez = 'X'
  tabuleiro = [None] * 9

  for rodada in range(9):
    print ('\nTabuleiro:\n')
    imprime_tabuleiro(tabuleiro)

    print ('\nCasas disponíveis:\n')
    imprime_casas_disponiveis(tabuleiro)

    disponiveis = casas_disponiveis(tabuleiro)
    
    if jogador_vez == 'X':
      jogada = joga_aleatoria_2(tabuleiro, jogadas_vencedoras, disponiveis)
    else:
      jogada = joga_aleatoria(tabuleiro, jogadas_vencedoras, disponiveis)
    
    tabuleiro[jogada] = jogador_vez

    sleep(2)

    vencedor = verifica_vencedor(tabuleiro, jogadas_vencedoras)
    if vencedor:
      output.clear()
      imprime_tabuleiro(tabuleiro)
      print ('Parabéns ' + vencedor + '! Você venceu!')
      return

    jogador_vez = 'X' if jogador_vez == 'O' else 'O'

    output.clear()

  imprime_tabuleiro(tabuleiro)
  print ('Empate!')

# Inicia o jogo
executa_jogo(jogadas_vencedoras)

import numpy as np

# print (np.random.randint(3))

l = ['a', 'b', 'c']
print (np.random.choice(l))