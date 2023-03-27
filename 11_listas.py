primera_lista = ['Manzana', 'Banano']
print(primera_lista)
nombres = ['Angélica', 'Miguel', 'Sarah']
print(nombres)

lista1 = [2, 4, 70, 5000, 2.55]
print(lista1)
lista2 = ['a', 123, 'A', 3.1416, 'Palabra', True, 2000]
print(lista2)
# Tamaño de una lista (len):
print('Tamaño de Lista')
print(len(lista1))
print(len(lista2))
# Tipo de Dato Lista:
print('Tipo de dato lista:')
print(type(lista1))
print(type(lista2))
# Otra lista:
print('Función list():')
num = [1, 2, 3, 4, 5]
print(num)
num2 = list([1, 2, 3, 4, 5])
print(num2)
print('Index list:')
print(num[0])
print(num[0:3])
print(num[-1::-1])
print('Uso de función IN:')
print(3 in num)
print(10 in num)
num1 = num
print(num)
print(num1)
print(num2)
print(num1 is num)
print(num2 is num)
print(num is num2)