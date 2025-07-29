# Compatible only with Debian based systems
import SetupEngine
import time 
import os 
import sys

def main():
    while True:
        os.system("clear")
        print("Hello, I am Vani, your setup helper.")
        print("I can help you with installing and maintaining packages.")
        print("Please pick from the options below:")
        print("1. Maintenance")
        print("2. Software Install")
        print("3. Exit")
        
        
        task = input("Please enter the task you want me to perform: ")

        if task == "1":
            print("Affirmative")
            SetupEngine.main()
        elif task == "2":
            print("Alright")
            SetupEngine.submain()
        elif task == "3":
            print("Shutting Down.... Please don't close the terminal")
            time.sleep(3)
            os.system("clear")
            break
        else: 
            print("I am not sure how to do that yet.")
            time.sleep(2.5)

if __name__ == "__main__":
    main()
