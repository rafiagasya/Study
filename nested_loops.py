# Nested loops
rows = int(input('Enter your rows :'))
columns = int(input('Enter your coloumns :'))
type = input('Enter your type :')

# Membuat variable awal
biner = 10
desimal = 10
panjang = 20
lebar = 40

# Membuat looping 
def lingkaran_persegi(biner, desimal):
    return biner * desimal

def lingkaran_panjang(panjang, lebar):
    return panjang * lebar

# Membuat hasil ke-3
result = lingkaran_panjang(40, 50)
print(result)

# Membuat hasil
result = lingkaran_persegi(10, 30)
print(result)

# Membuat rows
for biner in range(desimal):
    for s in range (panjang):
        print(type, end=' ')
    print()
    
# Membuat hasil code
for r in range(rows):
    for a in range(columns):
        print(type, end='')
    print()
    
