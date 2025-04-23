import numpy as np
from tensorflow.keras.models import model_from_json
import operator
import cv2
import sys, os
import schedule
import psutil
import serial
import time


ser = serial.Serial('/dev/ttyACM0', 9600,timeout=2)

json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)

# Category dictionary
categories = {0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE","A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}
#Sequence Values.
data = {0:'011100\n',1:'1000000\n',2:'101000\n',3:'110000\n',4:'110100\n',5:'100100\n',6:'111000\n',7:"111100\n",8:"101100\n",9:"011000\n","A":'1000000\n',"B":'101000\n',"C":'110000\n',"D":'110100\n',"E":'100100\n',"F":'111000\n',"G":"111100\n","H":"101100\n","I":"011000\n","J":"011100\n","K":"100010\n","L":"101010\n","M":"110010\n","N":"110010\n","O":"100110\n","P":"111010\n","Q":"111110\n","R":"101110\n","S":"011010\n","T":"011110\n","U":"100011\n","V":"101011\n","W":"011101\n","X":"110011\n","Y":"110111\n","Z":"100111\n"}
send = []
print('The CPU usage is: ', psutil.cpu_percent(4))
delno = 0
p = [""]
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #cordinates of roi.
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # +/- to compensate for the bounding box.
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting ROI
    roi = frame[y1:y2, x1:x2]
    
    roi = cv2.resize(roi, (64, 64)) 
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)
    # Batch of 1
    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
    
    prediction = {0: result[0][0], 
                  1: result[0][1], 
                  2: result[0][2],
                  3: result[0][3],
                  4: result[0][4],
                  5: result[0][5],
                  6: result[0][6],
                  7: result[0][7],
                  8: result[0][8],
                  9: result[0][9],
                  'A': result[0][10],
                  'B': result[0][11],
                  'C': result[0][12],
                  'D': result[0][13],
                  'E': result[0][14],
                  'F': result[0][15],
                  'G': result[0][16],
                  'H': result[0][17],
                  'I': result[0][18],
                  'J': result[0][19],
                  'K': result[0][20],
                  'L': result[0][21],
                  'M': result[0][22],
                  'N': result[0][23],
                  'O': result[0][24],
                  'P': result[0][25],
                  'Q': result[0][26],
                  'R': result[0][27],
                  'S': result[0][28],
                  'T': result[0][29],
                  'U': result[0][30],
                  'V': result[0][31],
                  'W': result[0][32],
                  'X': result[0][33],
                  'Y': result[0][34],
                  'Z': result[0][35],
                  }
    # Sorting based on top prediction
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    p = prediction[0][0]
    p = str(p)
    cv2.putText(frame,p, (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (0,90,270), 3)    
    cv2.imshow("Frame", frame)
    cv2.startWindowThread()
    #sendData(prediction)
    #schedule.every(5).do(sendData(p))
   
    p = str(data[prediction[0][0]])
    #ser.write(txt.encode())    
    time.sleep(0.08)
    try:
        ser.write(p.encode())
        print("Sent")
        ser.flush()
    except:
        print("Sending failed")
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    #print('The CPU usage is: ', psutil.cpu_percent(4))
    
#print(send)


ser.flush()
ser.close()


'''
def send_data(x):
    print("Starting!")
    time.sleep(0.1)
    print(x)
    txt = x
    print(txt.encode())
    ser.write(txt.encode())
    time.sleep(20)
    time.sleep(2)
    print("Done!")
'''

'''
for i in len(send):
    try:
        ser.write(send[i].encode())
        print("Sent")
    except:
        print("Sending failed")
    ser.close()
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
         break
'''
cap.release()
cv2.destroyAllWindows()
