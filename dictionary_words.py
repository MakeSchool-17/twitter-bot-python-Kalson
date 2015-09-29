with open('/usr/share/dict/words') as openfile:
    for line in openfile:
        for part in line.split():
            if __name__ == '__main__':
                print(part)
