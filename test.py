from string_operations import split_duets

x = ['szm123_11mnw', 'szm1711mnw,szm1527mnw(1).jpg']

y = list(filter(split_duets, x))
print(y)


if __name__ == '__main__':
    pass