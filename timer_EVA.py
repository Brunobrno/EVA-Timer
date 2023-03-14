import time, os

from colorama import init, Fore, Back, Style
# Initialize colorama
init()


#-----------BARVY FUNKCE----------------------
def yellow_txt():
    print(Fore.YELLOW, end='')

def red_txt():
    print(Fore.RED, end='')

def reset_txt():
    print(Fore.RESET, end='')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


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
                                   if y == '▒':
                                        red_txt()
                                        print(y,end="")
                                        reset_txt()
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
                         red_txt()
                    print(() + (globals()['n' + str(segItem)][z]), end=" ")#n(cislo z segItemu)[z]  tisk,
                    reset_txt()

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

E = ['║内部 internal  ▒▒▒▒▒▒      ║',
     '╠═══════════════════════════╣',
     '║ 主なエネルギー供給システム║',]

L = ['║ ',
      '║ ',
      '║ ']

Z = ['    ',
     '    ',
     '    ']
#-----------------------------------------------

blik = False
red = False

# Set text color to green and background color to yellow
print(Fore.YELLOW + Back.BLACK)


# Define the duration of the timer in seconds
duration = 70 #5minut



# Start the timer
start_time = time.time()
internal = True
external = False


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
    print("╔═══════════════════════════════════════╗")
    print("║ 活動限界まで  active time remaining   ║")
    print("╠═════════════════════════════╦═════════╩═════════════════╗")
    tiskHori(final,red,internal)
    print("╠═════════════════════════════╣ main energy supply system ║")
    print("║                             ╠═══════════════════════════╣")
    print("║                             ║外部 external  ▒▒▒▒▒▒      ║")
    print("╚═════════════════════════════╩═══════════════════════════╝")
    # If the timer is done, break out of the loop
    if remaining_time == 0:
        break

    # Wait for a short period to avoid using too much CPU time
    time.sleep(0.01)
    clear_console()

while True:
     time.sleep(0.3)
     if blik == True:
          final = "{}{}{}{}{}{}{}".format('L',minutes,"D",seconds,"D",milliseconds,"E")
          blik = False
          ATR = '活動限界まで  active time remaining'
          internal = True
     elif blik == False:
          final = "{}{}{}{}{}{}{}".format('L',"Z","D","ZZ","D","ZZ","E")
          blik = True
          ATR = "                                   "
          internal = False
     
     clear_console()
     print("╔═══════════════════════════════════════╗")
     print("║ "+ ATR + "   ║")
     print("╠═════════════════════════════╦═════════╩═════════════════╗")
     tiskHori(final,red,internal)
     print("╠═════════════════════════════╣ main energy supply system ║")
     print("║                             ╠═══════════════════════════╣")
     print("║                             ║外部 external  ▒▒▒▒▒▒      ║")
     print("╚═════════════════════════════╩═══════════════════════════╝")
     time.sleep(0.01)


print(Style.RESET_ALL +"----------------------------------------")


# dej barvy do metod aby jsi je mohl vložit mezi text v printu !!! !!! !!!