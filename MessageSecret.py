#2019-02-28
#Christophe Roux

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

fonction = input('Encrypter ou décrypter un message?[E/d]: ')

if fonction.lower() == 'e':

    key = input('Veuillez entrer une clé de cryptage: ')
    key = int(key)

    message = input('Veuillez entrer un message: ')

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character  
    print('Votre message encrypté est: ' + newMessage)

elif fonction.lower() == 'd':
    key = input('Veuillez entrer la clé de décryptage: ')
    key = int(key)

    message = input('Veuillez entrer le message à crypter')
