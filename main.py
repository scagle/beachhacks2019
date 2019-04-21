import mraa

count = 0
while (count < 100):  
    try:
        port = mraa.Aio(count);
        a = port.read();
        
        if (a/255 > 90) :
            pass      #BOTTLE IF FULL
        elif (a/255 < 50) :
            pass     #BOTTLE IS HALF FULL
        elif (a/255 <25) :
            pass         #YOU MIGHT WANNA CONSIDER REFILL THE MEDICINE
        elif (a/255 <10) :
            pass  #TIME TO GO GET MEDICATION
        print("Got a ADC" + str(count))
    except:
        print("Are you sure you have an ADC" + str(count))
    count = count + 1
