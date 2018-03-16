# Import Libraries
import os
import glob
import time
import sys

# Initialize the GPIO Pins
os.system('modprobe w1-gpio')  # Turns on the GPIO module
os.system('modprobe w1-therm')  # Turns on the Temperature module

# Finds the correct device file that holds the temperature data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# A function that reads the sensor data
def read_temp_raw():
    f = open(device_file, 'r')  # Opens the temperature device file
    lines = f.readlines()  # Returns the next
    f.close()
    return lines

# Convert the value of the sensor into a temperature
def read_temp():
    lines = read_temp_raw()  # Read the temperature 'device file'

    # While the first line does not contain 'YES', wait for 0.2s
    # and then read the device file again.
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

        # Look for the position of the '=' in the second ine of the
        # device file.
        equals_pos = lines[1].find('t')

        # if the '=' is found, convert the rest of the line after the
        # '=' into degrees Celsius, then degrees Fahrenheit
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_f



currentTemperature = print(read_temp())  # Reads current temperature from temp sensor
pumpOn = 1  # Code to turn pump on
pumpOff = 0  # Code to turn pum off
dropinterval = 9
print(currentTemperature)


def tempsetting0():
    print("tempSetting0 Code runs now")
    pulseduration = 2
    count = 0

    while count < dropinterval:
        print("The count is: ", count)
        count = count + 1
        time.sleep(1)
    print(pulseduration)
    return


if currentTemperature < 32:
    print("Temperature is less then 32")
elif 32 <= currentTemperature < 50:
    print("Current temperature is 32-50")
elif 50 <= currentTemperature < 80:
    print("Current temperature is 50-80")
elif 80 <= currentTemperature < 100:
    print("Current temperature is 80-100")
elif currentTemperature >= 100:
    print("Current temperature is above 100")
    tempsetting0()

sys.exit()
