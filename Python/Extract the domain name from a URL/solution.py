import re

def domain_name(url):
    pattern = r'^(http(s)?://)?(www\.)?(.+?)\.'
    try:
        found = re.search(pattern, url).groups()
    except AttributeError:
        found = ''
    print(found[-1])
    return(found[-1])

def main():
    domain_name("http://google.com")
    domain_name("http://google.co.jp")
    domain_name("www.xakep.ru")
    domain_name("https://youtube.com")

if __name__ == '__main__':
    main()