#2019-02-28
#Christophe Roux

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3

character = input('Veuillez entrer un clé: ')
position = alphabet.find(character)
print(position)

newPosition = (position + key) % 26
print(newPosition)

newCharacter = alphabet[newPosition]
print(newCharacter)
