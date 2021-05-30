import re

def alphanumeric(password):
    regex_exp = "[a-zA-Z0-9]"
    regex_check = re.search(regex_exp, password)
    if regex_check:
        return True
    else:
        return False

def main():
    print(alphanumeric("hello world"))
    print(alphanumeric("PassW0rd"))
    print(alphanumeric("     "))

if __name__ == '__main__':
    main()