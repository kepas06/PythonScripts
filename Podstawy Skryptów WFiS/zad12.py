# import os
# lst = [x[0] for x in os.walk("/home/Python")]

# print(lst)

import os

dir_list = next(os.walk('/home/lukasz'))[1]

print(dir_list)