base = 751
generation_point = (0, 1)
open_key = (179, 275)

letters = {
    (240, 442): 9,
    (243, 87): 5,
    (240, 309): 17,
    (237, 454): 2,
    (234, 587): 2,
    (235, 19): 2,
    (234, 587): 3,
    (238, 576): 17,
    (256, 121): 15
}


# Поиск противоположного числа при вычислениях в классах эквивалентности по модулю base
def reciprocal_search(number, base):
    i = 1
    while True:
        if number * i % base == 1:
            # print('Reciprocal number is', i)
            return i
        i += 1


# Перевод координаты точки в класс эквивалентности по модулю base
def mod(x, base):

    if type(x) == int:
        if x > 0:
            return x % base
        else:
            return base - abs(x) % base

    else:
        a, b = x
        if a > 0:
            return mod(a*reciprocal_search(b, base), base)
        else:
            return base - mod(abs(a)*reciprocal_search(b, base), base)


# Сложение точек A и B
def points_addition(A, B):
    print(f'{B} + {A}')
    x0, y0 = A[0], A[1]
    x1, y1 = B[0], B[1]
    if A == B:
        lam_a = (3*x0**2 - 1)
        lam_b = (2*y0)
    else:
        lam_a = (y1-y0)
        lam_b = (x1-x0)

    lam = mod((lam_a, lam_b), base)
    print(f'lambda: {lam_a}/{lam_b} = {lam} mod {base}')
    x2 = mod(lam**2 - x0 - x1, base)
    print(f'x: {lam}^2 - {x0} - {x1} = {lam**2 - x0 - x1} = {x2} mod {base}')
    y2 = mod(lam*(x0-x2)-y0, base)
    print(f'y: {lam}*({x0}-{x2}) - {y0} = {lam*(x0-x2)-y0} = {y2} mod {base}', end='\n\n')
    return x2, y2


# Умножение A саму на себя k раз
def points_multiplying(A, k):
    S = A
    for i in range(k-1):
        S = points_addition(A, S)
    return S


# Шифрование одного символа с координатой на эллиптической кривой letter_point, гентерирующей точкой generation_point,
# открытым ключом key и случайным значением k
def encrypt_letter(letter_point, generation_point, key, k):

    print(f'Encryption of point {letter_point}', end='\n\n')
    # First point
    point1 = points_multiplying(generation_point, k)
    print('First point:', point1, end='\n\n')

    # Second point
    point2 = points_addition(letter_point, points_multiplying(key, k))
    print('Second point:', point2, end='\n\n')

    print(f'Letter: {letter_point}, encrypted: {[point1, point2]}', end='\n\n')

    return [point1, point2]


# Шифрование всего текста
def encrypt_text(letters, generation_point, key):

    return [encrypt_letter(letter, generation_point, key, letters[letter]) for letter in letters]


print('Answer:', encrypt_text(letters, generation_point, open_key))


