import sys, os, time, shutil
import numpy as np
from math import ceil
from scipy import ndimage as ndi

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from PIL import Image as pil
from PIL import ImageChops

import skimage as sk
from skimage.measure import compare_ssim as ssim
from skimage.filters import gaussian
from skimage.measure import label
from skimage.measure import regionprops
from skimage.transform import rescale, resize

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#trim method takes out white borders on top and bottom of passed in image
#returns the cropped version of the image
def trim(im):
    bg = pil.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#show function will show the image array passed to it in greyscale
def show(im):
    plt.imshow(im, cmap='gray', interpolation='nearest')
    plt.show()


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#thresh_otsu method takes an image array and returns binary image array where
#all pixels above amt are white and below/equal to amt are black
def thresh_otsu(im, amt):
    im = im > amt
    im = sk.img_as_float(im)
    im = im*255
    return im


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
def sort_by_name():
    srcOld = 'D:\\Screenshots - Copy\\IG\\old\\'
    srcNew = 'D:\\Screenshots - Copy\\IG\\new\\'
    dest = 'D:\\Screenshots - Copy\\IG\\sorted\\'

    allPics = os.listdir(srcOld)
    for x, p in enumerate(allPics):
        try:
            name = get_name_and_pic(srcOld+p)[0]
            if name == '':
                name = 'ERROR'
            if not os.path.isdir(dest+name):
                os.makedirs(dest+name)
            shutil.copy(srcOld+p, dest+name+'\\'+p)

        except Exception as e:
            if not os.path.isdir(dest+'ERROR'):
                os.makedirs(dest+'ERROR')

            shutil.copy(srcOld+p, dest+'ERROR\\'+p)

        if x%10==0 or x%(len(allPics)-1)==0:
            print('Processed OLD: '+str(x+1)+' out of '+ str(len(allPics)))


    allPics = os.listdir(srcNew)
    for x, p in enumerate(allPics):
        try:
            name = get_name_and_pic(srcNew+p)[0]
            if name == '':
                name = 'ERROR'
            if not os.path.isdir(dest+name):
                os.makedirs(dest+name)
            shutil.copy(srcNew+p, dest+name+'\\'+p)
            
        except Exception as e:
            if not os.path.isdir(dest+'ERROR'):
                os.makedirs(dest+'ERROR')
            shutil.copy(srcNew+p, dest+'ERROR\\'+p)
            
        if x%10==0 or x%(len(allPics)-1)==0:
            print('Processed NEW: '+str(x+1)+' out of '+ str(len(allPics)))

            
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#separate_instas function will separate all(99.9%) the instagram screenshots 
#from non-instagram screenshots. Further into old and new instagram formats
def separate_instas():
    src = 'D:\\Screenshots - Copy\\'
    dest = src+'IG\\'
    non = src+'non\\'
    
    dirs = [dest, non, dest+'old', dest+'new']
    for d in dirs:
        if not os.path.isdir(d):
            os.makedirs(d)

    allPics = os.listdir(src)
    for x, pic in enumerate(allPics):
        if os.path.isfile(src+pic):
            if is_insta_screenshot(src+pic) == 1:
                shutil.copy(src+pic, dest+'old\\'+pic)
            elif is_insta_screenshot(src+pic) == 2:
                shutil.copy(src+pic, dest+'new\\'+pic)
            elif is_insta_screenshot(src+pic) == 0:
                shutil.copy(src+pic, non+pic)
        
        if x%25==0:
            print('Processed: '+str(x)+' out of '+ str(len(allPics)))


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#get_formats iterates through the path and based on the bottom portion of
#the screenshot, collects the most common "formats". Instagram screenshots all
#have a utility bar at the bottom. All variations of bar are saved for later use
def get_formats():
    #switch will change the otsu threshold and the crop size of bottom 
    switch = 'Screenshot_2016-05-11-17-36-20.png'
    path = 'D:\\Screenshots - Copy\\'
    allPics = os.listdir(path)
    formats = []
    amounts = []
    botSize = 168
    otsu = 100
    
    for num, pic in enumerate(allPics):
        if pic == switch:
            botSize = 144
            otsu = 204

        #read image as array, crop out bottom
        im = ndi.imread(path+pic, flatten=True)
        imm = im[im.shape[0]-botSize:][:]
        imm = thresh_otsu(imm,otsu)
        
        #add the first format into empty list
        if len(formats) == 0:
            formats.append(imm)
            amounts.append(1)
        else:
            #for loop will iterate through all formats to check if imm is in the list
            for idx, f in enumerate(formats):
                f = thresh_otsu(f,otsu)
                inList = False
                
                #resize smaller crop, need same dimmensions to compare
                if imm.shape != f.shape:
                    imm = (resize(imm/255,f.shape))*255
                #must match any format in the list by at least 93%
                if get_ssim(f,imm,readPaths=False) > 0.93:
                    inList = True                    
                    amounts[idx] += 1
                    break

            #if imm was not matched to a format, add it as a new one
            #limit of 5 (except switch) different formats or else VERY SLOW
            if ((not inList) and (len(formats)<5)) or pic == switch:
                formats.append(imm)
                amounts.append(1)

        #print progress every 10 pics
        if(num%100==0):
              print('Complete: '+str(num)+' out of '+str(len(allPics))+' - LEN: '+str(len(formats)))
        elif(num%10==0):
            print('Complete: '+str(num)+' out of '+str(len(allPics)))
            
    for idx, f in enumerate(formats):
        if amounts[idx] > 1:
            i = pil.fromarray(np.uint8(f))
            i.save('C:\\Users\\Igor\\Documents\\Python\\ProjectsAndScripts\\IGE\\Formats\\'+str(amounts[idx])+' - '+str(int(time.time())+idx)+'.png')

    return formats
  

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#is_insta_screenshot method will return True if the screenshot passed to it
#has the bottom instagram toolbar. This indicates that the screenshot is of IG
def is_insta_screenshot(img,readPath=True, boolean=False):

    #0 - NOT INSTA
    #1 - OLD FORMAT
    #2 - NEW FORMAT
    format1 = 'C:\\Users\\Igor\\Documents\\Python\\ProjectsAndScripts\\IGE\\Formats\\1-456.png'
    format2 = 'C:\\Users\\Igor\\Documents\\Python\\ProjectsAndScripts\\IGE\\Formats\\2-2764.png'

    im = ndi.imread(img, flatten=True)
    format1 = ndi.imread(format1, flatten=True)
    format2 = ndi.imread(format2, flatten=True)

    #Try to match format 1
    imm = im[im.shape[0]-168:][:]
    imm = thresh_otsu(imm,100)
    if get_ssim(format1,imm,readPaths=False) > 0.93:
        if boolean:
            return True
        return 1

    #Try to match format 2
    imm = im[im.shape[0]-144:][:]
    imm = thresh_otsu(imm,204)
    imm = (resize(imm/255,format1.shape))*255
    if get_ssim(format2,imm,readPaths=False) > 0.93:
        if boolean:
            return True
        return 2    

    return False if boolean else 0


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#get_ssim will return a float value (0.0-1.0)
#indicating how similar img1 and img2 are
def get_ssim(img1, img2, readPaths=True, otsu=-1, assist=False, gauss=0, rs=0):

    if readPaths:
        im1 = ndi.imread(img1, flatten=True)
        im2 = ndi.imread(img2, flatten=True)
    else:
        im1 = img1
        im2 = img2

    if otsu > 0:
        im1 = thresh_otsu(im1,otsu)
        im2 = thresh_otsu(im2,otsu)
    
    im1 = im1/255
    im1 = sk.img_as_float(im1)
    im2 = im2/255
    im2 = sk.img_as_float(im2)

    if assist==True:
        gauss = 1
        rs = 0.5
    
    if rs > 0:
        im1 = rescale(im1, rs)
        im2 = rescale(im2, rs)
    if gauss > 0:
        im1 = gaussian(im1, gauss)
        im2 = gaussian(im2, gauss)
    
    label = '{0:.2f}'.format(ssim(im1, im2)*100)
    #print('SSIM: ' + label +'%')

    return ssim(im1,im2)


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
def get_name():
    return None
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
def get_pic():
    return None
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
def get_both():
    return None
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
def draw_boxes(regions, src):
    return None
         
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#all_regions will extract the region with the name and the region with the picture
#from the list of passed in regions
#draw=True will draw a box around the discovered name and pic regions
#drawAll=True will draw a box around all discovered regions
#im is the image to draw 
def all_regions(regions, im=None, draw=True, drawAll=False):

    #draw makes box around name and pic
    #drawAll makes box around all found regions
    #both false = return name and pic regions
    if draw or drawAll:
        if im == None:
            print('Cannot draw without image parameter')
            draw = False
            drawAll = False
        else:
            fig, ax = plt.subplots(ncols=1, nrows=1)
            ax.imshow(im, cmap='gray', interpolation='nearest')

    nameRegs=[]
    for reg in regions:
        minr, minc, maxr, maxc = reg.bbox

        #Expand region a little bit. Avoids text pixel clipping
        minr -= 1 
        minc -= 1
        maxr += 2
        maxc += 5

        #Scale region by 4 (original image downsized by 4)
        minr *= 4
        minc *= 4
        maxr *= 4
        maxc *= 4

        blen = maxc - minc
        bhigh = maxr - minr

        #drawAll switch draws all regions, exits
        if drawAll:
            print(str(minr)+ ', '+str(minc)+ ', '+str(maxr)+ ', '+str(maxc))
            print('Dim: ' + str(blen) + ' x ' + str(bhigh))
            print('------------------------')
            rect = mpatches.Rectangle((minc,minr), blen, bhigh, fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)
        
        #This will find the the name region (will be long and not very tall
        if minc > 125 and minc < 200 and minr < 500 and bhigh >= 45 and bhigh <=100 and blen >=80 and blen <= 830 and regions.index(reg) < 10:
            print('Added Name!')
            print()
            nameRegs.append(reg)
            if draw:
                rect = mpatches.Rectangle((minc,minr), blen, bhigh, fill=False, edgecolor='red', linewidth=2)
                ax.add_patch(rect)
        #This will find the picture region
        #TODO - Images could be shorter than 750
        if blen >= 500 and bhigh >= 500:
            print('Added Pic!')
            print()
            picReg = reg
            if draw:
                rect = mpatches.Rectangle((minc,minr), blen, bhigh, fill=False, edgecolor='red', linewidth=2)
                ax.add_patch(rect)
  
    if drawAll or draw:
        plt.show()

    
    return nameRegs[0], picReg
    



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#    
#get_name_and_pic will take in a source instagram screenshot
#and return a string of who posted it as well as the cropped image
#savePic will save the picture to dest path
#saveAll will save high-res pic, low-res icon and cropped name text
#drawAll will draw a box around all discovered regions of the screenshot
def get_name_and_pic(src='', dest='', img=None, readPath=True, savePic=False, saveAll=False, drawAll=False, draw=False, showSteps=False):
    
    #try:
    if src == '' and img == None:
        print('No image given.')
        return None
    if readPath:
        im = ndi.imread(src, flatten=True)
    else:
        im = img

    #Convert from float(0.0 - 255.0) to float(0.0 - 1.0)
    im = im/255
    im = sk.img_as_float(im)

    #Downsize to reduce number of pixels (helps gaussian + otsu)
    ims = rescale(im, 0.5)
    ims = rescale(ims, 0.5)
    
    #Otsu, blur to spread pixels, otsu once more to create larger 'blobs'
    if showSteps:
        show(ims)
    imss = ims > 0.85
    if showSteps:
        show(imss)
    imss = gaussian(imss, 1.5)
    if showSteps:
        show(imss)
    imss = imss > 0.85
    if showSteps:
        show(imss)

    #Create and store all regions of black
    labelImage = label(imss, connectivity=2, background=1)
    regions = regionprops(labelImage)

    #Extract name and picture regions
    try:
        if drawAll == True:
            nameRegion, picRegion = all_regions(regions, im=im, drawAll=True)
        elif draw == True:
            nameRegion, picRegion = all_regions(regions, im=im, draw=True)
        else:
            nameRegion, picRegion = all_regions(regions)
    except IndexError:
        return [None,None]
    nameRegion = nameRegion.bbox
    picRegion = picRegion.bbox

    #Regions' bbox is ((y,x)(y,x)). Switch to ((x,y)(x,y)).*4 to resize bbox to proper resolution
    nameRegion = (nameRegion[1]*4,nameRegion[0]*4,nameRegion[3]*4,nameRegion[2]*4)
    picRegion = (picRegion[1]*4,picRegion[0]*4,picRegion[3]*4,picRegion[2]*4)

    #Open and crop out name and pic as new images
    if readPath:
        toCrop = pil.open(src)
    else:
        toCrop = pil.fromarray(np.uint8(img))
    name = toCrop.crop(nameRegion)
    pic = toCrop.crop(picRegion)
    picNoBord = trim(pic)

    #Calculate new icon resolution and make icon
    iconW, iconH = picNoBord.size
    iconH = ceil(iconH/9)
    iconW = ceil(iconW/9)
    picIcon = picNoBord.resize((iconW,iconH), pil.ANTIALIAS)
    
    #saves picture, name image and icon
    if savePic or saveAll:
        if dest == '':
            print('Cannot save without destination directory')
        else:
            picFile = dest + 'Pic - ' + src.split('\\')[-1]
            picNoBord.save(picFile)
            if saveAll:
                nameFile = dest + 'Name - ' + src.split('\\')[-1]
                name.save(nameFile)
                picIcon.save(dest + 'Icon - ' + src.split('\\')[-1])

    #OCR will parse name image and return name string 
    nametxt = pytesseract.image_to_string(name)
    nametxt = nametxt.replace('|','l')
    nametxt = nametxt.split('\n')[0]
    
    if nametxt == 'Photo' or nametxt == 'â€˜lmtagnam':
        im = ndi.imread(src, flatten=True)
        im = im[219:][:]
        return get_name_and_pic(src, img=im, dest=dest, readPath=False, saveAll=saveAll, drawAll=drawAll)
    
    #print(nametxt)
    return ([nametxt,picIcon])
    #except Exception as e:
        #print('Error ocurred: %s' %e)
        #return None
        

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-MAIN=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#'Yes' if fruit == 'Apple' else 'No'

if __name__ == '__main__':

    path = 'D:\\Screenshots - Copy\\IG\\sorted\\ERROR\\'
    pics = os.listdir(path)
    print(pics)
    for p in pics:
        try:
            name = get_name_and_pic(path+p,draw=True, saveAll=True, dest='D:\\new\\')[0]
            print(name)
        except UnicodeDecodeError:
            d = 'D:\\Screenshots - Copy\\IG\\Errs\\'
            for f in os.listdir(d):
                i1 = ndi.imread(d+f, flatten=True)
                show(i1)
                i2 = ndi.imread('D:\\new\\Name - '+p, flatten=True)
                show(i2)
                if i2.shape != i1.shape:
                    i2 = (resize(i2/255,i1.shape))*255
                ss = get_ssim(i1, i2, readPaths=False)
                print(ss)
                if ss > 0.93:
                    print(ss)
                    print('Needs move. Name: '+f.split('.')[0])
                else:
                    print('Nah')

        except Exception as e:
            print('Totally fucked: %s' %e)
                    
        #print(get_name_and_pic(path+p,draw=True)[0])
    #sort_by_name()
    sys.exit(0)
      
    src = 'C:\\Users\\Igor\\Documents\\Python\\Pics\\Python Pics\\for\\img (1).png'
    dest ='D:\\Screenshots - Copy\\IG\\New F\\'
    #namet, pic = get_name_and_pic(src, dest, savePic=True)

    im1 = dest+'Pic - img (1).png'
    im2 = dest+'iconbig.jpg'

    path = 'D:\\Screenshots - Copy\\IG\\New Folder\\'
    pics = os.listdir(path)

    for p in pics:
        get_name_and_pic(path+p, dest, saveAll=True, drawAll=True)
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

    
'''
-----PLAN-----

X - extract from screenshot: name and picture regions
X - bounding box coords serve as crop markers for pic and name
X - crop the name out of the screenshot (will only work for one format of screenshot)
X - crop the pic out of the screenshot
X - if there is a location in name, divide further (OCR will divide separate lines with \n)
X - convert the name to text using OCR
X - downsize image to smaller resolution (get icon size of insta pics)

X - make above work for all formats
X - top bar to be cropped (wifi, time etc)

 - Visit profile using name
 - Get date modified of original pic
 - Go down insta profile until reaching date
 - Search +/- several days, comparing thumbnails
 - if not found with date method, keep going until end of pics
 - if not found again, throw error
 - if found, collect all data and store in a database

--------------
'''
