#!/usr/bin/env python3
# Set up imports and paths
import matplotlib.pyplot as plt
import sys, os
from time import sleep, time
bufhelpPath = "../../python/signalProc"
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),bufhelpPath))
import bufhelp

## HELPER FUNCTIONS
def drawnow(fig=None):
    "force a matplotlib figure to redraw itself, inside a compute loop"
    if fig is None: fig=plt.gcf()
    fig.canvas.draw()
    #plt.pause(1e-3) # wait for draw.. 1ms

currentKey=None
def keypressFn(event):
    "wait for keypress in a matplotlib figure, and store in the currentKey global"
    global currentKey
    currentKey=event.key
def waitforkey(fig=None,reset=True):
    "wait for a key to be pressed in the given figure"
    if fig is None: fig=gcf()
    global currentKey
    fig.canvas.mpl_connect('key_press_event',keypressFn)
    if reset: currentKey=None
    while currentKey is None:
        plt.pause(1e-3) # allow gui event processing

## CONFIGURABLE VARIABLES
# make the target sequence
sentences=['hello world','this is new!','BCI is fun!'];
interSentenceDuration=3;
interCharDuration=1;

##------------------------------------------------------
##                    ADD YOUR CODE BELOW HERE
##------------------------------------------------------

# set the display and the string for stimulus
fig = plt.figure()
fig.suptitle('RunSentences-Stimulus', fontsize=24, fontweight='bold')
ax = fig.add_subplot(111) # default full-screen ax
ax.set_xlim((-1,1))
ax.set_ylim((-1,1))
ax.set_axis_off()
h =ax.text(0, 0, 'This is some text', style='italic')

## init connection to the buffer
ftc,hdr=bufhelp.connect();

bufhelp.sendEvent('stimulus.sentences','start');
## STARTING PROGRAM LOOP
h.set_text('some_text')
drawnow() # update the display

sleep(interCharDuration)
    
waitforkey(fig)

