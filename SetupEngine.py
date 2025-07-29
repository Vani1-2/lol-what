# Compatible only with Debian based systems



import sys
import os
import Setup
import time

def run_update():
    os.system("sudo apt update && sudo apt upgrade -y")

def run_clean():
    os.system("sudo apt autoremove && sudo apt autoclean -y")

def main():
    while True:
        os.system("clear")
        print("\nMaintenece Menu:")
        print("1. Update system")
        print("2. Clean system")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            run_update()
            time.sleep(2.3)
        elif choice == '2':
            run_clean()
        elif choice == '3':
            print("Exiting...")
            time.sleep(2.5)
            break
            os.system("clear")
            Setup.main()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


#On Ubuntu it will force to install snaps instead of a .deb package, f you ubuntu
def install_firefox():
    os.system("sudo apt install firefox -y")

def install_chrome():
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
    os.system("sudo apt install -f -y")

def install_vlc():
    os.system("sudo apt install vlc -y")

def install_fastfetch():
    os.system("sudo apt install fastfetch -y")

def install_vim():
    os.system("sudo apt install vim -y")

def install_git():
    os.system("sudo apt install git -y")


def submain():
    while True:
        os.system("clear")
        print("\nInstall Software:")
        print("1. Firefox")
        print("2. Google Chrome")
        print("3. VLC Media Player")
        print("4. fastfetch")
        print("5. vim")
        print("6. git")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            install_firefox()
            time.sleep(2.4)
        elif choice == '2':
            install_chrome()
            time.sleep(2.5)
        elif choice == '3':
            install_vlc()
            time.sleep(2.5)
        elif choice == '4':
            install_fastfetch()
            time.sleep(2.5)
        elif choice == '5':
            install_vim()
            time.sleep(2.5)
        elif choice == '6':
            install_git()
            time.sleep(2.5)
        elif choice == '7':
            print("Exiting...")
            time.sleep(1.5)
            break
            os.system("clear")
            Setup.main()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    submain()
    