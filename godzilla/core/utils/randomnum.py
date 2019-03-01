
import random
import  string


def randomnumutil():
    num = "1" + "".join(map(lambda x: random.choice(string.digits), range(7)))

    return num


if __name__ == '__main__':
    print(randomnumutil())