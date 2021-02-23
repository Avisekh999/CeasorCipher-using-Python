alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z']


def caesor(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)      
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        
        else:
            end_text += letter
    


    print(f"The {cipher_direction} text  is {end_text}")



from art import logo
print(logo)



should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    text = input("Type your text: \n").lower()
    shift = int(input("Type the shift number: \n"))


    shift = shift % 26
    caesor(start_text = text, shift_amount = shift, cipher_direction = direction)

    result = input("Type 'yes' if you want to go again.otherwise type 'no' .\n").lower()

    if result == "no":
        should_continue = False
        print("GoodBye")










# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")



# def decrypt(cipher_text, shift_amount):
#     decode_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decode_text += new_letter
#     print(f"The encoded text is {decode_text}")


# if direction == "encode":
#     encrypt(plain_text = text, shift_amount = shift)

# elif direction == "decode":
#     decrypt(cipher_text = text, shift_amount = shift)







