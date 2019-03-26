def pitagoras(start, end):
    emptyLst = []
    for x in range(start, end):
        for y in range(start, end):
            for z in range(start, end):
                if x*x + y*y == z*z:
                    emptyLst.append((x,y,z))
    print(emptyLst)


if __name__ == '__main__':
    pitagoras(10,20)

