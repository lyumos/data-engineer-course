if __name__ == "__main__":
    while True:
        phrase = input('Введите фразу: ')
        if phrase.replace(' ','') == phrase[::-1].replace(' ',''):
            print(f'"{phrase}" является палиндромом!')
        else:
            print(f'"{phrase}" не является палиндромом!')

