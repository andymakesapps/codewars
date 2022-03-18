from typing import Type


def same_structure_as(original,other):
    if len(original) != len(other):
        return False
    for i, j in zip(original, other):
        if type(i) != type(j):
            return False
        if type(i) is list and type(j) is list:
            if not same_structure_as(i, j):
                return False
    return True

def main():
    print(same_structure_as([1,[[1, 1],1]],[2,[[2, 2],2]]))
    print(same_structure_as([1,[1,1]],[[2,2],2]))

if __name__ == '__main__':
    main()