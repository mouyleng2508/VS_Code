LOWER_LETTERS = [chr(x) for x in range(97, 123)];
UPPER_LETTERS = [chr(x) for x in range(65, 91)];

def rot13():
    sourceString = input("Enter string to rot13:");
    resultString = "";
    for char in sourceString:
        if char.isupper():
            resultString += encrypt(char, UPPER_LETTERS);
        elif char.islower():
            resultString += encrypt(char, LOWER_LETTERS);
        else:
            resultString += char;
    print("The rot13 string is:%s" % (resultString));
            
def encrypt(char, letterList):
    resultchar = '';
    originalIndex = letterList.index(char)
    newIndex = originalIndex + 13
    resultchar += letterList[newIndex % len(letterList)]
    return resultchar
    
if __name__ == '__main__':
    rot13();