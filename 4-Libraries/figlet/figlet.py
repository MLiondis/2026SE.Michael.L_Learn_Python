import sys
import pyfiglet
import random

from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f":
        if sys.argv[2] in pyfiglet.FigletFont.getFonts():
            figlet.setFont(font=sys.argv[2])
            text = input("Enter text: ")
            print(figlet.renderText(text))
        else:
            sys.exit(print("Invalid Font"))
    else:
        sys.exit(print("Invalid Usage"))
elif len(sys.argv) == 1:
    figlet.setFont(font = random.choice(pyfiglet.FigletFont.getFonts()))
    text = input("Enter text: ")
    print(figlet.renderText(text))
else:
    sys.exit(print("Invalid Usage"))