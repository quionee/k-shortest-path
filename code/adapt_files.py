import os 

instancesList = os.listdir('../original_instances/')

for element in instancesList:
    newFile = open('../updated_instances/' + element, 'w')
    firstLine = -1

    with open('../original_instances/' + element) as file:
        content = file.readlines()
        firstLine = content[0]
        firstElement = int(firstLine.split(' ')[1]) + 3
        content = content[firstElement:]
        newFile.write(firstLine[1:])
        
        for line in content:
            line = line.split(' ')
            newFile.write(' '.join([line[1], line[2], line[3]]) + '\n')

    newFile.close()
