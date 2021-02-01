p = int(input('Введите длину пароля: '))


import random

def generate_good_password(length):
  # 1 задать алфавит
  alphabet = 'abcdefghijklmnopqrstuvwxyz'\
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
             '0123456789!@#$%^&*()_+,.'
  # 2 выбрать случайный символ из алфавита
  # 3 повторить 2 length раз
  # 4 склеить символы в строку
  password = ''
  for i in range(p):
    symbol = random.choice(alphabet)
    password += symbol
  return password

password = generate_good_password(p)
print(password)
