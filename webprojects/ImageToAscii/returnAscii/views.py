from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from PIL import Image, ImageChops, UnidentifiedImageError
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import os
import mimetypes
import json
#code by https://github.com/BSmith156/Image-to-ASCII/commits?author=BSmith156
#
def toascii(imagee,maxi=600, invert=False):
    gradient = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    inputPath = imagee
    # Optional arguments
    maxSet = False
    maxSize = maxi
    i = 3

    # Open input file
    try:
        image = Image.open(inputPath)
    except:
        quit()
    # Open output file

    # Resize
    if(maxSize > 0):
        image.thumbnail((maxSize / 2, maxSize / 2))

    # Convert to greyscale and invert if needed
    image = image.convert("L")
    if invert:
        image = ImageChops.invert(image)

    # Generate output
    output = ""
    width, height = image.size
    for y in range(height):
        for x in range(width):
            colour = image.getpixel((x, y))
            output += gradient[round((colour / 255) * (len(gradient) - 1))] + " "
        output += "\n"
    return output

@csrf_exempt
def index(request):
    # importing modules
      # Decode using the utf-8 encoding
    rq=request.body.decode('utf-8').replace("'",'"')
    my_json=json.loads(rq)
    print(my_json["Link"])
    link=my_json["Link"]
    width=my_json["Width"]
    print(link,width)
    urllib.request.urlretrieve(link,"gfg.png")
    x= toascii('C:\\Users\\T&M\\Desktop\\ImageToAscii\\gfg.png', int(width),True)
    return HttpResponse(x)


