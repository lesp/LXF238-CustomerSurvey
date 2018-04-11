import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import time

happy = 0
unhappy = 0


happy = int(input("Happy Stats"))
unhappy = int(input("Unhappy Stats"))
 
objects = ('Happy', 'Unhappy')
y_pos = np.arange(len(objects))
satisfaction = [happy,unhappy]
 
plt.bar(y_pos, satisfaction, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('No. of people')
plt.title('Satisfaction')
plt.savefig(str(time.ctime())+'.png') 
plt.show()

