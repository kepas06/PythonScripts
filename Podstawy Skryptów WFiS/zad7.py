from datetime import date

def numOfDays():
    """ counting number of days with distracting one date from another """

    print("Podaj rok, miesiac oraz dzien pierwszej daty: ")
    inputs = [input() for i in range(3)]

    print("Podaj rok, miesiac oraz dzien drugiej daty: ")
    inputs1 = [input() for i in range(3)]

    d0 = date(inputs[0], inputs[1], inputs[2])
    d1 = date(inputs1[0], inputs1[1], inputs1[2])
    delta = abs(d1 - d0)
    
    print(delta.days)
    return abs(delta.days)

if __name__ == '__main__':
    numOfDays()
