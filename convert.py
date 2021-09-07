from settings import *
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import os



def convertAndCompressPdf(file, OUTPUT_DIR=None):
    # take images from pdf
    images = convert_from_path(file, dpi=DPI_TMP_IMAGE, poppler_path=pooper_path, grayscale=GRAYSCALE)

    # take file name and extension
    filename = os.path.splitext(os.path.basename(file))[0]

    # did dir for tmp img exist?
    if os.path.exists(tmpimagefolder):
        pass
    else:
        os.mkdir(tmpimagefolder)
    delthis = os.path.realpath(tmpimagefolder)

    # saving and compress image to tmp dir
    # saving files name in dirs
    saved_img = []
    for i in range(len(images)):
        image = images[i]
        if i < 10:
            image.save(tmpimagefolder + 'image0' + str(i) + '.jpg', 'JPEG', quality=QUALITY)
            saved_img.append('image0' + str(i) + '.jpg')
        else:
            image.save(tmpimagefolder + 'image' + str(i) + '.jpg', 'JPEG', quality=QUALITY)
            saved_img.append('image' + str(i) + '.jpg')

    images_compressed = []
    for el in saved_img:
        el = Image.open(tmpimagefolder + el)
        images_compressed.append(el)

    # Writting total file. if output we put it this folder. else in input folder
    if OUTPUT_DIR:
        filename = OUTPUT_DIR +'\\' + filename + '.pdf'
    elif OVERWRITE:
        filename = os.path.realpath(os.path.dirname(file)) +'\\' + filename +'.pdf'
    else:
        filename = os.path.realpath(os.path.dirname(file)) +'\\' + filename +'__compressed.pdf'
    print(filename)

    images_compressed[0].save(filename, save_all=True, resolution=DPI, append_images=images_compressed[1:])


    # delete all temporary files
    for el in saved_img:
        os.remove(delthis + '\\' + el)
    os.rmdir(delthis)
    testtest(file)





