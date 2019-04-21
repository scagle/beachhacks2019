port = mraa.Aio(0);
a = port.read();

if (a/255 > 90) 
     #BOTTLE IF FULL
     pass
elif (a/255 < 50) :
    pass
    #BOTTLE IS HALF FULL
elif (a/255 <25) :
    pass
        #YOU MIGHT WANNA CONSIDER REFILL THE MEDICINE

else (a/255 <10) 
pass
        #TIME TO GO GET MEDICATION
