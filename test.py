# import random
print("Oyinda qaychi qudu va qog'oz boladi ")
print("sonlarni tanlang: \n 1)qog'oz \n 2)qaychi \n 3)quduq ")
def game():
  gamer = int(input('1 - dan 3 gacha bolgan soni tanlang!!! '))
  comp = int(input('1 - dan 3 gacha bolgan soni tanlang!!! '))
  if gamer == 1 and comp == 3:
    print("gamer qog'ozini tanladi va yuti!!! ")
  if gamer == 2 and comp == 3:
    print("comp qaychini tanladi va yuti!! ")
  if gamer == 3 and comp == 2:
    print("gamer qog'ozini tanladi va yuti!!!")
  elif gamer == 3 and comp == 3:
    print('Durang')
  elif gamer == 1 and  comp == 2:
    print('comp yuti !!!')
  elif gamer == 1 and comp == 1:
    print('Durang')
  else:
    print('1 -dan 3 gacha soni tanglang!!! ')
game()
while True:
   paftor = input('Bowqata oynash hohlasez restart dip yozin va oyin yana bowlanadi ')
   if paftor == 'restart':
     game()
   else:
     break