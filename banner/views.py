from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from colorthief import ColorThief
from PIL import Image
from models import Banner
import time
# Create your views here.

def index(request):
    number = Banner.objects.count()
    #number = len(objectList)
    return render_to_response('index.html' , {'flag': False , 'number':number})


def getImage(request):
    img = request.FILES['image']
    filename = time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
    folder = "static/img/"
    with open(folder + filename , 'wb+') as des:
        des.write(img.read())

    image = Image.open(folder + filename)
    width , height = image.size
    ratio = round(width * 1.0 / height , 2)

    colorObj = ColorThief(folder + filename)
    dominantColor = '#%02x%02x%02x' % colorObj.get_color(quality = 1)
    palette = ['#%02x%02x%02x' % item for item in colorObj.get_palette(color_count = 5)]
    paletteStr = palette[0]
    for item in palette[1:]:
        paletteStr += ";" + item

    number = Banner.objects.count()
    return render_to_response('index.html' , {'flag': True , 'filename': filename , 'width': width , 'height': height , 'ratio':ratio , 'dominantColor':dominantColor , 'palette': paletteStr , 'number':number})



def getData(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        width = request.POST['width']
        height = request.POST['height']
        ratio = request.POST['ratio']
        category = request.POST['category']
        imgCount = request.POST['imgCount']
        imgElements = request.POST['imgElements']
        textCount = request.POST['textCount']
        textElements = request.POST['textElements']
        textAlignment = request.POST['textAlignment']
        dominantColor = request.POST['dominantColor']
        palette = request.POST['palette']
        backgroundColor = request.POST['backgroundColor']
        textColor = request.POST['textColor']
        backgroundCategory = request.POST['backgroundCategory']

        banner = Banner(name = filename , width = int(width) , height = int(height) , 
                        ratio = float(ratio) , category = int(category) , imgCount = int(imgCount) , 
                        imgElement = imgElements , textCount = int(textCount) , textElement = textElements , 
                        textAlignment = int(textAlignment) , dominantColor = dominantColor , palette = palette , 
                        backgroundColor = backgroundColor , textColor = textColor , backgroundCategory = int(backgroundCategory))

        banner.save()

        print "SUCCESS!"
    number = Banner.objects.count()

    return render_to_response('index.html' , {'flag': False , 'number':number})