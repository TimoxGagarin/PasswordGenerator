from random import randint

count = int(input('Count of symbols: '))
password = ''

for i in range(count):
    password += chr(randint(0,256))

print(password)
#¯¬×éþmûÇ®ß£¬ÏaR
