# ----------------------------------------------------- #
# Step through a current working directory for a string #
# ----------------------------------------------------- #

import os
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".m"):
            print(os.path.join(root,file))
