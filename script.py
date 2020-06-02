import cv2
import os
import sys
import time

width = os.get_terminal_size().columns
dash = '-' * 61
welcome_message = "CONSOL IMAGE EDITOR"
exit_message = "THANK YOU"
parts = sys.argv[1].split("/")
location = '/'.join(parts[:-1])
sys.path.insert(1, location)
img = cv2.imread(sys.argv[1], 1)


def exitpg(changeKey):
    print(" ")
    if(changeKey == 1):
        print(" FILE SAVED AS \'newfile.jpg\'\n") 
    else:
        print(" NO CHANGES MADE.\n")
    print(exit_message.center(width-len(exit_message)+10))
    print(" "+'*' * (width-1))
    exit(0)
    
def saveImg(newImg):
    cv2.imwrite(location+'/'+'newfile.jpg',newImg)

def displayImg(newImg):
    time.sleep(2)
    cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)
    cv2.imshow('Image', newImg)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

def flipImg(newImg):
    check = False
    while(1):
        if(check):
            print(" \n WRONG INPUT. TRY AGAIN.\n")
        print(" " + dash)
        print('{:<52s}{:>6s}'.format(' |  Options'," |  Code |"))
        print(" " + dash)
        print('{:<53s}{:>6s}'.format(" |  Flip Vertically","|   1   |"))
        print('{:<53s}{:>6s}'.format(" |  Flip Horizontally","|   2   |"))
        print(" " + dash)
        response = int(input("\n Enter Your Response : "))
        if(response == 1):
            flippedImg = cv2.flip(newImg, 0)
            break
        elif(response == 2):
            flippedImg = cv2.flip(newImg, 1)
            break
        else:
            check = True
    displayImg(flippedImg)
    return flippedImg

def resizeImg(newImg):
    ratio = int(input(" Enter the Ratio : "))
    resized = cv2.resize(newImg, (newImg.shape[0]//ratio,newImg.shape[1]//ratio))
    displayImg(resized)
    return resized

def rotateImg(newImg):
    check = False
    while(1):
        if(check):
            print(" \n WRONG INPUT. TRY AGAIN.\n")
        print(" " + dash)
        print('{:<52s}{:>6s}'.format(' |  Options'," |  Code |"))
        print(" " + dash)
        print('{:<53s}{:>6s}'.format(" |  Rotate Clock Wise 90 ","|   1   |"))
        print('{:<53s}{:>6s}'.format(" |  Rotate Anti-Clock Wise 90 ","|   2   |"))
        print('{:<53s}{:>6s}'.format(" |  Rotate 180 ","|   3   |"))
        print(" " + dash)
        response = int(input("\n Enter Your Response : "))
        if(response == 1):
            rotated = cv2.rotate(newImg, cv2.ROTATE_90_CLOCKWISE)
            break
        elif(response == 2):
            rotated = cv2.rotate(newImg, cv2.ROTATE_90_COUNTERCLOCKWISE)
            break
        elif(response == 3):
            rotated = cv2.rotate(newImg, cv2.ROTATE_180)
            break
        else:
            check = True
    displayImg(rotated)
    return rotated

def greyscale(newImg):
    check = False
    while(1):
        if(check):
            print(" \n WRONG INPUT. TRY AGAIN.\n")
        print(" " + dash)
        print('{:<52s}{:>6s}'.format(' |  Options'," |  Code |"))
        print(" " + dash)
        print('{:<53s}{:>6s}'.format(" |  Convert to Black and White","|   1   |"))
        print('{:<53s}{:>6s}'.format(" |  Convert to RGB","|   2   |"))
        print('{:<53s}{:>6s}'.format(" |  Convert to HSV","|   3   |"))
        print(" " + dash)
        response = int(input("\n Enter Your Response : "))
        if(response == 1):
            greyImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)
            break
        elif(response == 2):
            greyImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB)
            break
        elif(response == 3):
            greyImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2HSV)
            break
        else:
            check = True
    displayImg(greyImg)
    return greyImg

def welcome_screen():
    changeCount = 0
    check = False
    newImg = img
    while(1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" "+'*' * (width-1))
        print(welcome_message.center(width-len(welcome_message)+20))
        print("\n EXIT CONSOL TO SAVE CHANGES\n")
        if (check):
            print(" WRONG INPUT. TRY AGAIN.")
        print(" " + dash)
        print('{:<52s}{:>6s}'.format(' |  Options'," |  Code |"))
        print(" " + dash)
        print('{:<53s}{:>6s}'.format(" |  Display Image","|   1   |"))
        print('{:<53s}{:>6s}'.format(" |  Resize Image","|   2   |"))
        print('{:<53s}{:>6s}'.format(" |  Rotate Image","|   3   |"))
        print('{:<53s}{:>6s}'.format(" |  Flip Image","|   4   |"))
        print('{:<53s}{:>6s}'.format(" |  Change Colorscale","|   5   |"))
        print('{:<53s}{:>6s}'.format(" |  Exit ","|   6   |"))
        print(" " + dash)
        response = input("\n Enter Your Response : ")
        print(" ")
        if(response == '1'):
            displayImg(newImg)
        elif(response == '2'):
            changeCount = changeCount + 1
            newImg = resizeImg(newImg)
        elif(response == '3'):
            changeCount = changeCount + 1
            newImg = rotateImg(newImg)
        elif(response == '4'):
            changeCount = changeCount + 1
            newImg = flipImg(newImg)
        elif(response == '5'):
            changeCount = changeCount + 1
            newImg = greyscale(newImg)
        elif(response == '6'):
            if(changeCount > 0):
                saveImg(newImg)
                exitpg(1)
            else:
                exitpg(0)
            
        else:
            check = True
        
if __name__ == '__main__':
    welcome_screen()
