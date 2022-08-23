#Iz podataka učitanih iz datoteke rezultati.csv sortirati listu po prezimenima.
#Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena.

from csv import reader
with open('rezultati.csv', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    rezultati = list(map(tuple, csv_reader))

rjecnik = {
    "nedovoljan:" : 0,
    "dovoljan:" : 0,
    "dobar:" : 0,
    "vrlo dobar:" : 0,
    "odlican:": 0,
}

for ime,prezime,bodovi in rezultati:
    if int(bodovi) <= 49:
        rjecnik["nedovoljan:"] += 1
    elif int(bodovi) > 49 and int(bodovi) <= 64:
        rjecnik["dovoljan:"] += 1
    elif int(bodovi) > 64 and int(bodovi) <= 79:
        rjecnik["dobar:"] += 1
    elif int(bodovi) > 79 and int(bodovi) <= 89:
        rjecnik["vrlo dobar:"] += 1
    else:
        rjecnik["odlican:"] += 1
    
for broj in rjecnik:
    print('Ocjena:', broj, ',', ' ', 'Ukupni broj ocjena:', rjecnik[broj])
