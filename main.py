
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','r','s','t','u','v','w','x','y','z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

simbols = ['!','#','$','%','&',',','*','+','-','_','/','|']

print("Bem vindo ao gerador de senhas!")

n_letters = int(input("Quantas letras vocêdeseja em sua senha?\n"))
n_simbols = int(input(f"quantos simbolos você gostaria?\n"))
n_letters = int(input(f"quantos numeros você gostaria?\n"))

password_list = []

for char in range(1, n_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, n_simbols + 1):
  password_list.append(random.choice(simbols))

for char in range(1, n_numbers + 1):
  password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
  password += char

  print(f"sua senha é: {password}")


