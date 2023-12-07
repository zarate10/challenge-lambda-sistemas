class HappyNumbers: 
    def __init__(self, n_base=1, exponent=2):
        self.n_base = n_base
        self.exponent = exponent

    def sum_exponentiated_numbers(self, n: int, total: int) -> int: 
        if n < 1: 
            return total
        else: 
            last_digit = n % 10 
            return self.sum_exponentiated_numbers(n // 10, total + last_digit ** self.exponent)

    def precalculated(self, n: int, visited_set: set) -> bool:
        return n in visited_set

    def is_happy_number(self, n: int, visited_set: set) -> bool:
        """
        Verifica si un número es feliz o no. 

        1. Se verifica si n == número base (caso base para happy numbers = 1). 

        2. Se comprueba que la suma actual de los dígitos elevados a un número determinado (exponent) no haya 
        sido previamente precalculada (esto indica que se inició un ciclo del que no podemos salir).

            2.1. Si se calculó -> return False                                                                                  
            2.2. Sino se calculó, se guarda el resultado y se llama recursivamente a la función con ese resultado, vuelve al paso 1. 
        """
        if n == self.n_base: 
            return True 
        else: 
            current_sum = self.sum_exponentiated_numbers(n, 0)

            if self.precalculated(current_sum, visited_set): 
                return False 
            
            visited_set.add(current_sum)
            return self.is_happy_number(current_sum, visited_set)

    def get_first_happy_numbers(self, max_num: int) -> list:
        return [n for n in range(1, max_num) if self.is_happy_number(n, set())]
    
    def show_first(self, n: int): 
        result = self.get_first_happy_numbers(n)
        print(f"\nPrimeros {n} numeros felices: {' '.join(map(str, result))}")


hn = HappyNumbers()
hn.show_first(100) # output: 1 7 10 13 19 23 28 31 32 44 49 68 70 79 82 86 91 94 97

hn2 = HappyNumbers(2, 5)
hn2.show_first(100) # output: 2, 11