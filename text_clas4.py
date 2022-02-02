If1. Butun son berilgan. Agar, berilgan son musbat bo’lsa, 1 ga oshirilsa, aks holda o’zgartirilmasin. Hosil bo’lgan sonni ekranga chiqaruvchi programma tuzilsin.
a = int(input('butun son yozing: '))
plus = 0
if a < 0:
   plus += 1
   print(plus,'ga oshirildi ')
else:
    print(a,'son manfiy ')
IF. 1-7 gacha bo’lgan butun sonlar berilgan. Kiritilgan songa mos ravishda hafta kunlarini so’zda ifoydalovchi programma tuzilsin. (1- Dushanba, 2- chorshanba,…h.k)

days = int(input('Hafta kunini tanglang: '))

if days == 1:
    print(days,'kun Dushanba ')
if days == 2:
    print(days,'kun Seshanba' )
if days == 3:
    print(days,'kun Chorshanba' )
if days == 4:
    print(days,'kun Payshanba' )
elif days == 5:
    print(days,'kun Jumma' )
elif days == 6:
    print(days,'kun Shanba' )
elif days == 7:
    print(days,'kun Yakshanba' )
else:
    print('Hafta kuni 7 kunda iborat ')

IF3. Oy raqamini berilgan. Kiritilgan oy qaysi faslga tegishli ekanligini chiqaruvchi programma tuzilsin.(Masalan: 2 chi oym ‘’qish’’).

month = int(input('soni qiriting: '))
if month == 1:
    print(month,'bu fasil Yoz bunga Iyun Iyul Avgust qiradi: ')
if month == 2:
    print(month,'Bu fasil Kuz bunga Sentabir Oktabir Noyabir qiradi')
elif month == 3:
    print(month,'Bu fasil Qish bunga Dekabi Yanvar Fevral qiradi')
elif month == 4:
    print(month,'Bu fasil Bohor bunga Mart Aprel  May qiradi')
elif 4 < month > 0:
    print(month,'Bowqa fasil va oy qomadi 1yilda 4 ta fasil fa 12 oy bor ')
