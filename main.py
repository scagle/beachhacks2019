import mraa

mraa.init()
print(mraa.getPinCount()) 
print(mraa.getVersion())
print("Raw adc bits: " + str(mraa.adcRawBits()))
print("Support adc bits: " + str(mraa.adcSupportedBits()))
count = 0
while (count < 100):  
    try:
        #There is no adcs on this dragonboard. wtf!! even from 0 to 100
        print("Reading I2c" + str(count))
        port = mraa.I2c(count)
        print("Trying to read I2c" + str(count))
        port.dir(mraa.DIR_IN);
        a = port.read(count);
        
        if (a/255 * 100 > 90) :
            pass      #BOTTLE IF FULL
        elif (a/255 * 100  < 50) :
            pass     #BOTTLE IS HALF FULL
        elif (a/255 * 100  <25) :
            pass         #YOU MIGHT WANNA CONSIDER REFILL THE MEDICINE
        elif (a/255 * 100  <10) :
            pass  #TIME TO GO GET MEDICATION
        print("Got a I2c" + str(count) + " of " + str(a))
    except:
        print("Are you sure you have an I2c" + str(count))
    count = count + 1
