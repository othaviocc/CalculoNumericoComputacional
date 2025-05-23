# -*- coding: utf-8 -*-
"""Aula 1.2 exercício 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tVOmywuW12sTl3BPHU3ZXrlZVIW4LaSY
"""

import numpy as np
import sympy as sp  # Biblioteca para interpretar expressões matemáticas de forma segura

# Entrada dos parâmetros do sistema de ponto flutuante
base = int(input("Digite a base do sistema de ponto flutuante: "))
digitos_mantissa = int(input("Digite a quantidade de dígitos na mantissa: "))
exp_min = int(input("Digite o expoente mínimo: "))
exp_max = int(input("Digite o expoente máximo: "))

# Entrada do número a ser representado, permitindo expressões como sqrt(7)
numero = float(sp.sympify(input("Digite o número que deseja representar no SPF (ex: sqrt(7), 2**(1/3)): ")))

# Passo 1: Normalizar o número na forma m × base^e
if numero == 0:
    print("O número 0 é representado exatamente no SPF.")
else:
    expoente = int(np.floor(np.log10(abs(numero)) / np.log10(base)))
    mantissa = numero / (base**expoente)

    # Passo 2: Arredondar a mantissa para o número especificado de dígitos
    mantissa = round(mantissa, digitos_mantissa - 1)

    # Se o arredondamento fez a mantissa ficar >= base, ajustamos
    if mantissa >= base:
        mantissa /= base
        expoente += 1

    # Passo 3: Verificar se o expoente está dentro dos limites do SPF
    if expoente < exp_min or expoente > exp_max:
        print("\nErro: O número não pode ser representado no SPF devido aos limites do expoente.")
    else:
        print(f"\nRepresentação de {numero} no SPF ({base}, {digitos_mantissa}, {exp_min}, {exp_max}) usando arredondamento:")
        print(f"{mantissa} × {base}^{expoente}")