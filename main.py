int(input("Please enter your password to encode: "))


def encoder(password):
    result = " "
    for i in password:
        result += int(i) - 2
        result = str(result)
    return result
