name = input('Input your name :')
phone_number = input('Inpur your phone number :')

# Membuat function
result = name.find('O')
result = phone_number.replace('-', '')

# Mecetak hasil
print(result)
print(phone_number)

# Membuat Variable baru
username = input('Enter your username :')

if len(username) > 12:
    print('Your username')
elif not username.find(' ') == -1:
    print('Your username correct')
elif not username.isalpha():
    print('Your correct')
else:
    print('Your correct answer')