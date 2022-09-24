if __name__ == "__main__":
    while True:
        n = input('Введите строку со скобками: ')
        count1 = count2 = count3 = 0
        for element in n:
            if element == '(' or element == ')':
                count1 += 1
            if element == '[' or element == ']':
                count2 += 1
            if element == '{' or element == '}':
                count3 += 1
        if count1 % 2 == count2 % 2 == count3 % 2 == 0:
            print(True)
        else:
            print(False)
