times = []
dic = {}
jogos = []

for x in range(16):
  pais = input(f'{x+1}ª Seleção: ').lower()
  times.append(pais)
  dic[f'{pais}'] = {'partidas':0,'normal':0, 'penaltis':0, 'vitorias':0, 'derrotas':0, 'marcados':0, 'sofridos':0}

print()
print('Por favor insira os resultados dos jogos no seguinte formato: time1 2 x 0 time2')
print('Em caso de penaltis, insira no seguinte formato: time1 2 x 2 (3 x 2) time2')
print()
for y in range(16):
  jogo = input(f'Resultado do jogo {y+1}: ').lower()
  jogos.append(jogo.split())

for jogo in jogos:
  if len(jogo) == 8:
    dic[jogo[0]]['partidas'] += 1
    dic[jogo[-1]]['partidas'] += 1
    dic[jogo[0]]['penaltis'] += 1
    dic[jogo[-1]]['penaltis'] += 1
    dic[jogo[0]]['marcados'] += int(jogo[1])
    dic[jogo[-1]]['marcados'] += int(jogo[3])
    dic[jogo[0]]['sofridos'] += int(jogo[3])
    dic[jogo[-1]]['sofridos'] += int(jogo[1])
    if int(jogo[4].lstrip('(')) > int(jogo[6].rstrip(')')):
      dic[jogo[0]]['vitorias'] += 1
      dic[jogo[-1]]['derrotas'] += 1
    else:
      dic[jogo[0]]['derrotas'] += 1
      dic[jogo[-1]]['vitorias'] += 1

  elif len(jogo) == 5:
    dic[jogo[0]]['partidas'] += 1
    dic[jogo[-1]]['partidas'] += 1
    dic[jogo[0]]['normal'] += 1
    dic[jogo[-1]]['normal'] += 1
    dic[jogo[0]]['marcados'] += int(jogo[1])
    dic[jogo[-1]]['marcados'] += int(jogo[3])
    dic[jogo[0]]['sofridos'] += int(jogo[3])
    dic[jogo[-1]]['sofridos'] += int(jogo[1])
    if int(jogo[1]) > int(jogo[3]):
      dic[jogo[0]]['vitorias'] += 1
      dic[jogo[-1]]['derrotas'] += 1
    else:
      dic[jogo[0]]['derrotas'] += 1
      dic[jogo[-1]]['vitorias'] += 1
    
for time in times:
  print('-'*50)
  print(f"Pais: {time.capitalize()}")
  print("Partidas:", dic[time]["partidas"])
  print("Partidas decididas em tempo normal de jogo:", dic[time]["normal"])
  print("Partidas decicidas nos penaltis:", dic[time]["penaltis"])
  print("Vitorias:", dic[time]["vitorias"])
  print("Derrotas:", dic[time]["derrotas"])
  print(f'Gols marcados: {dic[time]["marcados"]}')
  print(f'Gols sofridos: {dic[time]["sofridos"]}')

for time in times:
  if dic[time]['derrotas'] == 0:
    print('-'*50)
    print(f'Pais campeão: {time.capitalize()}')
    print('-'*50)