# group x and y detected in 1 graph

import serial
from time import sleep
from json import loads

from matplotlib import pyplot as plt

# Initialize plot
# create matplotlib figure and axes
fig, ax = plt.subplots()
line, = ax.plot([], [])
plt.ylabel("force")

# show the plot
plt.show(block=False)


ax.plot()

# Set the y-axis range
MAX_X = 300
ax.set_ylim(-20, 20)  # Set the maximum y-axis limit to 1
ax.set_xlim(0, MAX_X + MAX_X * 0.2)  # Set the maximum y-axis limit to 1
ax.get_xaxis().set_visible(False) # or -> ax.set_xticklabels([]) ## to hide x axis labels


x = list(range(MAX_X))
y = []

# initialize
BAUDRATE = 115200
serial_data = serial.Serial("com10", BAUDRATE)
sleep(1)

# when no data is passed
while serial_data.in_waiting == 0:
    pass

# waiting for setup to finish
while (data_packet := str(serial_data.readline(), "utf-8")) != "all set up, starting to send data...\r\n":
    print(data_packet)

# when no data is passed
while serial_data.in_waiting == 0:
    pass

while True:

    # read data
    data_packet = serial_data.readline()
    data_packet = loads(str(data_packet, "utf-8"))

    print(data_packet)

    if len(y) >= MAX_X:
        y.pop(0)

    y.append(data_packet["accel"][0] + data_packet["accel"][1])   

    line.set_xdata(x[MAX_X - len(y):]) # print only x to same number of y values # starting from end so then it gets traslated
    line.set_ydata(y)

    ax.relim()
    # ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

