import time
import sys

currentTemperature = 100  # Reads current temperature from temp sensor
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
