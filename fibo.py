def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    n = int(input("Introduce la cantidad de términos de la secuencia de Fibonacci que deseas ver: "))
    print("Secuencia de Fibonacci:")
    for val in fibonacci(n):
        print(val,end=" ")
    print()


if __name__ == "__main__":
    main()

