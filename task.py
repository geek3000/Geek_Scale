from PIL import Image
import os, PIL

def convert_to_png(file):
    img = Image.open(file)
    img=img.convert('RGB')
    return img

def scale_img(img_path, output_path, file_name):
    baseheight = 400
    img = Image.open(img_path)
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)

    output_file=output_path+"/resized_"+file_name
    img.save(output_file, optimize=True, quality=95)


print("GEEK123 Use me to scale image")

path=input("Enter the path of the directory: ")
if os.path.exists(path):
    output_path=path+'/output'
    try:
        
        os.mkdir(output_path)
    except:
        pass
        print("Output path already exist")
    for file in os.listdir(path):
        if file.endswith(".png") or file.endswith(".jpg"):
            img_path=path+'/'+file
            print("Scaling "+img_path)
            scale_img(img_path, output_path, file)
    print("End scaling images")

