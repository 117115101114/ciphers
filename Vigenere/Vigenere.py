table = [
    'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.lower().split(' '),
    'B C D E F G H I J K L M N O P Q R S T U V W X Y Z A'.lower().split(' '),
    'C D E F G H I J K L M N O P Q R S T U V W X Y Z A B'.lower().split(' '),
    'D E F G H I J K L M N O P Q R S T U V W X Y Z A B C'.lower().split(' '),
    'E F G H I J K L M N O P Q R S T U V W X Y Z A B C D'.lower().split(' '),
    'F G H I J K L M N O P Q R S T U V W X Y Z A B C D E'.lower().split(' '),
    'G H I J K L M N O P Q R S T U V W X Y Z A B C D E F'.lower().split(' '),
    'H I J K L M N O P Q R S T U V W X Y Z A B C D E F G'.lower().split(' '),
    'I J K L M N O P Q R S T U V W X Y Z A B C D E F G H'.lower().split(' '),
    'J K L M N O P Q R S T U V W X Y Z A B C D E F G H I'.lower().split(' '),
    'K L M N O P Q R S T U V W X Y Z A B C D E F G H I J'.lower().split(' '),
    'L M N O P Q R S T U V W X Y Z A B C D E F G H I J K'.lower().split(' '),
    'M N O P Q R S T U V W X Y Z A B C D E F G H I J K L'.lower().split(' '),
    'N O P Q R S T U V W X Y Z A B C D E F G H I J K L M'.lower().split(' '),
    'O P Q R S T U V W X Y Z A B C D E F G H I J K L M N'.lower().split(' '),
    'P Q R S T U V W X Y Z A B C D E F G H I J K L M N O'.lower().split(' '),
    'Q R S T U V W X Y Z A B C D E F G H I J K L M N O P'.lower().split(' '),
    'R S T U V W X Y Z A B C D E F G H I J K L M N O P Q'.lower().split(' '),
    'S T U V W X Y Z A B C D E F G H I J K L M N O P Q R'.lower().split(' '),
    'T U V W X Y Z A B C D E F G H I J K L M N O P Q R S'.lower().split(' '),
    'U V W X Y Z A B C D E F G H I J K L M N O P Q R S T'.lower().split(' '),
    'V W X Y Z A B C D E F G H I J K L M N O P Q R S T U'.lower().split(' '),
    'W X Y Z A B C D E F G H I J K L M N O P Q R S T U V'.lower().split(' '),
    'X Y Z A B C D E F G H I J K L M N O P Q R S T U V W'.lower().split(' '),
    'Y Z A B C D E F G H I J K L M N O P Q R S T U V W X'.lower().split(' '),
    'Z A B C D E F G H I J K L M N O P Q R S T U V W X Y'.lower().split(' ')
]

#for x in range(len(table)):
#    for y in range(len(table[x])):
#        print(table[x][y], end='')
#    print()
keyLen = 100000000

def start():
    text = input('text:')
    key = input('key:')
    newString = ''
    key = key * keyLen

    deEn = input('do you want the encipher or decipher? (e/d)')
    print(main(text,key,deEn))
    input()


def main(text,key,deEn):
    global table
    newString = ''
    if deEn.lower() == 'e':
        for x in range(len(text)):
            crrt_key = key[x]
            crrt_text = text[x]
            if crrt_text == ' ':
                newString += ' '
            else:
                x = encipher(table,crrt_text,crrt_key)
                newString += x
    if deEn.lower() == 'd':
        for x in range(len(text)):
            crrt_key = key[x]
            crrt_text = text[x]
            if crrt_text == ' ':
                newString += ' '
            else:
                x = decipher(table,crrt_text,crrt_key)
                newString += x
    return newString


            
                
                


def encipher(table,text,key):
    tableLen = len(table) 
    for x in range(tableLen):
        check = table[x][0]
        kcheck = key[0]
        if check == kcheck:
            row = table[x]
            rowlen = len(row)

            for y in range(rowlen):
                toprow = table[0]
                kcheck2 = toprow[y]
                textLet = text[0]
                if kcheck2 == textLet:
                    column = y
                    entext = row[column]
                    return entext


            

def decipher(table,text,key):
    tableLen = len(table) 
    for x in range(tableLen):
        check = table[x][0]
        kcheck = key[0]
        if check == kcheck:
            row = table[x]
            rowlen = len(row)

            for y in range(rowlen):
                toprow = table[0]
                kcheck2 = row[y]
                textLet = text[0]
                if kcheck2 == textLet:
                    column = y
                    entext = toprow[column]
                    return entext













if __name__ == "__main__":
    start()
