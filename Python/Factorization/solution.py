def factorize(number):
    factors = []
    output = ''
    i = 2
    while number != 1:
        if number % i == 0:
            factors.append(i)
            number = number / i
        else:
            i += 1
    for item in list(set(factors)):
        output += '({}**{})'.format(str(item), str(factors.count(item)))
    print(output)

def main():
    factorize(480)

if __name__ == '__main__':
    main()