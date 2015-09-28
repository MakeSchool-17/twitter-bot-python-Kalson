import random
import sys

if __name__ == '__main__':
    new_arrangement = sys.argv[1:]
    random.shuffle(new_arrangement)
    print(new_arrangement)
