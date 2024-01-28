import random
dlina = int(input('Введите длину пароля:'))
lst = [random.randint(0,100) for i in range(dlina)]
print(random.sample(lst, len(lst)))
