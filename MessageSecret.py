#2019-02-28
#Christophe Roux

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3

character = input('Veuillez entrer un clé: ')

position = alphabet.find(character)

newPosition = (position + key) % 26

newCharacter = alphabet[newPosition]
print('Le nouveau caractère est: ' + newCharacter)
