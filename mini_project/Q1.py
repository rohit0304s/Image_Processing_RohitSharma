from tkinter import *
import tkinter as tk
from tkinter import filedialog,Text
from PIL import Image,ImageTk
import cv2
import numpy as np
import pytesseract as pt
from pytesseract import Output

og_img=np.zeros((),np.uint8)
text=''
counter=0
my_image=np.zeros((),np.uint8)

root=tk.Tk()
canvas=tk.Canvas(root,height=700,width=700,bg='#6FA2BF')
canvas.pack()
frame=tk.Frame(root,bg='white')
frame.place(relwidth=0.6,relheight=0.9,relx=0.2,rely=0.05)
text_box=tk.Frame(frame,bg='#FDACD6')
text_box.place(relwidth=0.6,relheight=0.6,relx=0.2,rely=0.2)

def open_btn_clicked():
    filename = filedialog.askopenfilename(initialdir = 'E:\\',title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    print(filename)
    global og_img,my_image
    og_img = cv2.imread(filename)
    #og_img=cv2.resize(img,(640,640))
    my_image=og_img.copy()
    cv2.imshow('frame',og_img)
    cv2.waitKey(0)

def blur_btn_clicked():
    global my_image
    img_gray=cv2.cvtColor(og_img,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((2,2))
    gaussian_blur=cv2.GaussianBlur(img_gray,(5,5),2)
    my_image=gaussian_blur.copy()
    cv2.imshow('frame',gaussian_blur)

def auto_btn_clicked():
    global my_image
    image=cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((2,2))
    gaussian_blur=cv2.GaussianBlur(image,(5,5),2)
    edge=cv2.Canny(gaussian_blur,150,200)
    contours,heirarchy=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour=contours[max_index]
    perimeter=cv2.arcLength(max_contour,True)
    ROI=cv2.approxPolyDP(max_contour,0.01*perimeter,True)
    pts_1=np.array([ROI[0],ROI[1],ROI[3],ROI[2]],np.float32)
    pts_2=np.array([(0,0),(500,0),(0,500),(500,500)],np.float32)
    perspective=cv2.getPerspectiveTransform(pts_1,pts_2)
    transformed=cv2.warpPerspective(my_image,perspective,(500,500))
    my_image=transformed.copy()
    cv2.imshow('frame',transformed)

def manual_btn_clicked():
    pts=[]
    def mouse(event,x,y,flags,param):
        global my_image
        if event==cv2.EVENT_LBUTTONDOWN:
            pts.append((x,y))
        if len(pts)==4:
            warp(pts)
    def warp(pts):
        global my_image
        pts_1=np.array([pts[0],pts[1],pts[3],pts[2]],np.float32)
        pts_2=np.array([(0,0),(400,0),(0,400),(400,400)],np.float32)
        perspective=cv2.getPerspectiveTransform(pts_1,pts_2)
        transformed=cv2.warpPerspective(og_img,perspective,(400,400))
        my_image=transformed.copy()
        cv2.imshow('frame',transformed)
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame',mouse)

def ocr_btn_clicked():
    pt.pytesseract.tesseract_cmd=r'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python37\\Tesseract-OCR\\tesseract.exe'
    global my_image,text
    ret,global_thresh=cv2.threshold(my_image,170,255,cv2.THRESH_BINARY)
    text = pt.image_to_string(global_thresh,lang= 'eng')
    data = pt.image_to_data(global_thresh,output_type= Output.DICT)
    no_word = len(data['text'])
    for i in range(no_word):
        if int(data['conf'][i]) > 50:
            x,y,w,h = data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(global_thresh,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow('frame',global_thresh)
            cv2.waitKey(200)
    my_image=global_thresh.copy()

def show_btn_clicked():
    global text
    textbox = tk.Frame(frame,bg = '#FDFFD6')
    textbox.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
    text_frame = Text(textbox,bg = '#FDFFD6')
    text_frame.insert('1.0',text)
    text_frame.pack()

def save_btn_clicked():
    global counter
    global my_image
    counter+=1
    cv2.imwrite('image_'+str(counter) + '.jpg', my_image)

def og_btn_clicked():
    global my_image
    my_image=og_img.copy()
    cv2.imshow('frame',og_img)

def destroy_btn_clicked():
    cv2.destroyAllWindows()

def rotate_btn_clicked():
    global my_image
    image_90=cv2.rotate(my_image,cv2.ROTATE_90_CLOCKWISE)
    my_image=image_90.copy()
    cv2.imshow('frame',image_90)

def resize_btn_clicked():
    global my_image
    x=int(input('enter width pixel'))
    y=int(input('enter height pixel'))
    resize=cv2.resize(my_image,(x,y))
    my_image=resize.copy()
    cv2.imshow('frame',resize)

label=tk.Label(frame,text='Detected Text',fg='green',bg='white',font=('Arial',20))
label.place(relx=0.3,rely=0.1)

open_file = tk.Button(canvas,text = 'Open Image',fg = '#FAA65F',padx = 5,pady = 5, command = open_btn_clicked)
open_file.place(relx=0.035,rely=0.05)

blur_image=tk.Button(canvas,text='Blur Image',fg = '#FAA65F',padx = 10,pady = 5, command = blur_btn_clicked)
blur_image.place(relx=0.035,rely=0.2)

auto_crop=tk.Button(canvas,text='Auto Crop Image',fg = '#FAA65F',padx = 10,pady = 5, command = auto_btn_clicked)
auto_crop.place(relx=0.02,rely=0.375)

manual_crop=tk.Button(canvas,text='Manual Crop',fg = '#FAA65F',padx = 10,pady = 5, command = manual_btn_clicked)
manual_crop.place(relx=0.025,rely=0.5)

ocr_btn=tk.Button(canvas,text='OCR',fg = '#FAA65F',padx = 10,pady = 5, command = ocr_btn_clicked)
ocr_btn.place(relx=0.85,rely=0.05)

show_text=tk.Button(canvas,text='Show text',fg = '#FAA65F',padx = 10,pady = 5, command = show_btn_clicked)
show_text.place(relx=0.83,rely=0.2)

save_image=tk.Button(canvas,text='Save Image',fg = '#FAA65F',padx = 10,pady = 5, command = save_btn_clicked)
save_image.place(relx=0.83,rely=0.375)

show_og=tk.Button(canvas,text='Original Image',fg = '#FAA65F',padx = 8,pady = 5, command = og_btn_clicked)
show_og.place(relx=0.82,rely=0.5)

destroy_window=tk.Button(canvas,text='Destroy windows',fg = '#FAA65F',padx = 10,pady = 5, command = destroy_btn_clicked)
destroy_window.place(relx=0.82,rely=0.85)

rotate_image=tk.Button(canvas,text='Rotate Image',fg = '#FAA65F',padx = 10,pady = 5, command = rotate_btn_clicked)
rotate_image.place(relx=0.03,rely=0.7)

resize_image=tk.Button(canvas,text='Resize Image',fg = '#FAA65F',padx = 10,pady = 5, command = resize_btn_clicked)
resize_image.place(relx=0.03,rely=0.875)

root.mainloop()