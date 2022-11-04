# Erriana Thomas


def encoder(passkey):
    encode = ''

    # iterate through each number
    for i in passkey:
        # adds 3
        encode += str(int(i) + 3)
    return encode


def decoder(passkey):
    decode = ""
    for i in passkey:
        decode += str(int(i) - 3)
    return decode


debug = True
h
while debug:
    print("\nMenu\n" + ("-" * 13))
    print("1. Encode\n2. Decode\n3. Quit\n")

    option = int(input("Please enter an option: "))

    if option == 1:
        password = input("Please enter your password to encode: ")
        res = encoder(password)
        print("Your password has been encoded and stored!")

    elif option == 2:
        decoded_result = decoder(res)
        print(f"The encoded password is " + res + " and the original password is" + decoded_result)

    elif option == 3:
        break
