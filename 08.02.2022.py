class Ulov:
    volva = ('260','100','7')
    kiya_5  = ('280','100','7')
    jentra_1_5 = ('320','100','5')
    capa = ('280','100','8')
    matiz = ('180','100','16')


    def __init__(self,Vmax, Vo,a,name ):
        self.Vo = Vo
        self.Vmax =Vmax
        self.a = a
        self.name = name
    def formula(self):
      print(self.Vmax - self.Vo/self.a )

p1 = Ulov(int('220'),int('9'),int('100'),'nexi2')
p1.formula()






1