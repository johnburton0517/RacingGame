def redWinIncrease():

    with open('store.txt', 'r') as file:
        data = file.readlines()

    count = data[1]
    intCount = int(count)

    # increase count by 1
    intCount = intCount + 1
    count = str(intCount)
    count = count + '\n'

    data[1] = count

    with open('store.txt', 'w') as file:
        file.writelines(data)


def blueIncrease():

    with open('store.txt', 'r') as file:
        data = file.readlines()

    count = data[3]
    intCount = int(count)

    # increase count by 1
    intCount = intCount + 1
    count = str(intCount)
    count = count + '\n'

    data[3] = count

    with open('store.txt', 'w') as file:
        file.writelines(data)


def greenIncrease():

    with open('store.txt', 'r') as file:
        data = file.readlines()

    count = data[5]
    intCount = int(count)

    # increase count by 1
    intCount = intCount + 1
    count = str(intCount)
    count = count + '\n'

    data[5] = count

    with open('store.txt', 'w') as file:
        file.writelines(data)



def getRedWins():
    file = open('store.txt', 'r')

    # get count from file
    for i in range(2):
        count = file.readline()
    intCount = int(count)

    file.close()

    return intCount

def getBlueWins():
    file = open('store.txt', 'r')

    # get count from file
    for i in range(4):
        count = file.readline()
    intCount = int(count)

    file.close()

    return intCount

def getGreenWins():
    file = open('store.txt', 'r')

    # get count from file
    for i in range(6):
        count = file.readline()
    intCount = int(count)

    file.close()

    return intCount