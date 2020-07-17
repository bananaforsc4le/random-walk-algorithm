#Tugas mosi: Random Walk
#Naufal Zahid Yoga P - 1301170345 - IF4106

# 100 steps
# Arah: N,NE,SE,S,SW,W,NW
# Probabilitas sesuai dengan slide 07 di kumpulan slide pemsis

import random
import matplotlib.pyplot as plt

run = 10 #banyak run
steps = 100 #banyak step

r = 0
while r < run: # x dan y mulai dari 0
    x = 0
    y = 0
    x_plt = [] #array untuk simpan point x
    y_plt = [] #array untuk simpan point y
    x_plt.append(x)
    y_plt.append(y)
    i = 1
    while (i < steps):
        R = random.randint(0,steps) #Random nilai
        if 0 < R < 19: # Arah N
            y+=1
            x_plt.append(x)
            y_plt.append(y)
        elif 19 < R < 43: # Arah NE
            x+=1
            y+=1
            x_plt.append(x)
            y_plt.append(y)
        elif 43 < R < 60: # Arah E
            x+=1
            x_plt.append(x)
            y_plt.append(y)
        elif 60 < R < 70: # Arah SE
            x+=1
            y-=1
            x_plt.append(x)
            y_plt.append(y)
        elif 70 < R < 72: # Arah S
            y-=1
            x_plt.append(x)
            y_plt.append(y)
        elif 72 < R < 75: # Arah SW
            x-=1
            y-=1
            x_plt.append(x)
            y_plt.append(y)
        elif 75 < R < 85: # Arah W
            x-=1
            x_plt.append(x)
            y_plt.append(y)
        elif 85 < R < 100: # Arah NW
            x-=1
            y+=1
            x_plt.append(x)
            y_plt.append(y)
        elif R > steps:
            print("Error")
            break
        i+=1
    print("Run ke-",r+1)
    print("Titik X: ",x_plt)
    print("Titik Y: ",y_plt)
    a = str(r+1)
    lbl = 'Run ke-'+a
    fig, = plt.plot(x_plt,y_plt,label=lbl)
    plt.legend()
    #plt.show()
    r+=1

plt.xlabel('X Position')
plt.ylabel ('Y Position')
plt.show()




