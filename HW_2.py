# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:59:02 2020

@author: 陳彥儒
"""

from PIL import Image,ImageDraw
import matplotlib as plt

def main():
    dog_original = Image.open("dog.jpg")
    width,height = dog_original.size
    
    dog_gray = dog_original.convert('L')
    dog_gray.save('gray_dog.jpg')
    #plt.imshow(dog_gray)
    
    #Laplacian Image
    
    Laplacian = Image.new("L",(width,height))
    draw_img = ImageDraw.Draw(Laplacian)
    for i in range(0,width-2):
        for j in range(0,height-2):
           pixel = Laplacian_Img(dog_gray,i,j)
           draw_img.point((i,j),fill=(pixel))
   
    Laplacian.save('Laplacian_img.jpg')
    
    #Laplacian Image+Original Image>>noise
    
    Noise= Image.new("L",(width,height))
    draw_img = ImageDraw.Draw(Noise)
    for i in range(0,width):
        for j in range(0,height):
            pixel = dog_gray.getpixel((i,j))+Laplacian.getpixel((i,j))
            if pixel > 255: 
                pixel = 255 
            elif pixel < 0: 
                pixel = 0   
            draw_img.point((i,j),fill=(pixel))
    Noise.save('Noise.jpg')
          
    #sobel   
    Sobel = Image.new("L",(width,height))
    draw_img = ImageDraw.Draw(Sobel)                   
    for i in range(0,width-2):
        for j in range(0,height-2):
            pixel = Sobel_Img(dog_gray,i,j)
            draw_img.point((i,j),fill=(pixel))
    Sobel.save('Sobel.jpg')
    
    #Blur
    Blur = Image.new("L",(width,height))
    draw_img = ImageDraw.Draw(Blur)                   
    for i in range(0,width-2):
        for j in range(0,height-2):
            pixel = Blur_Img(Sobel,i,j)
            draw_img.point((i,j),fill=(pixel))
     
    Blur.save('Blur.jpg')   
    
    #Normalization
    Normal = Image.new("L",(width,height))
    draw_img = ImageDraw.Draw(Normal)                   
    for i in range(0,width):
        for j in range(0,height):
            pixel = int((Blur.getpixel((i,j))/255) * Laplacian.getpixel((i,j)))
            
            
            #print(pixel)
            draw_img.point((i,j),fill=(pixel))
    
    Normal.save('Normalization.jpg')
    #Final_img
    Final = Image.new("L",(width,height))
    draw_img = ImageDraw.Draw(Final)
    for i in range(0,width):
        for j in range(0,height):
            pixel = Normal.getpixel((i,j))+dog_gray.getpixel((i,j))
            if pixel > 255: 
               
                pixel = 255 
            elif pixel < 0: 
                
                pixel = 0
            #print(pixel)
            draw_img.point((i,j),fill=(pixel))
    Final.save('Final.jpg')
def Blur_Img(dog,x,y):
    pixel = []
    for i in range(0,3):
        for j in range(0,3):
            image  = dog.getpixel((x+j,y+i))
            pixel.append(image)
            
    result = int((1/9)*(pixel[0]*1+pixel[1]*1+pixel[2]*1+
              pixel[3]*1+pixel[4]*1+pixel[5]*1+
              pixel[6]*1+pixel[7]*1+pixel[8]*1))
    if result > 255: 
        result = 255      
    elif result < 0:        
        result = 0
    
    return result        
def Laplacian_Img(dog,x,y):
    pixel = []
    for i in range(0,3):
        for j in range(0,3):
            image  = dog.getpixel((x+j,y+i))
            pixel.append(image)
   
    result = (pixel[0]*-1+pixel[1]*-1+pixel[2]*-1+
              pixel[3]*-1+pixel[4]*8+pixel[5]*-1+
              pixel[6]*-1+pixel[7]*-1+pixel[8]*-1)
    #print(result)
    
    if result > 255:      
        result = 255       
    elif result < 0:        
        result = 0
    
    return result

def Sobel_Img(dog,x,y):
    pixel = []
    for i in range(0,3):
        for j in range(0,3):
            image  = dog.getpixel((x+j,y+i))
            pixel.append(image)
    result = abs(pixel[0]*-1+pixel[1]*-2+pixel[2]*-1+
                 pixel[3]*0+pixel[4]*0+pixel[5]*0+
                 pixel[6]*1+pixel[7]*2+pixel[8]*1)+ \
             abs(pixel[0]*-1+pixel[1]*0+pixel[2]*1+
                 pixel[3]*-2+pixel[4]*0+pixel[5]*2+
                 pixel[6]*-1+pixel[7]*0+pixel[8]*1)
    if result > 255:    
        result = 255        
    elif result < 0:       
        result = 0  
    return result
            
    
if __name__ =='__main__':
    main()
    


