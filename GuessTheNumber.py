# Угадай число!
from random import randint
from time import sleep
last_ans = 'Эта программа топ!(>w<)'

def player_mind():
  print('Выбери промежуток, в котором будет угадываться загаданное число.\nНапиши два числа: сначала меньшее потом большее через пробел.')
  diap1, diap2 = input().split()
  diap1, diap2 = int(diap1), int(diap2)
  print('Теперь загадай число, а я буду угадывать!')
  counter = 0
  while True:
    counter += 1
    harder = randint(1, 3)
    if harder == 3:
      rand_n = diap1 + (diap2 - diap1) // 2
    else:
      rand_n = randint(diap1, diap2)
    sleep(3)
    print(f'Это число - {rand_n}?(Напиши "Да" или "Нет")')
    ans = input()
    if ans.lower() == 'да':
      print(f'Ура, я угадал твое число за {counter} попыток!')
      break
    elif ans.lower() == 'нет':
      print('Это число больше или меньше твоего?\nНапиши "Мое число больше", если твое число больше либо напиши "Мое число меньше", если твое число меньше.')
      ans = input()
      if ans.lower() == 'мое число больше':
        diap1 = rand_n + 1
      elif ans.lower() == 'мое число меньше':
        diap2 = rand_n - 1

def computer_mind():
  print('Выбери промежуток, в котором будет угадываться загаданное число.\nНапиши два числа: сначала меньшее потом большее через пробел.')
  diap1, diap2 = input().split()
  diap1, diap2 = int(diap1), int(diap2)
  print('Теперь угадывай!')
  rand_n = randint(diap1, diap2)
  counter = 0
  print('Напиши число, которое думаешь я загадал!')
  while True:
    counter += 1
    ans = int(input())
    sleep(1.5)
    if ans == rand_n:
      print(f'Вау, ты угадал моё число за {counter} попыток!')
      break
    elif ans != rand_n:
      if ans > rand_n:
        print('Мое число меньше!')
      else:
        print('Моё число больше!')




print('Привет, это программа угадай число!\nСмотри: либо ты загадываешь число, либо я. А потом один из нас его угадывает!')
while last_ans.lower() != 'нет':
  print('Если хочешь загадать число, пиши - "Я загадываю".\nЕсли хочешь поугадывать то пиши - "Ты загадываешь".')
  ans = input()
  if ans.lower() == 'я загадываю':
    player_mind()
  elif ans.lower() == 'ты загадываешь':
    computer_mind()
    sleep(3)
  print('Сыграем еще? Напиши "Да" или "Нет".')
  last_ans = input()