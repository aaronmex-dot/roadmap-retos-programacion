
b = 2
c = 3
# Operadores Aritmeticos
+ , - , * , % , / , ** , //

suma = b + c
resta = b - c
multiplicacion = b * c
division = b / c
modulo = b % c
potencia = b ** c
print(f" Los operadores aritmeticos son:
      Suma: {suma},
      Resta: {resta},
      Multiplicacion: {multiplicacion}
      Division: {division}
      Potencia: {potencia}
      Modulo:{modulo}")


# Operadores Logicos   
AND , OR , NOT

x = a and b
y = a or b
z = not a

print(f"Los operadores son: \n AND: {x}, \n OR: {y}, \n NOT: {z}")

# Operadores de COMPARACION
!= , > , < , >= , <= , ==

a = 1
b = 2
c = 3
mayor =  c > a
menor =   a < c
igualdad =  a == b
mayor_o_igual_que =  a >= b
menor_o_igual_que =  c <= b
desigualdad  =    a != b

print("Los operadores de comparacion son:
      Mayor : {mayor}
      Mayor o igual que: {mayor_o_igual_que}
      Menor que: {menor}
      Menor o igual que: {menor_o_igual_que}
      Igualdad: {igualdad}
      Desigualdad: {desigualdad}\n""")


# Operadores de Asignacion 
El simbolo igual es el de asignacion mas comun  "="
Tambien se pueden utilizar 
+=
-=
*= 
print("Es posible utilizar los operadores de asignacion para incrementar o disminuir una variable en la cantidad requerida")

# Operadores de Identidad

si_es =  a is b
no_es = a is not b

print(f"Los operadores de identidad son:
      Es: {si_es},
      No es: {no_es}")

# Operadores de Pertenencia, 
IN   /   NOT IN 

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 99]
b = 3
c = 10
print(b in a)
>>> True
print( 89 in a)
>>> False

print ( c not in a)
>>> True

Print(" Evaluan si un elemento se encuentra dentro de una determinada coleccion")

# Estructuras de control 
While , For , If-Elif

if a > 18:
  print("You are  old enough")
elif a == 18:
  print("You are getting old")
elif a < 18:
  print("You are not old enough")
else:
  print("You have to pick again")


# FOR 
Se utiliza para iterar sobre elementos de un iterable, como una lista, tupla, diccionario, cadena, range etc...

fruits = ["Manzana" , "Pera" , "Melon" , " Durazno"]
for fruit in fruits:
  print(fruit)
Manzana
Pera
Melon
Durazno
# fruit representa cada elemento del iterable en cada iteracion 


# WHILE
Ejecuta su bloque de codigo mientras una condicion sea verdadera.

bill = 0 
while bill < 5:
  print(bill)
  bill += 1 
0
1
2
3
4

  
  


















      


