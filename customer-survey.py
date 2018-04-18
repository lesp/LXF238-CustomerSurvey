import matplotlib.pyplot as plt
import numpy as np
import time
from gpiozero import Button

#Buttons
yes = Button(17)
no = Button(27)
stats = Button(22)

#Reset Counters
happy = 0
unhappy = 0

print("Did you enjoy the event today? Press Green for Yes, Red for No")

while True:
    if yes.is_pressed:
        happy += 1
        print("Happy",str(happy))
        time.sleep(1)
    elif no.is_pressed:
        unhappy += 1
        print("Unhappy",str(unhappy))
        time.sleep(1)
    elif stats.is_pressed:
        objects = ('Happy', 'Unhappy')
        y_pos = np.arange(len(objects))
        satisfaction = [happy,unhappy]
        plt.bar(y_pos, satisfaction, align='center', alpha=1)
        plt.xticks(y_pos, objects)
        plt.ylabel('No. of people')
        plt.title('Satisfaction')
        plt.savefig(str(time.ctime())+'.png') 
        plt.show()
        time.sleep(1)


