import serial
from time import sleep
from json import loads

import pygame
# from pygame.locals import *


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


pygame.init()

# WIDTH = 640
# HEIGHT = 480
# GRID_SIZE = 15
# AXIS_PADDING = 20

AXIS_PADDING = 50
AXIS_WIDTH = 3
AXIS_STEP_Y = 60
AXIS_STEP_X = AXIS_STEP_Y * 2
AXIS_STEP__LENGTH = 10
AXIS_STEP_VALUE = 20

# screen res
HEIGHT = 2.5 * AXIS_PADDING + AXIS_STEP_Y * 9
WIDTH = 2.5 * AXIS_PADDING + AXIS_STEP_X * 7

print(f"width: {WIDTH}, height: {HEIGHT}")

# vars for graph
ORIGINX = 1.5 * AXIS_PADDING
ORIGINY = HEIGHT - 1.5 * AXIS_PADDING
ORIGIN = ( ORIGINX, ORIGINY ) # position on screen of (0, 0)

# elements in graph
x = list(range(100))
y = []



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("seismometer")

FONT_SIZE = 20
FONT = pygame.font.SysFont("cascadiamonoregular", FONT_SIZE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    while serial_data.in_waiting == 0:
        pass

    screen.fill((255, 255, 255))

    # draw axis
    pygame.draw.line(screen, (0, 0, 0), (ORIGINX, AXIS_PADDING), ORIGIN, AXIS_WIDTH) # y
    pygame.draw.line(screen, (0, 0, 0), ORIGIN, (WIDTH - AXIS_PADDING, ORIGINY), AXIS_WIDTH) # x

    # draw axis lines y
    for i in range(9, 0, -1):
        pygame.draw.line(screen, (0, 0, 0),
            (ORIGINX + AXIS_STEP__LENGTH, ORIGINY - AXIS_STEP_Y * (i - 1)),
            (ORIGINX - AXIS_STEP__LENGTH, ORIGINY - AXIS_STEP_Y * (i - 1)),
        AXIS_WIDTH)
        y_graph_number = FONT.render(str(AXIS_STEP_VALUE - 5 * (i - 1)) , False, (0, 0, 0))
        screen.blit(y_graph_number,
            (
                ORIGINX - 2 * AXIS_STEP__LENGTH - y_graph_number.get_width(),
                AXIS_PADDING + AXIS_STEP_Y * i - y_graph_number.get_height() / 2
            )
        )
    
    # draw axis lines x
    for i in range(7):
        pygame.draw.line(screen, (0, 0, 0),
            (ORIGINX + AXIS_STEP_X * i, ORIGINY - AXIS_STEP__LENGTH),
            (ORIGINX + AXIS_STEP_X * i, ORIGINY + AXIS_STEP__LENGTH),
        AXIS_WIDTH)
        y_graph_number = FONT.render(str(AXIS_STEP_VALUE * i) , False, (0, 0, 0))
        screen.blit(y_graph_number,
            (
                ORIGINX + AXIS_STEP_X * i - y_graph_number.get_width() / 2,
                ORIGINY + 2 * AXIS_STEP__LENGTH - y_graph_number.get_height() / 2
            )
        )


    ########## add accel data to graph ##########

    # read data
    data_packet = serial_data.readline()
    data_packet = loads(str(data_packet, "utf-8"))


    print(data_packet)

    if len(y) >= 100:
        y.pop(0)

    y.append(data_packet["accel"][0])

    # pygame.draw.lines(screen, (0, 0, 0), False, [ORIGINX + ], 5)



    pygame.display.flip() # TODO or update or blit? check which one to use
