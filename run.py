import os
import sys
import re

args = ' '.join([str(elem) for elem in sys.argv[2:]])
print("Running: " + sys.argv[1] + " "+ args)
if sys.platform == "linux" or sys.platform == "linux2":
    #print("we are in linux")
    os.system(sys.argv[1] + " " + args)
else:
#    os.system("$(echo \"" + args + "\" | cat | sed -r 's~/cygdrive/(.)/(.*)~ \1\:/\2 ~g' | cat | sed 's~/~\\~g' | sed -r 's~^ (.*)~\1~g')")
    result1 = re.sub(r'/cygdrive/(.)/(.*)',r'\1:/\2',args)
    result2 = re.sub(r'/',r'\\',result1)
    #final_result = sys.argv[1] + " \"" + result2 + "\""
    print(sys.argv[1] + " " + result2)
    os.system(sys.argv[1] + " " + result2)
