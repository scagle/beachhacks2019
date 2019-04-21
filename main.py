from pdb import set_trace # for debugging
import mraa               # for GPIO

gpio_1 = mraa.Gpio(23)  # Enable GPIO23
gpio_1.dir(mraa.DIR_IN) # Set GPIO23 as Input

