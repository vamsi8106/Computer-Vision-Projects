import cv2
import math
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"



def threshold(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return threshold_img

def distance_states(l):
    x1=int(l[0])+20
    y1=int(l[1])+5
    x2=int(l[2])+20
    y2=int(l[3])+5
    eDistance = math.dist([x1,y1], [x2,y2])
    cv2.line(img, (x1,y1), (x2,y2), (0, 200, 200), thickness=3, lineType=8)
    print("Distance between TAMILNADU and TELANGANA is :",eDistance)

def find_text(img,threshold_img):
        count=0
        l=[]
        boxes=pytesseract.image_to_data(threshold_img)
        hImg,wImg=threshold_img.shape
        for b in boxes.splitlines():
            
            if count!=0:
                b=b.split()
                #print()
                if len(b)==12:
                    #print(b)
                    x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(img,(x,y),(w+x,y+h),(0,0,255),3)
                    if b[11]=='TAMILNADU':
                        l.append(b[6])
                        l.append(b[7])
                    if b[11]=='TELANGANA':
                        l.append(b[6])
                        l.append(b[7])
                    if len(l)==4:
                        distance_states(l)
                        break   
            count=count+1

if __name__=="__main__":
    img= cv2.imread("india-map.jpg")
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  
    
    threshold_img=threshold(img)
    find_text(img,threshold_img)
    

    cv2.imshow('Result',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  