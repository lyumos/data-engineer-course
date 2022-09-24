if __name__ == "__main__":
    first_num = int(input('Введите первое число: '),2)
    second_num = int(input('Введите второе число: '),2)
    mult = bin(first_num * second_num)
    print(f'Произведение этих чисел: {mult[2:]}')