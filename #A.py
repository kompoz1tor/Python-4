from random import randint
max_num = 100
k = int(input('Введите натуральную степень k:'))
koeff = [randint(0, max_num) for i in range(k)] + [randint(1, max_num)]
polynomial = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])

polynomial = polynomial.replace('x^1+', 'x+')
polynomial = polynomial.replace('x^0', '')
polynomial += ('','1')[polynomial[-1]=='+']
polynomial = (polynomial, polynomial[:-2])[polynomial[-2:]=='^1']
print(polynomial)