import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/A")
    os.makedirs("data/train/B")
    os.makedirs("data/train/C")
    os.makedirs("data/train/D")
    os.makedirs("data/train/E")
    os.makedirs("data/train/F")
    os.makedirs("data/train/G")
    os.makedirs("data/train/H")    
    os.makedirs("data/train/I")
    os.makedirs("data/train/J")
    os.makedirs("data/train/K")
    os.makedirs("data/train/L")
    os.makedirs("data/train/M")
    os.makedirs("data/train/N")
    os.makedirs("data/train/O")
    os.makedirs("data/train/P")
    os.makedirs("data/train/Q")
    os.makedirs("data/train/R")
    os.makedirs("data/train/S")
    os.makedirs("data/train/T")
    os.makedirs("data/train/U")
    os.makedirs("data/train/V")
    os.makedirs("data/train/W")
    os.makedirs("data/train/X")
    os.makedirs("data/train/Y")
    os.makedirs("data/train/Z")
    
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/train/6")
    os.makedirs("data/train/7")
    os.makedirs("data/train/8")
    os.makedirs("data/train/9")
    
    os.makedirs("data/test/A")
    os.makedirs("data/test/B")
    os.makedirs("data/test/C")
    os.makedirs("data/test/D")
    os.makedirs("data/test/E")
    os.makedirs("data/test/F")
    os.makedirs("data/test/G")
    os.makedirs("data/test/H")
    os.makedirs("data/test/I")
    os.makedirs("data/test/J")
    os.makedirs("data/test/K")
    os.makedirs("data/test/L")
    os.makedirs("data/test/M")
    os.makedirs("data/test/N")
    os.makedirs("data/test/O")
    os.makedirs("data/test/P")
    os.makedirs("data/test/Q")
    os.makedirs("data/test/R")
    os.makedirs("data/test/S")
    os.makedirs("data/test/T")
    os.makedirs("data/test/U")
    os.makedirs("data/test/V")
    os.makedirs("data/test/W")
    os.makedirs("data/test/X")
    os.makedirs("data/test/Y")
    os.makedirs("data/test/Z")
    
    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")
    os.makedirs("data/test/6")
    os.makedirs("data/test/7")
    os.makedirs("data/test/8")
    os.makedirs("data/test/9")


# Train or test 
mode = 'test'
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'A': len(os.listdir(directory+"/A")),
             'B': len(os.listdir(directory+"/B")),
             'C': len(os.listdir(directory+"/C")),
             'D': len(os.listdir(directory+"/D")),
             'E': len(os.listdir(directory+"/E")),
             'F': len(os.listdir(directory+"/F")),
             'G': len(os.listdir(directory+"/G")),
             'H': len(os.listdir(directory+"/H")),
             'I': len(os.listdir(directory+"/I")),
             'J': len(os.listdir(directory+"/J")),
             'K': len(os.listdir(directory+"/K")),
             'L': len(os.listdir(directory+"/L")),
             'M': len(os.listdir(directory+"/M")),
             'N': len(os.listdir(directory+"/N")),
             'O': len(os.listdir(directory+"/O")),
             'P': len(os.listdir(directory+"/P")),
             'Q': len(os.listdir(directory+"/Q")),
             'R': len(os.listdir(directory+"/R")),
             'S': len(os.listdir(directory+"/S")),
             'T': len(os.listdir(directory+"/T")),
             'U': len(os.listdir(directory+"/U")),
             'V': len(os.listdir(directory+"/V")),
             'W': len(os.listdir(directory+"/W")),
             'X': len(os.listdir(directory+"/X")),
             'Y': len(os.listdir(directory+"/Y")),
             'Z': len(os.listdir(directory+"/Z")),
             '0': len(os.listdir(directory+"/0")),
             '1': len(os.listdir(directory+"/1")),
             '2': len(os.listdir(directory+"/2")),
             '3': len(os.listdir(directory+"/3")),
             '4': len(os.listdir(directory+"/4")),
             '5': len(os.listdir(directory+"/5")),
             '6': len(os.listdir(directory+"/6")),
             '7': len(os.listdir(directory+"/7")),
             '8': len(os.listdir(directory+"/8")),
             '9': len(os.listdir(directory+"/9"))}

    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "A: "+str(count['A']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "B: "+str(count['B']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "C: "+str(count['C']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "D: "+str(count['D']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "E: "+str(count['E']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "F: "+str(count['F']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "G: "+str(count['G']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "H: "+str(count['H']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "I: "+str(count['I']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "J: "+str(count['J']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "K: "+str(count['K']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "L: "+str(count['L']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "M: "+str(count['M']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "N: "+str(count['N']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "O: "+str(count['O']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "P: "+str(count['P']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "Q: "+str(count['Q']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "R: "+str(count['R']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "S: "+str(count['S']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "T: "+str(count['T']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "U: "+str(count['U']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "V: "+str(count['V']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "W: "+str(count['W']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "X: "+str(count['X']), (10, 350), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "Y: "+str(count['Y']), (10,360 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "Z: "+str(count['Z']), (10,370 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "0: "+str(count['0']), (10,380 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "1: "+str(count['1']), (10,390 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "2: "+str(count['2']), (10,400 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "3: "+str(count['3']), (10,410 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "4: "+str(count['4']), (10,420 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "5: "+str(count['5']), (10,430 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "6: "+str(count['6']), (10,440 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "7: "+str(count['7']), (10,450 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "8: "+str(count['8']), (10,460 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
    cv2.putText(frame, "9: "+str(count['9']), (10,470 ), cv2.FONT_HERSHEY_PLAIN, 0.7, (0,255,255), 1)
 
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64)) 
 
    cv2.imshow("Frame", frame)
    

    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 180, 250, cv2.ADAPTIVE_THRESH_MEAN_C)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'A/'+str(count['A'])+'.jpg', roi)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'B/'+str(count['B'])+'.jpg', roi)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'C/'+str(count['C'])+'.jpg', roi)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'D/'+str(count['D'])+'.jpg', roi)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'E/'+str(count['E'])+'.jpg', roi)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'F/'+str(count['F'])+'.jpg', roi)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'G/'+str(count['G'])+'.jpg', roi)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'H/'+str(count['H'])+'.jpg', roi)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'I/'+str(count['I'])+'.jpg', roi)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'J/'+str(count['J'])+'.jpg', roi)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'K/'+str(count['K'])+'.jpg', roi)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'L/'+str(count['L'])+'.jpg', roi)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'M/'+str(count['M'])+'.jpg', roi)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'N/'+str(count['N'])+'.jpg', roi)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'O/'+str(count['O'])+'.jpg', roi)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'P/'+str(count['P'])+'.jpg', roi)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory+'Q/'+str(count['Q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'R/'+str(count['R'])+'.jpg', roi)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'S/'+str(count['S'])+'.jpg', roi)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'T/'+str(count['T'])+'.jpg', roi)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'U/'+str(count['U'])+'.jpg', roi)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'V/'+str(count['V'])+'.jpg', roi)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'W/'+str(count['W'])+'.jpg', roi)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'X/'+str(count['X'])+'.jpg', roi)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'Y/'+str(count['Y'])+'.jpg', roi)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory+'Z/'+str(count['Z'])+'.jpg', roi)
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['0'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['1'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['2'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['3'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['4'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['5'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['6'])+'.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['7'])+'.jpg', roi)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['8'])+'.jpg', roi)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['9'])+'.jpg', roi)
    
            
cap.release()
cv2.destroyAllWindows()
