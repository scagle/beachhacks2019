port = mraa.Aio(0);
a = port.read();

if (a/255 > 90) {
     #BOTTLE IF FULL
}
elif (a/255 < 50) {
    #BOTTLE IS HALF FULL
}elif (a/255 <25) {
        #YOU MIGHT WANNA CONSIDER REFILL THE MEDICINE
}
else (a/255 <10) {
        #TIME TO GO GET MEDICATION
}