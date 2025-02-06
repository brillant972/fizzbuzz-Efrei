def fizzbuzz(n):
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)

def main():
    for n in range(1, 101):
        print(fizzbuzz(n))

if __name__ == '__main__':
    main()
