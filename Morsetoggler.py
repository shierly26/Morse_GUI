from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

CODE = {' ': ' ',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}


## hardware
led = LED(14)

def dot():
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)

def dash():
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)


## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = "Helvetica",size = 12, weight = "bold")

### EVENT FUNCTIONS ###  
def MorseToggle():
    if led.is_lit:
        led.off()
        MorseButton["text"] = "Turn Morse on"
    else:
        
        inputValue = textBox.get("1.0","end-1c")
        for letter in inputValue:
            for symbol in CODE[letter.upper()]:
                if symbol == "-":
                    dash()
                elif symbol == ".":
                    dot()
                else:       
                    time.sleep(0.5)
            time.sleep(0.5)		
def close():
    GPIO.cleanup()
    win.destroy()
    
### WIDGETS ###
label = Label(win, text= "Enter Text:")
label.grid(row =0, column=0)

textBox= Text(win,height=2,width=10)
textBox.grid(row=0,column=1)

MorseButton = Button(win, text = "Turn Morse on", font = myFont, command = MorseToggle, bg = "red", height = 1, width = 24)
MorseButton.grid(row=1, column=1)

ExitButton = Button(win, text = "Exit", font = myFont, command = close, bg = "bisque2", height = 1, width = 6)
ExitButton.grid(row=2, column=1)

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly

win.mainloop() #loop forever
