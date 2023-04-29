#Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
word = 'one'
phrase = 'onetwonine'

for el in word:
    count = 0
    for letter in phrase:
        if letter == el:
            count +- 1
    print(f'{el} - {count}')
