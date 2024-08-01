let = 'trwagmyfpdxbnjzsqvhlcke'
def calc(dni): 
    sol, con = [], dni.count('?')
    for i in range(10**con):
        yes = dni[:-1]
        for j in range(con):
            yes = yes.replace('?',str(i).zfill(con)[j],1)
        if let[int(yes) % 23].upper() == dni[8].upper():
            sol.append(yes + dni[8])
    return sol

while True:
    dni = input('Introduce el DNI:    ')
    sol = calc(dni) if dni[8] != '?' else [dni[:-1] + let[int(dni[:-1]) % 23].upper()]
    print(sol)
    print("Hay " + str(len(sol)) + " resultado(s) compatible(s).")
