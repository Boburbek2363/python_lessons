1.n natural soni berilgan.(100 >n>99).Shu sonning yuzlar xonasini aniqlovchi programma tuzilsin.
2. n natural soni berilgan.(9<n<100).Quyidigilarni aniqlovchi programma tuzilsin.
     1. N soni oxirgi raqami aniqlansin.
     2. N soni birinchi raqami aniqlansin.
     3. Raqamlari yig’indisi nimaga teng?
3. Uchburchakning tomonlari a,b,c berilgan. Geron formulasidan foydalangan holda uchburchak yuzini hisoblovchi programma tuzilsin.

n = int(input('Soni qiritng: '))
if n < 1000 or n > 99:
    print(n%100)
n = int(input("sonni qiriting: "))
if 9 < n < 100:
    print(n%10)
    print(n//10)
      d1 = n % 10
      d2 = n // 10
      print(d1 + d2)