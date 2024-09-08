#CAESAR CIPHER MESSAGE Coder n Decoder:
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Alternate way...if u r not willing to add limit of *if new_position > 25* :

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#This is the indirect method including step by step explanation of the process...
'''def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
         position = alphabet.index(letter)
         new_position = position + shift

         if new_position > 25:
             new_position -= 26

         encrypted_text += alphabet[new_position]
    print(f"The encoded text is {encrypted_text}.")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift

        if new_position < 0:
            new_position += 26

        decrypted_text += alphabet[new_position]
    print(f"The decrypted text is {decrypted_text}")

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)'''

#This is the direct method of completion that includes summarized concept of the above written code...
def caesar(Given_text, shift_count, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_count *= -1
    for letter in Given_text:
        #condition for checking if char is in list...i.e to allow " ", "symbols" to comtinue...  
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_count
            if cipher_direction == "decode" and shift_count < 0:
                new_position += 26
            else:
                new_position -= 26
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f"The {cipher_direction}d text is {end_text}.")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift = shift % 26        
    caesar(Given_text = text, shift_count = shift, cipher_direction = direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'No'\n").lower()
    if result == 'no':
        should_continue = False
        print("Thanks for using...Goodbye")