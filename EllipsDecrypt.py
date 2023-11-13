base = 751
secret_key = 27

encrypted_letters = [
            [(745, 210), (185, 105)],
            [(188, 93), (681, 385)],
            [(377, 456), (576, 465)],
            [(440, 539), (138, 298)],
            [(745, 210), (520, 2)],
            [(188, 93), (681, 385)],
            [(286, 136), (282, 410)],
            [(72, 254), (200, 721)],
            [(72, 254), (643, 94)],
            [(745, 210), (476, 315)],
            [(440, 539), (724, 229)]
]


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


# Расшифрование одного зашифрованного символа letter с секретным ключом key
def decrypt_letter(letter, key):

    nkg = points_multiplying(letter[0], key)
    nkg = (nkg[0], -1*nkg[1])
    decrypted_point = points_addition(letter[1], nkg)
    print('Decrypted point:', decrypted_point, end='\n\n')

    return decrypted_point


# Расшифрование всего текста
def decrypt_text(letters, key):

    return [decrypt_letter(letter, key) for letter in letters]


print('Answer:', decrypt_text(encrypted_letters, secret_key))



