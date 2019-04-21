from pdb import set_trace # for debugging
import mraa               # for GPIO

print(mraa.getVersion())

try:
    x = mraa.Aio(0)
    print(x.read())
    print("%.f" % x.readFloat())
except:
    print("Couldn't find ADC!")

# ir1 = mraa.Gpio(28)       # Enable GPIO28
# ir1.dir(mraa.DIR_IN)      # Set GPIO28 as Input
