

def cezar_message(message, key):
    encrypted_message = ''
    for i in message:
        if i.isalpha():
            digit = ord(i) + key
            print(digit, end=' ')

            if i.isupper():
                if digit > 90:
                    digit -= 26
                elif digit < 65:
                    digit +=26

            else:
                if digit > 122:
                    digit -= 26
                elif digit < 97:
                    digit += 26

            encrypted_message += chr(digit)
        else:
            encrypted_message += i
    return encrypted_message


print("\n Twoja zaszyfrowana wiadomość to: ", cezar_message("Asia", 12))




