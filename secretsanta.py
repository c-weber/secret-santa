import random


def randomize(names):
    nametuples = []
    chosennames = []
    chosenpartners = []
    while len(chosennames) != len(names) and len(chosennames) != len(names):
        index = random.randint(0, len(names)-1)
        firstname = names[index]
        if chosennames.__contains__(firstname):
            while chosennames.__contains__(firstname):
                index = random.randint(0, len(names) - 1)
                firstname = names[index]
        chosennames.append(firstname)
        secondname = names[random.randint(0, len(names)-1)]
        if chosenpartners.__contains__(secondname) or secondname == firstname:
            while chosenpartners.__contains__(secondname) or secondname == firstname:
                index = random.randint(0, len(names) - 1)
                secondname = names[index]
        chosenpartners.append(secondname)
        nametuple = (firstname, secondname)
        nametuples.append(nametuple)
    return nametuples


if __name__ == '__main__':
    names = input("Bitte Namen mit Komma getrennt einfuegen: \n").split(',')
    randomizedNames = randomize(names)
    for nametuple in randomizedNames:
        print(f'{nametuple[0]} beschenkt {nametuple[1]}')

