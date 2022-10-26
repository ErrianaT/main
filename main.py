# Erriana Thomas


def encoder(password):
    result = " "
    for i in password:
        result += int(i) - 2
        result = str(result)
    return result


def decoder(password):
    decoded_string = " "
    for i in password:
        decoded_string += int(i) - 3
        decoded_string = str(decoded_string)
    return decoded_string


debug = True

while debug:
    print("Menu\n" + ("-" * 13))
    print("1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))
    password = int(input("Please enter your password to encode: "))

    if option == 1:


    elif option == 2:
        print("")
    if option == 3:
        break

