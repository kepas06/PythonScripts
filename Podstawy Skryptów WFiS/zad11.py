import os

def goingTroughTheDirectory(directory,pattern):
    lst = []

    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.txt'): 
                if pattern in open(filename).read():
                    lst.append(filename)

    print(lst)

goingTroughTheDirectory("/home/lukasz/Python/",'program')
            
    
