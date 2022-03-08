from numpy import poly1d


import re
def simplify(poly):
    pattern = r'([+\-]?)(\d*)([a-z]+)'
    matches = re.findall(pattern, poly)
    for match in matches:
        if match[1] == '':
            match[1] = '1'

def main():
    poly1 = "dc+dcba"
    poly2 = "2xy-yx"
    poly3 = "-a+5ab+3a-c-2a"
    poly4 = "-abc+3a+2ac"
    
    simplify(poly3)

if __name__ == '__main__':
    main()