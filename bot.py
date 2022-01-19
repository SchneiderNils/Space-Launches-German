#####################################
#                                   #
#       Version: v1.0.0             #
#       Creater: Nils Schneider     #
#                                   #
#       Bearbeitet: 18.01.2022      #
#           ToDo Liste:             #
#      https://orburl.de/6UHi3H     #
#                                   #
#####################################
from api import *

while True:
    prüfung()
    senden()
    print(f"{bcolors.HEADER}Nächste Prüfung in 10 Minuten!{bcolors.ENDC}")
    time.sleep(300)
    print(f"{bcolors.HEADER}Nächste Prüfung in 5 Minuten!{bcolors.ENDC}")
    time.sleep(240)
    print(f"{bcolors.HEADER}Nächste Prüfung in 1 Minuten!{bcolors.ENDC}")
    time.sleep(50)
    print(f"{bcolors.HEADER}Nächste Prüfung in 10 Sekunden!{bcolors.ENDC}")
    print(bcolors.LINE)
    time.sleep(10)
    print("\n\n\n\n\n")
