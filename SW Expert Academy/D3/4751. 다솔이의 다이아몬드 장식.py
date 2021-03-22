tc = int(input())
for t in range(tc):
    sample = input()
    row = ['..#..','.#.#.','#.'+sample+'.#']


    if len(sample) == 1:
        for i in range(len(row)):
            print(row[i])
        for i in range(len(row)-2, -1, -1):
            print(row[i])
    else:
        s = sample[0]
        row = ['..#..', '.#.#.', '#.' + s + '.#']
        for i in range(3):
            print(row[i], end='')
            for k in range(1, len(sample)-1):
                splus = sample[k]
                row_plus = ['.#..', '#.#.', '.' + splus + '.#', '#.#.', '.#..']
                print(row_plus[i],end='')
            splus = sample[-1]
            row_plus = ['.#..', '#.#.', '.' + splus + '.#', '#.#.', '.#..']
            print(row_plus[i])

        for i in range(len(row) - 2, -1, -1):
            print(row[i], end='')
            for k in range(len(sample)-1):
                print(row_plus[i],end='')
            print()