"""
Python program to demonstrate concept of Interfaces. 
Program contains Printer interface and its subclasses to send text to any printer.
"""
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass
    
    def disconnect(self):
        pass

class HP(Printer):
    def printit(self, text):
        print("HP prints:", text)
    
    def disconnect(self):
        print("Disconnected from HP")
        return 0
    
class IBM(Printer):
    def printit(self, text):
        print("IBM prints:", text)
    
    def disconnect(self):
        print("Disconnected from IBM")
        return 0
    
def main():
    choice = input("Which printer do you want to use? ")
    if choice.lower() == "hp":
        hp = HP()
        while True:
            text = input("Enter some text to print: ")
            hp.printit(text)
            
            inp = input("Continue using? (Y/N): ")
            
            if inp.lower().startswith("n"):
                break
        return hp.disconnect()
        
    elif choice.lower() == "ibm":
        ibm = IMB()
        while True:
            text = input("Enter some text to print: ")
            ibm.printit(text)
            
            inp = input("Continue using? (Y/N): ")
            
            if inp.lower().startswith("n"):
                break
        return ibm.disconnect()
    else:
        print("Error, incorrect choice.")
        return -1
    
if __name__ == "__main__":
    while True:
        output = main()
        if output == 0:
            break
