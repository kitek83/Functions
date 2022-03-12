#zig_zag
"""Small animation program. This program will create back-and-forth, zigzag pattern until
the user sops it pressing any keyboard button or ctrl+c"""

import sys, time

ident = 0
identIncreasing = True  #using a flag identIncresing, which is set to True, so the program will run continously
                        #untill the type of event makes it False.

try:    #using try-except statement to catch KeyboardInterrupt exception
    while True:             #infinite loop - while statement
        print(' '*ident, end='')
        print('********')
        time.sleep(0.1) #Pause for 1/10th second

        #using nested if condtional statement
        if identIncreasing:     #it means that is True
            ident += 1
            if ident == 20:
                #change directions
                identIncreasing = False
        else:               #flag is False and program will run untill the flag is True
            ident -= 1
            if ident == 0:
                #change direction
                identIncreasing = True

except KeyboardInterrupt:
    sys.exit()

"""out:
********
 ********
  ********
   ********
    ********
     ********
      ********
       ********
        ********
         ********
          ********
           ********
            ********
             ********
              ********
               ********
                ********
                 ********
                  ********
                   ********
                    ********
                   ********
                  ********
                 ********
                ********
               ********
              ********
             ********
            ********
           ********
          ********
         ********
        ********
       ********
      ********
     ********
    ********
   ********
  ********
 ********
********
 ********
  ********
   ********
    ********
     ********
      ********
       ********
        ********
         ********
          ********
           ********
            ********
             ********
              ********
               ********
                ********
                 ********
                  ********
                   ********
                    ******** - ctrl+c
"""


