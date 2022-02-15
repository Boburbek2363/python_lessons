class Boss(object):
    def __init__(self, name,):
        self.name = name

class Magazine(Boss):
    def __init__(self, name, lacation, n_owner,n_employees ):
        self.name = name
        self.lacation = lacation
        self.n_owner = n_owner
        self.n_employees = n_employees
    def form(self):
        print(self.name,  '2018 ish boshlagan  magazini General direktori ' + ' '+ self.n_owner  + ' Ularni qolida  ' + self.n_employees + ' IShci iwlid' )

# d1 = Magazine ('Havas', str('177780'),'Aziz Azimov', str('5'))
# d1.form()

class info_worker(Boss ):
    def __init__(self, name):
        Boss.__init__(self, name, )
        self.worker = []
        self.balans = []

    def add_worker(self, *workers):
        for worker in workers :
            self.workers.append(worker)

    def delete_worker(self, worker):
        self.workers.remove(worker)

    def get_ages(self):
        for ages in self.age:
            ages.get_age()

class enter_exit(Boss):
    def __init__(self, name):
        Boss.__init__(self, name)
        self.workers = []


    def add_worker(self, *workers):
        for worker in workers:
            self.workers.append(worker)

    def delete_subjects(self, worker):
        self.workers .remove(worker)

    def get_wokers(self):
        for woker in self.wokers:
            woker.get_name()

class worker(Boss):
    def __init__(self, name, age, date):
        Boss.__init__(self, name)
        self.age = age
        self.date = date
        self.subjects = []

    def get_name(self):
        print('Ishchini nomi ', self.name + ' Yoshi ' + ' ' + self.age + ' Ishla qirgan sanasi ' + self.date)

    def add_subjects(self, *subject):
        for i in subject:
            self.subjects.append(i)

    def delete_subjects(self, subject):
        self.subjects.remove(subject)

    def get_subjects(self):
        for subject in self.subjects:
            subject.get_name()

class Subject(Boss):
    def __init__(self, name, age, job):
        Boss.__init__(self, name)
        self.age = age
        self.job = job

    def get_name(self):
        print('Ismi', self.name,'Yoshi',self.age + 'da lavozimi' + ' ' + self.job)

# d1 = worker('Bobur','22','12.02.22')
# d1.get_name()
#
# sub1 = worker('Faruh', '22', '12.01.20')
# sub2 = worker('Nozi', '18', '21.9.21')
# sub3 = worker('Faruh', '22', '15.06.18')
# sub4 = worker('Faruh', '22', '1.01.22')

d1 = worker ('Bobur','22','12.02.22')


sub1 = Subject('Fazlidin', '22', 'polkaci')
sub2 = Subject('Nozi', '18', 'Kassir')
sub3 = Subject('Feruza', '22', 'razdacha')
sub4 = Subject('Faruh', '22', 'Kassir')
d1.get_name()
d1.add_subjects(sub1, sub2, sub3, sub4,)
d1.get_subjects()
