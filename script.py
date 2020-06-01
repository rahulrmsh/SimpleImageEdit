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

def exitpg():
    print(" ")
    print(exit_message.center(width-len(exit_message)))
    print(" "+'*' * (width-1))
    exit(0)

def displayImg(img):
    cv2.namedWindow('Image', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('Image', img)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

def flipImg(img):
    flippedImg = cv2.flip(img, 1)
    displayImg(flippedImg)
    cv2.imwrite(location+'/'+'newfile.jpg',flippedImg)    

def resizeImg(img):
    ratio = int(input(" Enter the Ratio : "))
    resized = cv2.resize(img, (img.shape[0]//ratio,img.shape[1]//ratio))
    displayImg(resized)
    cv2.imwrite(location+'/'+'newfile.jpg',resized)

def rotateImg(img):
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    displayImg(rotated)
    cv2.imwrite(location+'/'+'newfile.jpg',rotated)

def greyscale():
    greyImg = cv2.imread(sys.argv[1], 0)
    displayImg(greyImg)
    cv2.imwrite(location+'/'+'newfile.jpg',greyImg)
    
def getImage():
    img = cv2.imread(sys.argv[1], 1)
    return img

def welcome_screen():
    check = False
    while(1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" "+'*' * (width-1))
        print(welcome_message.center(width-len(welcome_message)))
        print("\n\n")
        if (check):
            print(" WRONG INPUT. TRY AGAIN.")
        print(" " + dash)
        print('{:<52s}{:>6s}'.format(' |  Options'," |  Code |"))
        print(" " + dash)
        print('{:<53s}{:>6s}'.format(" |  Display Image","|   1   |"))
        print('{:<53s}{:>6s}'.format(" |  Resize Image","|   2   |"))
        print('{:<53s}{:>6s}'.format(" |  Rotate Image","|   3   |"))
        print('{:<53s}{:>6s}'.format(" |  Flip Image","|   4   |"))
        print('{:<53s}{:>6s}'.format(" |  Change Greyscale","|   5   |"))
        print('{:<53s}{:>6s}'.format(" |  Exit ","|   6   |"))
        print(" " + dash)
        response = input("\n Enter Your Response : ")
        if(response == '1'):
            displayImg(img)
        elif(response == '2'):
            resizeImg(img)
        elif(response == '3'):
            rotateImg(img)
        elif(response == '4'):
            flipImg(img)
        elif(response == '5'):
            greyscale()
        elif(response == '6'):
            exitpg()
        else:
            check = True
        
def load_animation(string_input, animation_input, final_count, speed, controller): 
    load_str = string_input
    animation = animation_input
    anicount = 0
    counttime = 0        
    i = 0                     
    while (counttime != final_count): 
        time.sleep(speed)  
        sys.stdout.write("\r"+ load_str + animation[anicount]+"\t") 
        sys.stdout.flush() 
        anicount = (anicount + 1)% len(animation_input)
        counttime = counttime + 1
    if(controller == 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        
if __name__ == '__main__':
    welcome_screen()
    

