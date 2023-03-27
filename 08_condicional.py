# Condicional if
adivinar = 40
number = int(input('Sr usuario, digite un número:'))
if (number > adivinar):
  print('Valor más pequeño')
elif (number < adivinar):
  print('Aumente el valor')
else:
  print("VERDADERO")

# IF anidado 2:
if (number >= adivinar):
  if (number > adivinar):
    print('Coloque un número menor.')
  else:
    print('Acertado!!!')
else:
  print('Coloque un número mayor')
# Fin del IF.

print('La instrucción "IF" terminó')
