Tabuleiro = ['_','_','_','_','_','_','_','_','_']

def jogo():
  rodada = 0
  simbx = 'X'
  simbo = 'O'
  while True:
    if rodada%2 == 0:
      simb = simbx
    else:
      simb = simbo
    print(f"\nJogador {rodada%2+1} - {simb}")
    print()
    showtab()
    print()
    print('Escolha a posição de 1 a 9')
    while True:
      try:
        posição = int(input('Posição da jogada: '))
        print()
        if 0 < posição < 10:
          break
        else:
          print('Por favor digite uma valor entre 1 e 9')
      except Exception as e:
        print(f'Problema: {e}')

    if Tabuleiro[posição-1] == '_':
      if rodada%2 == 0:
        Tabuleiro[posição-1] = simbx
      else:
        Tabuleiro[posição-1] = simbo
    else:
      print("Posição Invalida")
      rodada -=1
    
    if Vencedor():
      showtab()
      print('=-'*15)
      print(f"Jogador {rodada%2+1} VENCEU! Parabéns!")
      print('=-'*15)
      print()
      break
    rodada +=1
    if rodada == 9:
      showtab()
      print('=-'*5)
      print('DEU VELHA!')
      print('=-'*5)
      print()
      break

def Vencedor():
  #horizontais
  if (Tabuleiro[0] == Tabuleiro[1] == Tabuleiro[2]) and Tabuleiro[0] != '_':
    return True
  if (Tabuleiro[3] == Tabuleiro[4] == Tabuleiro[5]) and Tabuleiro[3]!= '_':
    return True
  if (Tabuleiro[6] == Tabuleiro[7] == Tabuleiro[8]) and Tabuleiro[6]!= '_':
    return True

  #Vertical
  if (Tabuleiro[0] == Tabuleiro[3] == Tabuleiro[6]) and Tabuleiro[0] != '_':
    return True
  if (Tabuleiro[1] == Tabuleiro[4] == Tabuleiro[7]) and Tabuleiro[1] != '_':
    return True
  if (Tabuleiro[2] == Tabuleiro[5] == Tabuleiro[8]) and Tabuleiro[2] != '_':
    return True

  #Diagonal
  if (Tabuleiro[0] == Tabuleiro[4] == Tabuleiro[8]) and Tabuleiro[0]  != '_':
    return True
  if (Tabuleiro[2] == Tabuleiro[4] == Tabuleiro[6]) and Tabuleiro[2] != '_':
    return True
  return False

        


def showtab():
  print(f'{Tabuleiro[0]:^3}|{Tabuleiro[1]:^3}|{Tabuleiro[2]:^3}')
  print(f'{Tabuleiro[3]:^3}|{Tabuleiro[4]:^3}|{Tabuleiro[5]:^3}')
  print(f'{Tabuleiro[6]:^3}|{Tabuleiro[7]:^3}|{Tabuleiro[8]:^3}')

def tutorial():
  print('='*37)
  print(' <<<<  J O G O  D A  V E L H A  >>>>')
  print('='*37)
  tutorial = [1,2,3,4,5,6,7,8,9]
  print(f'            {tutorial[0]:^3}|{tutorial[1]:^3}|{tutorial[2]:^3}')
  print(f'            {tutorial[3]:^3}|{tutorial[4]:^3}|{tutorial[5]:^3}')
  print(f'            {tutorial[6]:^3}|{tutorial[7]:^3}|{tutorial[8]:^3}')
  print()
  print('Cada jogador deve escolher uma casa\n  que será preenchida com X para\n o jogador 1 e O para o jogador 2')




tutorial()
print()

while True:
  try:
    op = int(input('Deseja jogar?\n0.Não\n1.Sim\n'))
    if op == 1:
      op2 = 1
      while op2 == 1:
        jogo()
        Tabuleiro = ['_','_','_','_','_','_','_','_','_']

        op2 = 0
    elif op == 0:
      print('Até a proxima!')
      break
    else:
      print('Operação invalida')
  except Exception as e:
    print(f'Problema: {e}')