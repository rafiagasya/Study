import time

my_clock = int(input('Enter your code right here:'))

for f in range(0, my_clock):
    minute = int(f / 60)
    hours = int(f / 360)
    print(f'{hours:05}: {minute:02}')
    time.sleep(1)
print('Going weke up')