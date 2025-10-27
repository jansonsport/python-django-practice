import math

def primes(number_of_primes):
    my_list = []
    if number_of_primes < 1:
        raise ValueError("input should be higher than 1")
    num = 2
    while len(my_list) < number_of_primes:
        limit = int(math.sqrt(num))
        is_prime = True
        for x in my_list:
            if x > limit:
                break
            if num % x == 0:
                is_prime = False
                break
        if is_prime:
            my_list.append(num)
        num += 1

    return my_list

primes_list = primes(10)
print(primes_list)