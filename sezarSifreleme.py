MAX_KEY_VALUE=26
def getType():
    while True:
        print("Sezar şifreleme ya da şifre çözme işlemi yapabilirsiniz...")
        type = input("Şifreleme veya şifre çözme işlemini seçiniz: (e or d)  ")
        if(type=="e" or type=="d"):
            return type
        else:
            print("Lütfen şifreleme için e, şifre çözme işlemi için d işlemlerini giriniz.")
def getKey():
    while True:
        key = int(input("Belirtilen aralıkta anahter değeri giriniz: 1-{} ".format(MAX_KEY_VALUE)))
        if(key>=1 and key<=26):
            return key
        else:
            print("Lütfen belirtilen aralıkta bir değer giriniz... 1-{}".format(MAX_KEY_VALUE))
def getMessage(message,key,type):
    if type == "d":
        key = -key
    translated = ""
    for letter in message:
        if letter.isalpha():
            newLetter = ord(letter)
            newLetter += key
            if letter.isupper():
                if newLetter > ord("Z"):
                    newLetter -= 26
                elif newLetter < ord("A"):
                    newLetter += 26
            elif letter.islower():
                if newLetter > ord("z"):
                    newLetter -= 26
                elif newLetter < ord("a"):
                    newLetter += 26
            translated +=chr(newLetter)
        else:
            translated+=letter
    return translated


type = getType()
key = getKey()
message = input("Mesajınızı giriniz: ")

print("Şifrelenen mesaj: {}".format(getMessage(message,key,type)))