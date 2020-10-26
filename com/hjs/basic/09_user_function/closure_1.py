def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of


def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input - 1)

    return inner_factorial(input)

if __name__ == '__main__':
    # square = nth_power(2)
    # print(square)
    # print(square(2))
    # cube = nth_power(3)
    # print(cube)
    # print(cube(3))
    print(factorial(5))
