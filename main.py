import time, os

from colorama import init, Fore, Back, Style

# Initialize colorama
init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#------------FUNKCE-----------------
def tiskPod (number , string ,forSegment):
  #int (number) na string aby fungoval cyklus a přiřadí se string na int pole (forSegment)
  for items in string:
    forSegment.append(int(items))

  #int forSegment itemy se čtou aby vytisknuly čísla na konzoli
  for y in forSegment:
    for x in globals()['n' + str(y)]:
          print(x)

def tiskHori(number):

    forSegment = []

    #rozdeleni inputu na pole aby se vytisknulo jednotlive cislo
    for items in number:
          forSegment.append(items) #1,2,3,4...

    #tisk horizontalne
    for z in range(3):
        for segItem in forSegment:
               if segItem == 'D':
                    print(D[z], end="")
               elif segItem != 'D' :
                    print(globals()['n' + str(segItem)][z], end=" ")#n(cislo z segItemu)[z]  tisk,
            #print(len(forSegment), end="")
        print("")



#-----------konec funkci------------------
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
     
D   =['   ',
      ' ▀ ',
      ' ▀ '] 
#-----------------------------------------------

# Set text color to green and background color to yellow
print(Fore.RED + Back.BLACK)



# Define the duration of the timer in seconds
duration = 300 #5minut

# Start the timer
start_time = time.time()

# Loop until the timer is done
while True:
    # Calculate the time elapsed since the timer started
    elapsed_time = time.time() - start_time

    # Calculate the minutes, seconds, and milliseconds from the elapsed time
    minutes = int(elapsed_time / 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time % 1) * 1000)
    milliseconds = int(milliseconds / 10)

    if minutes==None:
     minutes = "0"
    
    if seconds==None:
     seconds = "00"
    elif seconds <10:
     seconds = "0" + str(seconds)
    
    if milliseconds == 0:
     milliseconds = "00"

    my_string = "{}{}{}{}{}".format(minutes,"D",seconds,"D",milliseconds)
    # Display the timer in the format "minutes : seconds : milliseconds"
    tiskHori(my_string)

    # If the timer is done, break out of the loop
    if elapsed_time >= duration:
        break

    # Wait for a short period to avoid using too much CPU time
    time.sleep(0.01)
    clear_console()


print(Style.RESET_ALL +"----------------------------------------")
exit("---\nkonec programu\n---")
