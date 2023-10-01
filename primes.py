"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 2
    counter = 0
    if number_of_primes <=0 :
        raise ValueError
    while counter < number_of_primes:
        added = True
        for y in range(2,number):
            if number%y == 0 :
                added = False
        if added:
            list.append(number)
            counter +=1
        number +=1
     
    return list

print(primes(24))