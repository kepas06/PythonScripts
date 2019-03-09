# import os
# from os import listdir
# from os.path import isfile, join

# dir_list = next(os.walk('/home/lukasz'))[1]

# exact_list = [ x[0] for x in os.walk('/home/lukasz/Python/PythonScripts')]
# onlyfiles = [f for f in '/home/lukasz/Python/PythonScripts' if isfile(join('/home/lukasz/Python/PythonScripts', f))]
# print(onlyfiles)
import os

for path, subdirs, files in os.walk("/home/lukasz/Python/PythonScripts"):
    for name in files:
        print os.path.join(path, name)