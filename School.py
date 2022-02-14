class School():
    """Sozdan wkola"""
    def __init__(self, number,sinif,fanlar):
        self.number = number
        self.sinif = sinif
        # self.oqtuvchilar = oqtuvchilar
        # self.oquvchilar = oquvchilar
        self.fanlar = fanlar
        # print('maktab yaraldi')
    def group(self):
        """skolka klasov """
        desc =str(self.number,) +'-Maktab.' + str(self.sinif) + 'ta -sinif.' + str(self.fanlar) + 'ta -fan'
        return desc
    def teacher(self):
        """O'qtuvchilar royhati"""
        print('Azimov Aziz - Matematika fanidan oqtuvchi')
        print('Jorayeva Sevara - Angliskiy fanidan oqtuvchi')
        print('Choriyev Muzafar - IT program fanidan oqtuvchi')
        print('Azimov Nodir - JIsomiy fanidan oqtuvchi')
        print('Soliyev  - Matematika fanidan oqtuvchi')
        print('Aripova Aziza - Rustili fanidan oqtuvchi')
        print('Qosimov Sasha - Fransuz  fanidan oqtuvchi')
        print('Ergashov Odil - Fizika fanidan oqtuvchi')
        print('Azimova Mariya - Kimyo fanidan oqtuvchi')
class students(School):
    def __init__(self, name ,sinif, fanlari, ):
        """Vorisilik """
        super(). __init__(name, sinif , fanlari, )
        self.name = name
        self.sinif = sinif
        self.fanlari = fanlari
        self.fanlar_f = 'fizika'
        # print('Sinif yaratildi ')

    def fanlar(self):
        print('yana 8 fani bor ')

    def group(self):
        """skolka klasov """
        desc = str(self.name, ) + ' oquvchi.' + str(self.sinif) + 'chi a-sinif.' + str(self.fanlari) + 'lar'
        return desc
"""maktab raqami newta sinf borligi va fanlari"""
# my = School(48,12,9)
# print(my.group())

"""O'quvchilar  royhato va fanlari"""
# sinif = students ('Aziz',6,'Matimatika')
# sinif_1 = students ('masha',6,'Matimatiklar')
# sinif_2 = students ('Sanjar',6,'Matimatiklar')
# sinif_3 = students ('Nodira',6,'Matimatiklar')
# sinif_4 = students ('Aziza',6,'Matimatiklar')
# sinif_5 = students ('Nurmuhamad',6,'Matimatik')
# sinif_6 = students ('Siroj',6,'Matimatiklar')
# sinif_7 = students ('Sher',6,'Matimatiklar')
# sinif_8 = students ('nodir',6,'Matimatiklar')
# sinif_9 = students ('Azi',6,'Matimatiklar')
# sinif_10 = students ('Bob',6,'Matimatiklar')
# sinif_11 = students ('komola',6,'Matimatiklar')
# sinif_12 = students ('siroj',6,'Matimatiklar')
# sinif_13 = students ('agzam',6,'Matimatiklar')
# print(sinif.group ())







#
# print(sinif_1.group())

#
#
# print(my.group())
# m1 = students('bbb', 7, )


# sinif = students (str('Aziz',9,'Matimatika'))
# sinif_1 = students ('masha',6,'Matimatiklar')
# sinif_2 = students ('Sanjar',6,'Matimatiklar')
# sinif_3 = students ('Nodira',6,'Matimatiklar')
# sinif_4 = students ('Aziza',6,'Matimatiklar')
# sinif_5 = students ('Nurmuhamad',6,'Matimatik')
# sinif_6 = students ('Siroj',6,'Matimatiklar')
# sinif_7 = students ('Sher',6,'Matimatiklar')
# sinif_8 = students ('nodir',6,'Matimatiklar')
# sinif_9 = students ('Azi',6,'Matimatiklar')
# sinif_10 = students ('Bob',6,'Matimatiklar')
# sinif_11 = students ('komola',6,'Matimatiklar')
# sinif_12 = students ('siroj',6,'Matimatiklar')
# sinif_13 = students ('agzam',6,'Matimatiklar')
# # print(sinif.group())
# print(sinif_1.group())
# print(sinif_2.group())
# print(sinif_3.group())
# print(sinif_4.group())
# print(sinif_5.group())
# print(sinif_6.group())






#     def students(self):
#         print('zdes 10 studentov yest')
#
# my_schol = School(48)
# print(my_schol.number,'-maktab')
# my_schol.group()
