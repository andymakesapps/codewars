import re

def alphanumeric(password):
    return password.isalnum()
    
    regex_exp = "[a-zA-Z0-9]"
    regex_check = re.search(regex_exp, password)
    if regex_check:
        return True
    else:
        return False

def main():
    print(alphanumeric("hello world_"))
    print(alphanumeric("PassW0rd"))
    print(alphanumeric("     "))

if __name__ == '__main__':
    main()