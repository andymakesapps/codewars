from operator import truediv


def scramble(s1, s2):
    '''
    for letter in s1:
        s2 = s2.replace(letter, '', 1)
    if s2 == '':
        return True
    else:
        return False
    '''
#Times out...
    for letter in set(s2):
        if s1.count(letter) < s2.count(letter):
            return False
    return True


def main():
    s1 = "rkqodlw" 
    s2 = "world"
    print(scramble(s1, s2))

if __name__ == '__main__':
    main()