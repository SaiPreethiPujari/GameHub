#casier chiper
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encryption(plain_text,shift_key):
    casier_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position=(position+shift_key)%26
            casier_text =casier_text+alphabets[new_position]
        else:
            casier_text+=char
    print(f"The casier text is {casier_text}")

plain_text=""
def decryption(casier_text,shift_key):
    plain_text = ""
    for char in casier_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position=(position-shift_key)%26
            plain_text =plain_text+alphabets[new_position]
        else:
            plain_text+=char
    print(f"The casier text is {plain_text}")

wanna_do = False
while not wanna_do:
    what_to_do = input("Enter 'encrpt' for encryption or 'decrypt' for decryption: ").lower()
    text=input("Enter any text: ")
    shift=int(input("Enter any number: "))

    if what_to_do=='encrypt':
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=='decrypt':
        decryption(casier_text=text,shift_key=shift)
    else:
        print("Enter valid input")
    quit = input("Enter q to quit: ").lower()
    if quit=="q":
        wanna_do = True
        print("Have a good day.Bye...!!!")

