with open('1.txt', encoding="utf-8") as f:
    lines = f.readlines()
    print(type(lines))
    print(len(lines))
    for line in lines:
        print(line, end="")

with open('2.txt', encoding="utf-8") as f:
    lines = f.readlines()
    print(type(lines))
    print(len(lines))
    print(lines)

with open('3.txt', encoding="utf-8") as f:
    lines = f.readlines()
    print(type(lines))
    print(len(lines))
    print(lines)


with open('result.txt', 'w') as f:
    f.write('2.txt\n')
    with open('2.txt') as content:
        lines = content.readlines()
        f.write(str(len(lines)))
        f.write('\n')
        for line in lines:
            f.write(line)
        f.write('\n')

    f.write('1.txt\n')
    with open('1.txt') as content:
        lines = content.readlines()
        f.write(str(len(lines)))
        f.write('\n')
        for line in lines:
            f.write(line)
        f.write('\n')
            
    f.write('3.txt\n')
    with open('3.txt') as content:
        lines = content.readlines()
        f.write(str(len(lines)))
        f.write('\n')
        for line in lines:
            f.write(line)
