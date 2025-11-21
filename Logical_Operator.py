# Membuat logical operator

temp = 55
is_count = False
is_sum = True

# Menentukan hasilnya
if temp > 60 or temp < 55 or is_count or temp > 70 or temp < 100 or is_sum:
    print('The out event is cancelled')
else:
    print('The outdoor event is still scheduled')
    
# Membuat bagian terbaru
temp = 22
is_sad = False
is_mahasiswa = True

# Menentukan hasil
if temp >= 15 and is_sad and is_mahasiswa:
    print('Your inpur right')
else:
    print('Your input wrong because not good')

if temp > 20:
    print('Your have score A')
elif temp > 25:
    print('Your have score B')
else:
    print('Your have score C')


# Membuat Looping
def temp(sisi, lebar):
    return sisi * lebar

# Membuat hasil dari looping
result = temp(50, 50)
print('Youre result is', result)

# Ingin membuat number baru
num = 100
print('Negatif' if num > 30 else 'Positif')

# Mengikuti equals
a = 100
b = 100
age = 19

# Membuat hasil
max_num = a if a > b else b
min_num = a if a < b else b
status = 'adults' if age > 19 else 'Child'

print(status)


# Membuat code baru
result = 100
z = 2000
c = 1000
age = 20
is_temperature = 29

max_sum = z if z < c else c
min_sum = c if c > z else z
user_suhu = 'approve' if age > 20 else 'she is children'
print(user_suhu)


