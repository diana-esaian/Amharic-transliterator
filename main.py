dictionary = {}
latin = []
lines = []
column = []
strochka = []
output = ''

with open('amh.tsv', 'r') as csv_file:
    for line in csv_file:
        letters = line.split()
        letters = ''.join(letters)
        lines.append(letters)
    latin.append(lines[0])
    latin = latin[0]
    lines.remove(lines[0])

    for index in range(len(lines)):
        stroka = lines[index]
        if len(stroka) == 8:
            column.append(stroka[0])
            stroka = stroka.replace(stroka[0], "")
        else:
            column.append(stroka[0:2])
            stroka = stroka.replace(stroka[0:2], "")
        strochka.append(stroka)

    for index in range(len(column)):
        stepen = 0
        while stepen <= len(latin)-1:
            dictionary[strochka[index][stepen]] = column[index] + latin[stepen]
            stepen += 1

text = input()
for character in text:
    output = output + dictionary[character]
print(output)
