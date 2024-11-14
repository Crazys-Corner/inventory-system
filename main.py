print('Starting App')


import database 
import homepage
import time

database.init()

print("""
.___              _____                 
|   | _______  __/     \ _____    ____  
|   |/    \  \/ /  \ /  \\__  \  /    \ 
|   |   |  \   /    Y    \/ __ \|   |  \\
|___|___|  /\_/\____|__  (____  /___|  /
         \/            \/     \/     \/
""")

print('App Started! Continuing in 5 seconds')
#time.sleep(5)

homepage.homepage()
