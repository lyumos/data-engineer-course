if __name__ == "__main__":
    units = ['',"I","II","III","IV","V","VI","VII","VIII","IX"]
    dozens = ['',"X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hundreds = ['',"C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thousands = ['',"M","MM"]
    while True:
        number = input('Введите число арабскими цифрами: ')
        roman_num = thousands[int(number) // 1000] + hundreds[int(number) % 1000 // 100] + dozens[int(number) % 100 // 10] + units[int(number) % 10]
        print(f'Это же число римскими цифрами: {roman_num}\n')
