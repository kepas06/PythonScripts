import os

for path, subdirs, files in os.walk("/home/lukasz/Python/PythonScripts"):
    for name in files:
        print os.path.join(path, name)