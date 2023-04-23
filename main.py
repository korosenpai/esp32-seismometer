# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

import serial
from time import sleep
from json import loads

from matplotlib import pyplot as plt

# Initialize plot
# create matplotlib figure and axes
fig, ax = plt.subplots(3)

lines = {
    "x": ax[0].plot([], [])[0],
    "y": ax[1].plot([], [])[0],
    "z": ax[2].plot([], [])[0]
}

# show the plot
plt.show(block=False)


# ax[0].plot()
# ax[1].plot()
# ax[2].plot()

# Set the y-axis range
MAX_X = 300
for elem in ax:
    elem.set_ylim(-20, 20)  # Set the maximum y-axis limit to 1
    elem.set_xlim(0, MAX_X + MAX_X * 0.2)  # Set the maximum y-axis limit to 1
    elem.get_xaxis().set_visible(False) # or -> ax.set_xticklabels([]) ## to hide x axis labels

ax[0].set_title("onde p", fontstyle = "italic", loc = "left", fontsize = "medium")
ax[1].set_title("onde s", fontstyle = "italic", loc = "left", fontsize = "medium")
ax[2].set_title("onde superficiali", fontstyle = "italic", loc = "left", fontsize = "medium")


x = list(range(MAX_X))
y = {
    "x": [], # x recieved from sensor
    "y": [],
    "z": []
}

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

    for n, axis in enumerate(y):
        if len(y[axis]) >= MAX_X:
            y[axis].pop(0)

        y[axis].append(data_packet["accel"][n])    

        lines[axis].set_xdata(x[MAX_X - len(y[axis]):]) # print only x to same number of 'y[axis]' values # starting from end so then it gets traslated
        lines[axis].set_ydata(y[axis])

    ax[0].relim()
    ax[1].relim()
    ax[2].relim()
    # ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

