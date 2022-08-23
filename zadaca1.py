#svakom studentu generirati nasumičnu ocjenu od 1 do 5.
#Prebrojati u rječnik koliko ima kojih ocjena.
#Izračunati postotak prolaznosti. (sve ocjene veće od 1).

import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

studenti = {}
for ime in imena:
    studenti[ime] = random.randint(1,5)

uk = 0
for ime in studenti:
    uk += 1 #ukupan broj studenata
print("ukupan broj studenata",uk)

ocjena1 = 0
ocjena2 = 0
ocjena3 = 0
ocjena4 = 0
ocjena5 = 0

for ime in studenti:
    if studenti[ime]==1:
        ocjena1 +=1
    elif studenti[ime]==2:
        ocjena2 +=1
    elif studenti[ime]==3:
        ocjena3 +=1
    elif studenti[ime]==4:
        ocjena4 +=1
    elif studenti[ime]==5:
        ocjena5 +=1
print(studenti)
prolaznost = (ocjena2+ocjena3+ocjena4+ocjena5)/uk
postotak = round(prolaznost*100,2)
print("broj studenata koji nisu polozili:",ocjena1, ",broj studenata s ocjenom 2:",ocjena2, ",broj studenata s ocjenom 3:",ocjena3, ",broj studenata s ocjenom 4:",ocjena4, ",broj studenata s ocjenom 5:",ocjena5, ",postotak prolaznosti je:", postotak)


