import time
from tkinter import *
import tkinter as tk
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

led = LED(14)

# Top level window
frame = tk.Tk()
frame.title("Morse Code input by Finn Steendam")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget

MORSEDICT = {' ': '_', "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--', 
             '-': '-....-', '.': '.-.-.-', '/': '-..-.', '0': '-----', '1': '.----', 
             '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
             '7': '--...', '8': '---..', '9': '----.', ':': '---...', ';': '-.-.-.', 
             '?': '..--..', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 
             'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 
             'R': '.-.','S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 
             'X': '-..-', 'Y': '-.--', 'Z': '--..', '_': '..--.-'}

  
def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        if inp != '' and len(inp) < 12:
                encodedSentence = Morse_Letter(inp)
                lbl.config(text = inp + " in morse = " + encodedSentence)
                for characters in encodedSentence:
                        if characters == '.':
                                led.on()
                                time.sleep(0.25)
                                led.off()
                                time.sleep(0.15)
                        else:
                                led.on()
                                time.sleep(1)
                                led.off()
                                time.sleep(0.15)
        else:
                lbl.config(text = "Please input a string with less than 12 characters")
                        

def Morse_Letter(letter):
        list_letter = letter.upper()
       # lbl.config(text = list_letter[1])
        encodedSentence = ""
        for characters in list_letter:
                encodedSentence += MORSEDICT[characters] + ""

               
        return encodedSentence

# TextBox Creation
inputtxt = tk.Text(frame, height = 5, width = 20)  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(frame, text = "Print", command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()

frame.mainloop()
