#2019-02-28
#Christophe Roux

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

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
