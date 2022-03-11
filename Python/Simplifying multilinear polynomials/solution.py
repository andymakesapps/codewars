import re

def simplify(poly):
    poly_dict = {}
    print(poly)
    pattern = r'[-]?[\d+]?\w+'
    poly_matches = re.findall(pattern, poly)
    print(poly_matches)
    for match in poly_matches:
        match_list = break_up_poly(match)
        match_symbol = match_list[0]
        match_unit = match_list[1]
        if match_symbol in poly_dict:
            poly_dict[match_symbol] = poly_dict[match_symbol] + match_unit
        else:
            poly_dict[match_symbol] = match_unit
    print(poly_dict)
    #TODO: Transform dict intro string - new function ?

def break_up_poly(poly_unit):
    unit_value = 1
    if poly_unit[0] == '-':
        unit_value = -1
    if poly_unit[0] == '-' or poly_unit[0] == '+':
        poly_unit = poly_unit[1:]
    
    pattern = '([\d+]?)(\w+)'
    poly_matches = re.match(pattern, poly_unit)
    poly_matches_list = list((poly_matches.groups()))
    print(poly_matches_list)
    if poly_matches_list[0] == '':
        poly_matches_list[0] = '1'
    unit_symbol = "".join(sorted(poly_matches_list[1]))
    unit_value = unit_value * int(poly_matches_list[0])
    return [unit_symbol, unit_value]

def main():
    poly1 = "dc+dcba"
    poly2 = "2xy-yx"
    poly3 = "-a+5ab+3a-c-2a"
    poly4 = "-abc+3a+2ac"
    
    simplify(poly3)

if __name__ == '__main__':
    main()