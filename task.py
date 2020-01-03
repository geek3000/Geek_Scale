from PIL import Image
import os, PIL

def convert_to_png(file):
    img = Image.open(file)
    img=img.convert('RGB')
    return img

def scale_img(img, path, file_name):
    baseheight = 400
    
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)

    output_file=output_path+"/resized_"+file_name+'.jpg'
    img.save(output_file, optimize=True, format='JPEG', quality=90)

    size=0
    with open(output_file, 'rb') as q:
        t=q.read()
        size=len(t)
        
    if(size<64000):
        img.save(output_file, optimize=True, format='JPEG', quality=60)

print("GEEK123 Use me to scale image")

path=input("Enter the path of the directory: ")
if os.path.exists(path):
    try:
        output_path=path+'/output'
        os.mkdir(output_path)
    except:
        pass
        print("Output path already exist")
    for file in os.listdir(path):
        if file.endswith(".png"):
            img_path=path+'/'+file
            print("Scaling "+img_path)
            img=convert_to_png(img_path)
            scale_img(img, path, file.split('.')[0])
    print("End scaling images")

