def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    return [x for x in range(2, limit + 1) if is_prime(x)]

def main():
    try:
        limit = int(input("Introduce el límite superior para generar números primos: "))
        primes = generate_primes(limit)
        print("Números primos hasta el límite especificado:", primes)
    except ValueError:
        print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()


