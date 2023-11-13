import numpy as np
import pandas as pd


df = pd.read_excel('Variants.xlsx', header=0)


def ferma(N):
    t = int(np.sqrt(N)) + 1

    while True:

        w = t * t - N
        sqrt_w = int(np.sqrt(w))

        if sqrt_w * sqrt_w == w:
            p = t + sqrt_w
            q = t - sqrt_w

            print(f"Iteration: t={t}, w={w}, sqrt(w)={sqrt_w}, p={p}, q={q}")

            return p, q

        else:
            print(f"Iteration: t={t}, w={w} -- not square")
        t += 1


class Message:
    def __init__(self, variant, N, e, C):
        self.variant = variant
        self.N = N
        self.e = e
        self.C = C
        self.text = None

    def decrypt_message(self):
        p, q = ferma(self.N)
        phi = (p - 1) * (q - 1)
        d = pow(self.e, -1, phi)

        message = ''
        for c in self.C.split('\n'):
            m = pow(int(c), d, self.N)
            try:
                part = m.to_bytes(4, byteorder='big').decode('cp1251')
            except:
                part = '<None>'
            message += part

        self.text = message


messages = list()
full_text = ''

for idx, line in df.iterrows():
    messages.append(Message(*line.to_list()))

for message in messages:
    if message.variant != 11:
        message.decrypt_message()
    else:
        message.text = '<None>'

    # message.decrypt_message()

    print(f'{message.variant}. {message.text}', end='\n\n')
    full_text += message.text


print(f'\nПолный текст:\n\n {full_text}')



