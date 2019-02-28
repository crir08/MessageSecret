#2019-02-28
#Christophe Roux

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = input('Veuillez entrer une clé de cryptage: ')
key = int(key)

character = input('Veuillez entrer un caractère: ')

position = alphabet.find(character)

newPosition = (position + key) % 26

newCharacter = alphabet[newPosition]
print('Le nouveau caractère est: ' + newCharacter)
