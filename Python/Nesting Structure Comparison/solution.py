def same_structure_as(original,other):
    for i in range(0, len(original)):
        print(len(original[i])==len(other[i]))

def main():
    print(same_structure_as([1,[1,1]],[2,[2,2]]))
    print(same_structure_as([1,[1,1]],[[2,2],2]))

if __name__ == '__main__':
    main()