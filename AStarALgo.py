import math
from random import randrange, randint

import pygame
from tkinter import messagebox
import tkinter

window1 = tkinter.Tk()
window1.wm_withdraw()



# This sets the margin between each cell
MARGIN = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1400, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("A Star Algorithm")

# Loop until the user clicks the close button.
done = False

class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.Discovered = False
        self.g = None
        self.h = None
        self.Score = None
        self.isStart = False
        self.IsFinish = False
        self.isSearched = False
        self.isBlock = False
        self.IsBacktracked = False

def getMinimumforDiscoveredList():
    return min([i.Score for i in DiscoveredTrackerToBeSearched])
def calc_manhattan_distance_h(x, y):
    return math.sqrt((abs(x-End[0]))**2 + (abs(y-End[1]))**2)

WIDTH = 5
HEIGHT = 5
#gh = 15
#gw = 26
maxBlockerCount = 9000

#29,900
gh = 130
gw = 230

TileTracker = [ [None]*gw for i in range(gh)]

BlockerCount = 0

for row in range(gh):
    for column in range(gw):
        TileTracker[row][column] = Tile(row, column)

while BlockerCount < maxBlockerCount:
    tx = randint(0,gh - 1)
    ty = randint(0,gw - 1)
    if TileTracker[tx][ty].isBlock == False:
        TileTracker[tx][ty].isBlock = True
        BlockerCount += 1




Start = None
End = None
Found = False

DiscoveredTrackerToBeSearched = []
LastBackTracked = None

def updatenearbyscores(x,y):
    global Found
    global DiscoveredTrackerToBeSearched

    #left
    if (y-1) >= 0 and (y-1)<gw:
        temp_g = 1
        temp_h = calc_manhattan_distance_h(x,y-1)

        #for undiscovered cells
        if  TileTracker[x][y-1].g == None and  TileTracker[x][y-1].h == None:

            if TileTracker[x][y-1].IsFinish:
                Found = True

            elif not TileTracker[x][y-1].isStart and not TileTracker[x][y-1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x][y - 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x][y - 1].g = temp_g

                TileTracker[x][y - 1].h = temp_h
                TileTracker[x][y - 1].Score = round(TileTracker[x][y - 1].g + TileTracker[x][y - 1].h,1)
                TileTracker[x][y - 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x][y - 1])
        else:
            #for discovered cells : check score if its less then update the optimum score
            if ((temp_g+TileTracker[x][y].g)<TileTracker[x][y-1].g):
                TileTracker[x][y-1].g = temp_g + TileTracker[x][y].g
                TileTracker[x][y-1].Score = round(TileTracker[x][y-1].g + TileTracker[x][y-1].h,1)




    #right
    if (y+1) >= 0 and (y+1)<gw:
        temp_g = 1
        temp_h = calc_manhattan_distance_h(x, y+1)

        # for undiscovered cells
        if TileTracker[x][y+1].g == None and TileTracker[x][y+1].h == None:

            if TileTracker[x][y+1].IsFinish:
                Found = True

            elif not TileTracker[x][y+1].isStart and not TileTracker[x][y+1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x][y + 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x][y + 1].g = temp_g
                TileTracker[x][y + 1].h = temp_h
                TileTracker[x][y + 1].Score = round(TileTracker[x][y + 1].g + TileTracker[x][y + 1].h,1)
                TileTracker[x][y + 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x][y + 1])

        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x][y+1].g):
                TileTracker[x][y+1].g = temp_g + TileTracker[x][y].g
                TileTracker[x][y+1].Score = round(TileTracker[x][y+1].g + TileTracker[x][y+1].h,1)


    #top left
    if (x-1) >= 0 and (x-1)<gh and (y-1)>=0 and (y-1)<gw:
        temp_g = math.sqrt(2)
        temp_h = calc_manhattan_distance_h(x-1, y-1)

        # for undiscovered cells
        if TileTracker[x-1][y-1].g == None and TileTracker[x-1][y-1].h == None:
            if TileTracker[x-1][y-1].IsFinish:
                Found = True
            elif not TileTracker[x-1][y-1].isStart and not TileTracker[x-1][y-1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x - 1][y - 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x - 1][y - 1].g = temp_g

                TileTracker[x - 1][y - 1].h = temp_h
                TileTracker[x - 1][y - 1].Score = round(TileTracker[x - 1][y - 1].g + TileTracker[x - 1][y - 1].h,1)
                TileTracker[x - 1][y - 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x - 1][y - 1])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x-1][y-1].g):
                TileTracker[x-1][y-1].g = temp_g + TileTracker[x][y].g
                TileTracker[x-1][y-1].Score = round(TileTracker[x-1][y-1].g + TileTracker[x-1][y-1].h,1)
        print(TileTracker[x-1][y-1].Score)

    #top right
    if (x-1) >= 0 and (x-1)<gh and (y+1)>=0 and (y+1)<gw:
        temp_g = math.sqrt(2)
        temp_h = calc_manhattan_distance_h(x - 1, y + 1)

        # for undiscovered cells
        if TileTracker[x - 1][y + 1].g == None and TileTracker[x - 1][y + 1].h == None:
            if TileTracker[x - 1][y + 1].IsFinish:
                Found = True
            elif not TileTracker[x - 1][y + 1].isStart and not TileTracker[x - 1][y + 1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x - 1][y + 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x - 1][y + 1].g = temp_g

                TileTracker[x - 1][y + 1].h = temp_h
                TileTracker[x - 1][y + 1].Score = round(TileTracker[x - 1][y + 1].g + TileTracker[x - 1][y + 1].h,1)
                TileTracker[x - 1][y + 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x - 1][y + 1])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x - 1][y + 1].g):
                TileTracker[x - 1][y + 1].g = temp_g + TileTracker[x][y].g
                TileTracker[x - 1][y + 1].Score = round(TileTracker[x - 1][y + 1].g + TileTracker[x - 1][y + 1].h,1)
        print(TileTracker[x - 1][y + 1].Score)

    #top
    if (x-1) >= 0 and (x-1)<gh:
        temp_g = 1
        temp_h = calc_manhattan_distance_h(x - 1,y)

        # for undiscovered cells
        if TileTracker[x - 1][y].g == None and TileTracker[x - 1][y].h == None:
            if TileTracker[x - 1][y].IsFinish:
                Found = True
            elif not TileTracker[x - 1][y].isStart and not TileTracker[x - 1][y].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x - 1][y].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x - 1][y].g = temp_g
                TileTracker[x - 1][y].h = temp_h
                TileTracker[x - 1][y].Score = round(TileTracker[x - 1][y].g + TileTracker[x - 1][y].h,1)
                TileTracker[x - 1][y].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x - 1][y])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x - 1][y].g):
                TileTracker[x - 1][y].g = temp_g + TileTracker[x][y].g
                TileTracker[x - 1][y].Score = TileTracker[x - 1][y].g + TileTracker[x - 1][y].h
        print(TileTracker[x - 1][y].Score)

    #bottom
    if (x+1) >= 0 and (x+1)<gh:
        temp_g = 1
        temp_h = calc_manhattan_distance_h(x + 1, y)

        # for undiscovered cells
        if TileTracker[x + 1][y].g == None and TileTracker[x + 1][y].h == None:
            if TileTracker[x + 1][y].IsFinish:
                Found = True
            elif not TileTracker[x + 1][y].isStart and not TileTracker[x + 1][y].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x + 1][y].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x + 1][y].g = temp_g
                TileTracker[x + 1][y].h = temp_h
                TileTracker[x + 1][y].Score = round(TileTracker[x + 1][y].g + TileTracker[x + 1][y].h,1)
                TileTracker[x + 1][y].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x + 1][y])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x + 1][y].g):
                TileTracker[x + 1][y].g = temp_g + TileTracker[x][y].g
                TileTracker[x + 1][y].Score = round(TileTracker[x + 1][y].g + TileTracker[x + 1][y].h,1)
        print(TileTracker[x + 1][y].Score)

    #bottom left
    if (x+1) >= 0 and (x+1)<gh and (y-1)>=0 and (y-1)<gw:
        temp_g = math.sqrt(2)
        temp_h = calc_manhattan_distance_h(x + 1, y - 1)

        # for undiscovered cells
        if TileTracker[x + 1][y - 1].g == None and TileTracker[x + 1][y - 1].h == None:
            if TileTracker[x + 1][y - 1].IsFinish:
                Found = True
            elif not TileTracker[x + 1][y - 1].isStart and not TileTracker[x + 1][y - 1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x + 1][y - 1].g = temp_g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x + 1][y - 1].g = temp_g
                TileTracker[x + 1][y - 1].h = temp_h
                TileTracker[x + 1][y - 1].Score = round(TileTracker[x + 1][y - 1].g + TileTracker[x + 1][y - 1].h,1)
                TileTracker[x + 1][y - 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x + 1][y - 1])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x + 1][y - 1].g):
                TileTracker[x + 1][y - 1].g = temp_g + TileTracker[x][y].g
                TileTracker[x + 1][y - 1].Score = round(TileTracker[x + 1][y - 1].g + TileTracker[x + 1][y - 1].h,1)
        print(TileTracker[x + 1][y - 1].Score)

    #bottom right

    if (x+1) >= 0 and (x+1)<gh and (y+1)>=0 and (y+1)<gw:
        temp_g = math.sqrt(2)
        temp_h = calc_manhattan_distance_h(x + 1, y + 1)

        # for undiscovered cells
        if TileTracker[x + 1][y + 1].g == None and TileTracker[x + 1][y + 1].h == None:
            if TileTracker[x+1][y+1].IsFinish:
                Found = True
            elif not TileTracker[x+1][y+1].isStart and not TileTracker[x+1][y+1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x + 1][y + 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x + 1][y + 1].g = temp_g

                TileTracker[x + 1][y + 1].h = temp_h
                TileTracker[x + 1][y + 1].Score = round(TileTracker[x + 1][y + 1].g + TileTracker[x + 1][y + 1].h,1)
                TileTracker[x + 1][y + 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x + 1][y + 1])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x + 1][y + 1].g):
                TileTracker[x + 1][y + 1].g = temp_g + TileTracker[x][y].g
                TileTracker[x + 1][y + 1].Score = round(TileTracker[x + 1][y + 1].g + TileTracker[x + 1][y + 1].h,1)
        print(TileTracker[x + 1][y + 1].Score)

    TileTracker[x][y].isSearched = True

    # while not Found:
    #     pass#KeepDiscovering()

def updatenearbyscores_ignoring_corners(x,y):
    global Found
    global DiscoveredTrackerToBeSearched

    #left
    if (y-1) >= 0 and (y-1)<gw:
        temp_g = 1
        temp_h = calc_manhattan_distance_h(x,y-1)

        #for undiscovered cells
        if  TileTracker[x][y-1].g == None and  TileTracker[x][y-1].h == None:

            if TileTracker[x][y-1].IsFinish:
                Found = True

            elif not TileTracker[x][y-1].isStart and not TileTracker[x][y-1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x][y - 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x][y - 1].g = temp_g

                TileTracker[x][y - 1].h = temp_h
                TileTracker[x][y - 1].Score = round(TileTracker[x][y - 1].g + TileTracker[x][y - 1].h,1)
                TileTracker[x][y - 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x][y - 1])
        else:
            #for discovered cells : check score if its less then update the optimum score
            if ((temp_g+TileTracker[x][y].g)<TileTracker[x][y-1].g):
                TileTracker[x][y-1].g = temp_g + TileTracker[x][y].g
                TileTracker[x][y-1].Score = round(TileTracker[x][y-1].g + TileTracker[x][y-1].h,1)




    #right
    if (y+1) >= 0 and (y+1)<gw:
        temp_g = 1
        temp_h = calc_manhattan_distance_h(x, y+1)

        # for undiscovered cells
        if TileTracker[x][y+1].g == None and TileTracker[x][y+1].h == None:

            if TileTracker[x][y+1].IsFinish:
                Found = True

            elif not TileTracker[x][y+1].isStart and not TileTracker[x][y+1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x][y + 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x][y + 1].g = temp_g
                TileTracker[x][y + 1].h = temp_h
                TileTracker[x][y + 1].Score = round(TileTracker[x][y + 1].g + TileTracker[x][y + 1].h,1)
                TileTracker[x][y + 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x][y + 1])

        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x][y+1].g):
                TileTracker[x][y+1].g = temp_g + TileTracker[x][y].g
                TileTracker[x][y+1].Score = round(TileTracker[x][y+1].g + TileTracker[x][y+1].h,1)


    #top left
    if (x-1) >= 0 and (x-1)<gh and (y-1)>=0 and (y-1)<gw:
        temp_g = math.sqrt(2)
        temp_h = calc_manhattan_distance_h(x-1, y-1)

        # for undiscovered cells
        if TileTracker[x-1][y-1].g == None and TileTracker[x-1][y-1].h == None and not TileTracker[x-1][y].isBlock and not TileTracker[x][y-1].isBlock:
            if TileTracker[x-1][y-1].IsFinish:
                Found = True
            elif not TileTracker[x-1][y-1].isStart and not TileTracker[x-1][y-1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x - 1][y - 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x - 1][y - 1].g = temp_g

                TileTracker[x - 1][y - 1].h = temp_h
                TileTracker[x - 1][y - 1].Score = round(TileTracker[x - 1][y - 1].g + TileTracker[x - 1][y - 1].h,1)
                TileTracker[x - 1][y - 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x - 1][y - 1])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if not TileTracker[x - 1][y].isBlock and not TileTracker[x][y - 1].isBlock:
                if ((temp_g + TileTracker[x][y].g) < TileTracker[x-1][y-1].g):
                    TileTracker[x-1][y-1].g = temp_g + TileTracker[x][y].g
                    TileTracker[x-1][y-1].Score = round(TileTracker[x-1][y-1].g + TileTracker[x-1][y-1].h,1)
        print(TileTracker[x-1][y-1].Score)

    #top right
    if (x-1) >= 0 and (x-1)<gh and (y+1)>=0 and (y+1)<gw:
        temp_g = math.sqrt(2)
        temp_h = calc_manhattan_distance_h(x - 1, y + 1)

        # for undiscovered cells
        if TileTracker[x - 1][y + 1].g == None and TileTracker[x - 1][y + 1].h == None and not TileTracker[x - 1][y].isBlock and not TileTracker[x][y + 1].isBlock:
            if TileTracker[x - 1][y + 1].IsFinish:
                Found = True
            elif not TileTracker[x - 1][y + 1].isStart and not TileTracker[x - 1][y + 1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x - 1][y + 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x - 1][y + 1].g = temp_g

                TileTracker[x - 1][y + 1].h = temp_h
                TileTracker[x - 1][y + 1].Score = round(TileTracker[x - 1][y + 1].g + TileTracker[x - 1][y + 1].h,1)
                TileTracker[x - 1][y + 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x - 1][y + 1])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if not TileTracker[x - 1][y].isBlock and not TileTracker[x][y + 1].isBlock:
                if ((temp_g + TileTracker[x][y].g) < TileTracker[x - 1][y + 1].g):
                    TileTracker[x - 1][y + 1].g = temp_g + TileTracker[x][y].g
                    TileTracker[x - 1][y + 1].Score = round(TileTracker[x - 1][y + 1].g + TileTracker[x - 1][y + 1].h,1)
        print(TileTracker[x - 1][y + 1].Score)

    #top
    if (x-1) >= 0 and (x-1)<gh:
        temp_g = 1
        temp_h = calc_manhattan_distance_h(x - 1,y)

        # for undiscovered cells
        if TileTracker[x - 1][y].g == None and TileTracker[x - 1][y].h == None:
            if TileTracker[x - 1][y].IsFinish:
                Found = True
            elif not TileTracker[x - 1][y].isStart and not TileTracker[x - 1][y].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x - 1][y].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x - 1][y].g = temp_g
                TileTracker[x - 1][y].h = temp_h
                TileTracker[x - 1][y].Score = round(TileTracker[x - 1][y].g + TileTracker[x - 1][y].h,1)
                TileTracker[x - 1][y].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x - 1][y])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x - 1][y].g):
                TileTracker[x - 1][y].g = temp_g + TileTracker[x][y].g
                TileTracker[x - 1][y].Score = TileTracker[x - 1][y].g + TileTracker[x - 1][y].h
        print(TileTracker[x - 1][y].Score)

    #bottom
    if (x+1) >= 0 and (x+1)<gh:
        temp_g = 1
        temp_h = calc_manhattan_distance_h(x + 1, y)

        # for undiscovered cells
        if TileTracker[x + 1][y].g == None and TileTracker[x + 1][y].h == None:
            if TileTracker[x + 1][y].IsFinish:
                Found = True
            elif not TileTracker[x + 1][y].isStart and not TileTracker[x + 1][y].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x + 1][y].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x + 1][y].g = temp_g
                TileTracker[x + 1][y].h = temp_h
                TileTracker[x + 1][y].Score = round(TileTracker[x + 1][y].g + TileTracker[x + 1][y].h,1)
                TileTracker[x + 1][y].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x + 1][y])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if ((temp_g + TileTracker[x][y].g) < TileTracker[x + 1][y].g):
                TileTracker[x + 1][y].g = temp_g + TileTracker[x][y].g
                TileTracker[x + 1][y].Score = round(TileTracker[x + 1][y].g + TileTracker[x + 1][y].h,1)
        print(TileTracker[x + 1][y].Score)

    #bottom left
    if (x+1) >= 0 and (x+1)<gh and (y-1)>=0 and (y-1)<gw:
        temp_g = math.sqrt(2)
        temp_h = calc_manhattan_distance_h(x + 1, y - 1)

        # for undiscovered cells
        if TileTracker[x + 1][y - 1].g == None and TileTracker[x + 1][y - 1].h == None and not TileTracker[x + 1][y].isBlock and not TileTracker[x][y - 1].isBlock:
            if TileTracker[x + 1][y - 1].IsFinish:
                Found = True
            elif not TileTracker[x + 1][y - 1].isStart and not TileTracker[x + 1][y - 1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x + 1][y - 1].g = temp_g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x + 1][y - 1].g = temp_g
                TileTracker[x + 1][y - 1].h = temp_h
                TileTracker[x + 1][y - 1].Score = round(TileTracker[x + 1][y - 1].g + TileTracker[x + 1][y - 1].h,1)
                TileTracker[x + 1][y - 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x + 1][y - 1])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if not TileTracker[x + 1][y].isBlock and not TileTracker[x][y - 1].isBlock:
                if ((temp_g + TileTracker[x][y].g) < TileTracker[x + 1][y - 1].g):
                    TileTracker[x + 1][y - 1].g = temp_g + TileTracker[x][y].g
                    TileTracker[x + 1][y - 1].Score = round(TileTracker[x + 1][y - 1].g + TileTracker[x + 1][y - 1].h,1)
        print(TileTracker[x + 1][y - 1].Score)

    #bottom right

    if (x+1) >= 0 and (x+1)<gh and (y+1)>=0 and (y+1)<gw:
        temp_g = math.sqrt(2)
        temp_h = calc_manhattan_distance_h(x + 1, y + 1)

        # for undiscovered cells
        if TileTracker[x + 1][y + 1].g == None and TileTracker[x + 1][y + 1].h == None and not TileTracker[x][y + 1].isBlock and not TileTracker[x + 1][y].isBlock:
            if TileTracker[x+1][y+1].IsFinish:
                Found = True
            elif not TileTracker[x+1][y+1].isStart and not TileTracker[x+1][y+1].isBlock:
                if TileTracker[x][y].g != None:
                    TileTracker[x + 1][y + 1].g = temp_g + TileTracker[x][y].g
                else:
                    TileTracker[x + 1][y + 1].g = temp_g

                TileTracker[x + 1][y + 1].h = temp_h
                TileTracker[x + 1][y + 1].Score = round(TileTracker[x + 1][y + 1].g + TileTracker[x + 1][y + 1].h,1)
                TileTracker[x + 1][y + 1].Discovered = True
                DiscoveredTrackerToBeSearched.append(TileTracker[x + 1][y + 1])
        else:
            # for discovered cells : check score if its less then update the optimum score
            if not TileTracker[x][y + 1].isBlock and not TileTracker[x + 1][y].isBlock:
                if ((temp_g + TileTracker[x][y].g) < TileTracker[x + 1][y + 1].g):
                    TileTracker[x + 1][y + 1].g = temp_g + TileTracker[x][y].g
                    TileTracker[x + 1][y + 1].Score = round(TileTracker[x + 1][y + 1].g + TileTracker[x + 1][y + 1].h,1)
        print(TileTracker[x + 1][y + 1].Score)

    TileTracker[x][y].isSearched = True

    # while not Found:
    #     pass#KeepDiscovering()

BackTrackDone = False
def UpdateBackTracking(x,y):
    BackTrackList = []
    global LastBackTracked
    #left
    if (y-1)>=0 and (y-1)<gw and TileTracker[x][y-1].isStart:
        BackTrackDone = True
        return
    if (y-1)>=0 and (y-1)<gw and TileTracker[x][y-1].isSearched == True:
        BackTrackList.append(TileTracker[x][y-1])
    #right
    if (y+1)>=0 and (y+1)<gw and TileTracker[x][y+1].isStart:
        BackTrackDone = True
        return
    if (y+1)>=0 and (y+1)<gw and TileTracker[x][y+1].isSearched == True:
        BackTrackList.append(TileTracker[x][y+1])
    #top
    if (x-1)>=0 and (x-1)<gh and TileTracker[x-1][y].isStart:
        BackTrackDone = True
        return
    if (x-1)>=0 and (x-1)<gh and TileTracker[x-1][y].isSearched == True:
        BackTrackList.append(TileTracker[x-1][y])

    #topleft
    if (x-1)>=0 and (x-1)<gh and (y-1)>=0 and (y-1)<gw and TileTracker[x-1][y-1].isStart:
        BackTrackDone = True
        return
    if (x-1)>=0 and (x-1)<gh and (y-1)>=0 and (y-1)<gw and TileTracker[x-1][y-1].isSearched == True:
        BackTrackList.append(TileTracker[x-1][y-1])

    #topright
    if (x-1)>=0 and (x-1)<gh and (y+1)>=0 and (y+1)<gw and TileTracker[x-1][y+1].isStart:
        BackTrackDone = True
        return
    if (x-1)>=0 and (x-1)<gh and (y+1)>=0 and (y+1)<gw and TileTracker[x-1][y+1].isSearched == True:
        BackTrackList.append(TileTracker[x-1][y+1])

    #bottom
    if (x+1)>=0 and (x+1)<gh and TileTracker[x+1][y].isStart:
        BackTrackDone = True
        return
    if (x+1)>=0 and (x+1)<gh and TileTracker[x+1][y].isSearched == True:
        BackTrackList.append(TileTracker[x+1][y])

    #bottomleft
    if (x+1)>=0 and (x+1)<gh and (y-1)>=0 and (y-1)<gw and TileTracker[x+1][y-1].isStart:
        BackTrackDone = True
        return
    if (x+1)>=0 and (x+1)<gh and (y-1)>=0 and (y-1)<gw and TileTracker[x+1][y-1].isSearched == True:
        BackTrackList.append(TileTracker[x+1][y-1])

    #bottomright
    if (x+1)>=0 and (x+1)<gh and (y+1)>=0 and (y+1)<gw and TileTracker[x+1][y+1].isStart:
        BackTrackDone = True
        return
    if (x+1)>=0 and (x+1)<gh and (y+1)>=0 and (y+1)<gw and TileTracker[x+1][y+1].isSearched == True:
        BackTrackList.append(TileTracker[x+1][y+1])

    minE = min([i.g for i in BackTrackList if i.IsBacktracked == False])

    for j in BackTrackList:
        if j.g == minE and j.IsBacktracked == False:
            TileTracker[j.x][j.y].IsBacktracked = True
            LastBackTracked = [j.x,j.y]
            return

def UpdateBackTracking_ignoring_corners(x,y):
    BackTrackList = []
    global LastBackTracked
    #left
    if (y-1)>=0 and (y-1)<gw and TileTracker[x][y-1].isStart:
        BackTrackDone = True
        return
    if (y-1)>=0 and (y-1)<gw and TileTracker[x][y-1].isSearched == True:
        BackTrackList.append(TileTracker[x][y-1])
    #right
    if (y+1)>=0 and (y+1)<gw and TileTracker[x][y+1].isStart:
        BackTrackDone = True
        return
    if (y+1)>=0 and (y+1)<gw and TileTracker[x][y+1].isSearched == True:
        BackTrackList.append(TileTracker[x][y+1])
    #top
    if (x-1)>=0 and (x-1)<gh and TileTracker[x-1][y].isStart:
        BackTrackDone = True
        return
    if (x-1)>=0 and (x-1)<gh and TileTracker[x-1][y].isSearched == True:
        BackTrackList.append(TileTracker[x-1][y])

    #topleft
    if (x-1)>=0 and (x-1)<gh and (y-1)>=0 and (y-1)<gw and TileTracker[x-1][y-1].isStart:
        BackTrackDone = True
        return
    if (x-1)>=0 and (x-1)<gh and (y-1)>=0 and (y-1)<gw and TileTracker[x-1][y-1].isSearched == True:
        if not TileTracker[x-1][y].isBlock and not TileTracker[x][y-1].isBlock:
            BackTrackList.append(TileTracker[x-1][y-1])

    #topright
    if (x-1)>=0 and (x-1)<gh and (y+1)>=0 and (y+1)<gw and TileTracker[x-1][y+1].isStart:
        BackTrackDone = True
        return
    if (x-1)>=0 and (x-1)<gh and (y+1)>=0 and (y+1)<gw and TileTracker[x-1][y+1].isSearched == True:
        if not TileTracker[x-1][y].isBlock and not TileTracker[x][y+1].isBlock :
            BackTrackList.append(TileTracker[x-1][y+1])

    #bottom
    if (x+1)>=0 and (x+1)<gh and TileTracker[x+1][y].isStart:
        BackTrackDone = True
        return
    if (x+1)>=0 and (x+1)<gh and TileTracker[x+1][y].isSearched == True:
        BackTrackList.append(TileTracker[x+1][y])

    #bottomleft
    if (x+1)>=0 and (x+1)<gh and (y-1)>=0 and (y-1)<gw and TileTracker[x+1][y-1].isStart:
        BackTrackDone = True
        return
    if (x+1)>=0 and (x+1)<gh and (y-1)>=0 and (y-1)<gw and TileTracker[x+1][y-1].isSearched == True:
        if not TileTracker[x][y-1].isBlock and not TileTracker[x+1][y].isBlock:
            BackTrackList.append(TileTracker[x+1][y-1])

    #bottomright
    if (x+1)>=0 and (x+1)<gh and (y+1)>=0 and (y+1)<gw and TileTracker[x+1][y+1].isStart:
        BackTrackDone = True
        return
    if (x+1)>=0 and (x+1)<gh and (y+1)>=0 and (y+1)<gw and TileTracker[x+1][y+1].isSearched == True:
        if not TileTracker[x+1][y].isBlock and not TileTracker[x][y+1].isBlock:
            BackTrackList.append(TileTracker[x+1][y+1])

    minE = min([i.g for i in BackTrackList if i.IsBacktracked == False])

    for j in BackTrackList:
        if j.g == minE and j.IsBacktracked == False:
            TileTracker[j.x][j.y].IsBacktracked = True
            LastBackTracked = [j.x,j.y]
            return









number_font = pygame.font.SysFont( None, 16 )

SearchStarted = False
BackTrackedToStart = False
IsdrawingBlocks = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
count = 0
while not done:
    # run search subsequently until Goal Found ! :)
    if Start is not None and End is not None and not Found and SearchStarted:
        if len(DiscoveredTrackerToBeSearched) != 0:
            tempD = 0
            tempDC = DiscoveredTrackerToBeSearched.copy()
            minA = getMinimumforDiscoveredList()
            for i in range(0,len(tempDC)):
                if tempDC[i].Score == minA and tempDC[i].isSearched == False:
                    #updatenearbyscores(tempDC[i].x, tempDC[i].y)
                    updatenearbyscores_ignoring_corners(tempDC[i].x, tempDC[i].y)
                    tempD += 1
            l = 0
            while tempD>0:
                if DiscoveredTrackerToBeSearched[l].isSearched == True and DiscoveredTrackerToBeSearched[l].Score == minA:
                    del DiscoveredTrackerToBeSearched[l]
                    tempD -= 1
                    continue
                l += 1

        else:
            if count == 1:
                print('cannot reach destination ! its blocked')
            else:
                #updatenearbyscores(Start[0],Start[1])
                updatenearbyscores_ignoring_corners(Start[0],Start[1])
                count = 1

    # backtracking
    if Found and not BackTrackDone:
        if LastBackTracked == None:
            #UpdateBackTracking(End[0],End[1])
            UpdateBackTracking_ignoring_corners(End[0],End[1])
        else:
            #UpdateBackTracking(LastBackTracked[0], LastBackTracked[1])
            UpdateBackTracking_ignoring_corners(LastBackTracked[0], LastBackTracked[1])


    # Draw the grid and display routes
    for row in range(gh):
        for column in range(gw):
            pygame.draw.rect(screen,
                             'White',
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

            if [row,column] == Start:
                pygame.draw.rect(screen,
                                 'Blue',
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

            if [row,column] == End:
                pygame.draw.rect(screen,
                                 'Red',
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

            if TileTracker[row][column].isBlock == True:
                pygame.draw.rect(screen, 'Black',
                                 [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

            if TileTracker[row][column].Discovered == True:
                number_image = number_font.render(str(round(TileTracker[row][column].g,1)), True, 'BLACK', 'WHITE')

                if TileTracker[row][column].isSearched == True:
                    pygame.draw.rect(screen,'Red',[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])

                elif TileTracker[row][column].Discovered == True:
                    pygame.draw.rect(screen,'Green',[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
            if TileTracker[row][column].IsBacktracked == True:
                pygame.draw.rect(screen, 'Purple',[(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])



                #screen.blit(number_image, (((MARGIN + WIDTH) * column + MARGIN + 15), ((MARGIN + HEIGHT) * row + MARGIN + 15)))

    # initiate search via key press after start and goal are set
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if Start is None:
                Start = [row, column]
                TileTracker[row][column].isStart = True
            elif End is None:
                End = [row, column]
                TileTracker[row][column].IsFinish = True
            else:
                IsdrawingBlocks = True
                if not TileTracker[row][column].isStart and not TileTracker[row][column].IsFinish:
                    TileTracker[row][column].isBlock = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if Start is not None and End is not None and not Found:
                    SearchStarted = True
                    if len(DiscoveredTrackerToBeSearched) != 0:
                        tempD = 0
                        tempDC = DiscoveredTrackerToBeSearched.copy()
                        minA = getMinimumforDiscoveredList()
                        for i in range(0, len(tempDC)):
                            if tempDC[i].Score == minA and tempDC[i].isSearched == False:
                                #updatenearbyscores(tempDC[i].x, tempDC[i].y)
                                updatenearbyscores_ignoring_corners(tempDC[i].x, tempDC[i].y)
                                tempD += 1
                        l = 0
                        while tempD > 0:
                            if DiscoveredTrackerToBeSearched[l].isSearched == True and DiscoveredTrackerToBeSearched[
                                l].Score == minA:
                                del DiscoveredTrackerToBeSearched[l]
                                tempD -= 1
                                continue
                            l += 1

                    else:
                        if count == 1:
                            print('cannot reach destination ! its blocked')
                        else:
                            #updatenearbyscores(Start[0], Start[1])
                            updatenearbyscores_ignoring_corners(Start[0], Start[1])
                            count = 1
            if event.key == pygame.K_r:
                TileTracker = [[None] * gw for i in range(gh)]
                Start = None
                End = None
                Found = False
                SearchStarted = False
                DiscoveredTrackerToBeSearched = []
                count = 0
                LastBackTracked = None
                BackTrackDone = False
                for row in range(gh):
                    for column in range(gw):
                        TileTracker[row][column] = Tile(row, column)

        elif event.type == pygame.MOUSEMOTION:
            if IsdrawingBlocks:
                mouse_position = pygame.mouse.get_pos()
                column = mouse_position[0] // (WIDTH + MARGIN)
                row = mouse_position[1] // (HEIGHT + MARGIN)

            if not TileTracker[row][column].isStart and not TileTracker[row][column].IsFinish:
                TileTracker[row][column].isBlock = True

        elif event.type == pygame.MOUSEBUTTONUP:
            IsdrawingBlocks = False

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
