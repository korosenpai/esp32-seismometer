# 3 component -> separate x, y and z detected in their own graph

import serial
from json import loads

from matplotlib import pyplot as plt

MAX_X = 500 # change value of x axis # overall it will impact velocity of plot when sliding

# create axis data variables
x = list(range(MAX_X))
y = {
    "x": [], # x recieved from sensor
    "y": [],
    "z": []
}

# Initialize plot
# create matplotlib figure and axes
fig, ax = plt.subplots(3)

lines = {
    "x": ax[0].plot([], [])[0],
    "y": ax[1].plot([], [])[0],
    "z": ax[2].plot([], [])[0]
}

plt.show(block=False) # show the plot


# Set the y-axis range
for elem in ax:
    elem.set_ylim(-20, 20)
    elem.set_xlim(0, MAX_X + MAX_X * 0.2) # + 20% to create padding effect
    elem.get_xaxis().set_visible(False) # or -> ax.set_xticklabels([]) ## to hide x axis labels


ax[0].set_title("X; onde superficiali", fontstyle = "italic", loc = "left", fontsize = "medium")
ax[1].set_title("Y; onde superficiali", fontstyle = "italic", loc = "left", fontsize = "medium")
ax[2].set_title("Z; onde sotterranee", fontstyle = "italic", loc = "left", fontsize = "medium")



# initialize serial
BAUDRATE = 115200
serial_data = serial.Serial("com10", BAUDRATE)


# when no data is passed
while serial_data.in_waiting == 0:
    pass

# waiting for setup to finish
while (data_packet := str(serial_data.readline(), "utf-8")) != "all set up, starting to send data...\r\n":
    print(data_packet)


while True:

    # read data
    data_packet = serial_data.readline()
    data_packet = loads(str(data_packet, "utf-8"))

    print(data_packet)

    for n, axis in enumerate(y):

        if len(y[axis]) >= MAX_X: # avoid holding data greater than axis # will slide out of view and crash
            y[axis].pop(0)

        y[axis].append(data_packet["accel"][n])

        # print only x to same number of 'y[axis]' values # starting from end to create sliding effect
        lines[axis].set_xdata(x[MAX_X - len(y[axis]):])
        lines[axis].set_ydata(y[axis])


    fig.canvas.draw()
    fig.canvas.flush_events()

