
## Lambda Sistemas - Challenge 

#### [Ejericio 1](https://github.com/zarate10/challenge-lambda-sistemas/blob/main/happy_numbers.py)

**Consigna**: Hacer un programa que imprima los X primeros [happy numbers](https://en.wikipedia.org/wiki/Happy_number). 

a) Modificar el programa para que tanto el valor final al que hay que llegar (1 en el caso de los happy numbers) como la potencia aplicada (2 en el caso de los happy numbers) sean parametrizables. 

b) Aplicar alguna optimización, suponiendo que la memoria no es problema. 

**Estrategia**: Se utilizó recursión para obtener la sumatoria de los dígitos de un número pasado por parámetro, y, en base a esa lógica, también se aplicó recursión para comprobar si el resultado de la sumatoria de los dígitos del número elevado a un n cumple con nuestro caso base en algún punto. 

* a) Cubierto.
* b) Para optimizar la implementación propuesta, en vez de guardar en un Set los elementos visitados, podríamos guardarlos en un ABB, de tal modo que a la inserción los elementos queden ordenados para que posteriormente la comprobación nos quede con un costo temporal O(log n).

#### [Ejericio 2](https://github.com/zarate10/challenge-lambda-sistemas/blob/main/happy_numbers.py)

**Consigna**: Hacer un programa que analice el archivo de recorridos de Bicicletas de la Ciudad y devuelva las tres estaciones de origen más “calientes” (de las que salen más recorridos) en la mañana (de 6 a 11:59) 
