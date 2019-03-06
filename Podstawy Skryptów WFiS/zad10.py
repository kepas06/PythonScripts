

dict_of_students = [("Asia Tomaszewska",4),("Michal Sadowski",3),("Kajetan Kajetanowicz",2),
    ("Marcin Czyzewski",2),("Cezary Pazura",4),("Marcin Gudowski",5),("Jarek Radas",4)]

def returnByCriteria(lst,num):
    lst = [(x[0],x[1]) for x in dict_of_students if x[1] == num]
    print(lst)

returnByCriteria(dict_of_students,4)

