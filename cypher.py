code = ""
print("would you like to 1.encrypt or 2.decrypt?")
choicecrypt = input(">>")
print("would you like to 1. set your own *numerical* kay, or 2. use the default?")
choicekey = input(">>")
if choicekey == '1':
    print("input your key now")
    key = input(">>")
if choicekey == '2':
    key = 284
if choicecrypt == '1':
    print("enter your text to encrypt")
    encrypt = input('>>')
    encrypt = encrypt.replace(" ", "/")
    for x in encrypt:
        code = code + (chr(ord(x) + key))
if choicecrypt == '2':
    print("enter your text to decrypt")
    decrypt = input('>>')
    decrypt = decrypt.replace("/", " ")
    for x in decrypt:
        code = code + (chr(ord(x) - key))
print(code)