import time, os, threading
from playsound import playsound
from colorama import init, Fore, Back, Style
# Initialize colorama
init()


#-----------BARVY FUNKCE----------------------
def yellow_txt():
    return Fore.YELLOW

def red_txt():
    return Fore.RED

def red_bck():
     return Back.RED

def reset_txt():
    return Fore.RESET + Back.RESET

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# █▒█▒█▒█
#------------FUNKCE-----------------

def tiskHori(number,red,internal):

    forSegment = []

    #rozdeleni inputu na pole aby se vytisknulo jednotlive cislo
    for items in number:
          forSegment.append(items) #1,2,3,4...vBbbBfbvcBVcbvbcv
    #tisk horizontalne
    for z in range(3):
        for segItem in forSegment:
               if segItem == 'D':
                    print(D[z], end="")
               elif segItem == 'E':
                    if internal == True and z == 0:
                         for x in E[z]:
                              for y in x:
                                   if y == '█' or y == '▒':
                                        print(red_txt() + y + reset_txt(),end="")
                                   else:
                                        print(y,end="")
                    else:
                         print(E[z], end="")
               elif segItem == 'L':
                    print(L[z], end="")
               elif segItem == 'Z':
                    print(Z[z], end="")
               elif segItem != 'D' or segItem != 'E' or segItem!= 'L' or segItem!='Z':
                    if red == True:
                         print(red_txt(),end="")
                    print((globals()['n' + str(segItem)][z]) + reset_txt(), end=" ")#n(cislo z segItemu)[z]  tisk,

        print("")



#-----------PAMĚŤ ČÍSEL A UI------------------
n0 =['█▀█',
     '█ █',
     '█▄█' ]

n1 =['■█ ',
     ' █ ',
     '▄█▄'] 

n2 =['█▀█',
     '▄■▀',
     '█▄▄'] 

n3 =['▀▀█',
     ' ■█',
     '▄▄█'] 

n4 =['█ █',
     '▀■█',
     '  █'] 

n5 =['█▀▀',
     '▀■▄',
     '▄▄█'] 

n6 =['█▀█',
     '█■▄',
     '█▄█']

n7 =['█▀█',
     '  █', 
     '  █']

n8 =['█▀█',
     '█■█',
     '█▄█']

n9 =['█▀█',
     '▀▀█',
     '▄▄█'] 
     
D  =['    ',
     ' ▀  ',
     ' ▀  '] 

E = ['║ 内部 internal  ██████     ║',
     '╠═══════════════════════════╣',
     '║ 主なエネルギー供給システム║',]

L = ['║ ',
      '║ ',
      '║ ']

Z = ['    ',
     '    ',
     '    ']
#-----------------------------------------------



#------------PROMĚNNÝ--------------------------

blik = False
red = False

# Define the duration of the timer in seconds
duration = int(input("Enter time(between 1 - 300):")) #čas
if duration > 300 or duration <= 0:
     print("please enter value between 1 to 300 seconds !")
     duration = int(input("Enter time(between 1 - 300):")) #čas


#             stop slow  normal racing || internal external
timerState = [False,False,False,False,False,True]




#----------------------------------------------
# Start the timer
start_time = time.time()
timerState[0:3] = [False] * 3
timerState[3:6] = [True, False, False]

# Loop until the timer is done
while True:
    # Calculate the time elapsed since the timer started
    remaining_time = duration - (time.time() - start_time)

    if remaining_time < 0:
        remaining_time = 0

    # Calculate the minutes, seconds, and milliseconds from the elapsed time
    minutes = int(remaining_time / 60)
    seconds = int(remaining_time % 60)
    milliseconds = int((remaining_time % 1) * 1000)
    milliseconds = int(milliseconds / 10)

    if minutes==None or minutes <1:
     minutes = "0"
     red = True
    
    if seconds==None:
     seconds = "00"
    elif seconds <10:
     seconds = "0" + str(seconds)
    
    if milliseconds == 0:
     milliseconds = "00"
    elif milliseconds <10:
     milliseconds = "0" + str(milliseconds)

    final = "{}{}{}{}{}{}{}".format('L',minutes,"D",seconds,"D",milliseconds,"E")
    # Display the timer in the format "minutes : seconds : milliseconds"

    #------------print section-------------------
    print("╔═══════════════════════════════════════╗")
    print("║ 活動限界まで  active time remaining   ║")
    print("╠═════════════════════════════╦═════════╩═════════════════╗")
    tiskHori(final,red,timerState[3])
    print("╠═════════════════════════════╣ main energy supply system ║")
    print("║ STOP   SLOW  NORMAL  RACING ╠═══════════════════════════╣")
    print("║ " + (red_txt() if timerState[0]== True else reset_txt()) + "████   " + (red_txt() if timerState[1]== True else reset_txt()) + "████   " + (red_txt() if timerState[2]== True else reset_txt()) + "████    " + (red_txt() if timerState[3]== True else reset_txt()) + "████  " + reset_txt() + "║ 外部 external  "+ (red_txt() if timerState[5]== True else reset_txt()) + "██████" + reset_txt() + "     ║")
    print("╚═════════════════════════════╩═══════════════════════════╝")
    if milliseconds == 99:
     playsound(r"C:/Users/bruno/Desktop/Docs/evangelion-timer-UI-python-/sounds/beep.mp3")
    elif milliseconds == 1:
     playsound(None)
    # If the timer is done, break out of the loop
    if remaining_time == 0:
        break

    # Wait for a short period to avoid using too much CPU time
    time.sleep(0.01)
    clear_console()
#---------------------------------------------------------
timerState[0] = True
#---------------------------------------------------------
while True:
     time.sleep(0.3)
     if blik == True:
          final = "{}{}{}{}{}{}{}".format('L',minutes,"D",seconds,"D",milliseconds,"E")
          blik = False
          ATR = '活動限界まで  active time remaining'
          timerState[3] = True
     elif blik == False:
          final = "{}{}{}{}{}{}{}".format('L',"Z","D","ZZ","D","ZZ","E")
          blik = True
          ATR = "                                   "
          timerState[3] = False
     
     clear_console()
     print("╔═══════════════════════════════════════╗")
     print("║ "+ ATR + "   ║")
     print("╠═════════════════════════════╦═════════╩═════════════════╗")
     tiskHori(final,red,timerState[3])
     print("╠═════════════════════════════╣ main energy supply system ║")
     print("║ STOP   SLOW  NORMAL  RACING ╠═══════════════════════════╣")
     print("║ " + (red_txt() if timerState[0]== True else reset_txt()) + "████   " + (red_txt() if timerState[1]== True else reset_txt()) + "████   " + (red_txt() if timerState[2]== True else reset_txt()) + "████    " + (red_txt() if timerState[3]== True else reset_txt()) + "████  " + reset_txt() + "║ 外部 external  "+ (red_txt() if timerState[5]== True else reset_txt()) + "██████" + reset_txt() + "     ║")
     print("╚═════════════════════════════╩═══════════════════════════╝")
     time.sleep(0.01)


print(Style.RESET_ALL +"----------------------------------------")


# dej barvy do metod aby jsi je mohl vložit mezi text v printu !!! !!! !!!