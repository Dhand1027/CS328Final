from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['lines.linewidth'] = 1



fig = plt.figure()
fig2 = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ab = fig2.add_subplot(111, projection='3d')

data = np.array([])
data_file = "\Users\Dylan\Desktop\data3.csv"
data_for_current_speaker = np.genfromtxt(data_file, delimiter=',')
#print data_for_current_speaker
x = np.empty([])
y = np.empty([])
z = np.empty([])

hX = 42.38960413
hY = -72.52782467
hZ = 999.7586
x = np.append(x, hX)
y = np.append(y, hY)
#z = np.append(z, hZ)

#print "size", data_for_current_speaker.size
for i in range(0,data_for_current_speaker.size/8):
    x = np.append(x,data_for_current_speaker[i][0])
    y = np.append(y,data_for_current_speaker[i][1])


normal = x[1]
normalY = y[1]
for i in range(0,data_for_current_speaker.size/8):
    x[i] = (x[i] - normal)*1000
    y[i] = (y[i] - normalY) * 1000

deltaX = np.array([])
deltaY = np.array([])
deltaX = np.append(deltaX,0)
deltaY = np.append(deltaY,0)

for i in range(1,data_for_current_speaker.size/8):
    z = np.append(z, data_for_current_speaker[i][0])
    diffX = abs(x[i+1]-x[i])
    if diffX > 1:
        deltaX = np.append(deltaX,deltaX[i-1])
    else:
        deltaX = np.append(deltaX,x[i])

    diffY = abs(y[i+1]-y[i])
    if diffY > 1:
        deltaY = np.append(deltaY,deltaY[i-1])
    else:
        deltaY = np.append(deltaY,y[i])



print "BREAK"
print deltaX
print deltaY
print z.size

ax.plot(deltaX, deltaY, z, c='r', marker='', color='green')
ax.set_title('Delta Values')
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Pressure (atm)')

#plt.show()



avgX = np.array([])
avgY = np.array([])

z = np.array([])
for i in range(1,data_for_current_speaker.size/8):
    aX = (deltaX[i-1]+deltaX[i])/2
    aY = (deltaY[i-1]+deltaY[i])/2

    avgX = np.append(avgX, aX)
    avgY = np.append(avgY, aY)
    z = np.append(z, data_for_current_speaker[i][0])


print "BREAK"
print avgX.size
print avgY.size
print z.size
ab.plot(avgX, avgY, z, c='r', marker='', color='blue')
ab.set_title('Average Values')
ab.set_xlabel('Latitude')
ab.set_ylabel('Longitude')
ab.set_zlabel('Pressure (atm)')

plt.show()




