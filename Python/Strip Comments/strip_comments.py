'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:


result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''
def solution(string, special_characters):
    for line in string.split('\n'):
        for character in special_characters:
            if character in line:
                print(line.split(character)[0])

def main():
    solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    solution("a #b\nc\nd $e f g", ["#", "$"])

if __name__ == '__main__':
    main()