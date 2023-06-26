# Importing library
import cv2
from pyzbar.pyzbar import decode
import requests
import json
from django.shortcuts import render, redirect

# Make one method to decode the barcode

def checkbookprice(request):

    return render(request, 'checkbookprice/checkbookprice.html')

def BarcodeReader(image):
    # read the image in numpy array using cv2
    img = cv2.imread(image)

    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                # Print the barcode data
                ISBN = int(barcode.data)
                return ISBN

def aladin_api(ISBN):
    # 키와 url 정의
    key = "ttbhbh53530957001"
    url = f"http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={key}&itemIdType=ISBN&ItemId={ISBN}&output=js&Version=20131101&OptResult=c2binfo"

    # request 보내기
    response = requests.get(url)

    # 받은 response를 json 타입으로 바뀌주기
    response_json = json.loads(response.text)

    # 확인
    datas = response_json['item'][0]
    print(datas['title'])
    print(datas['link'])
    print(datas['isbn13'])
    print(datas['priceSales'])
    print(datas['priceStandard'])
    print(datas['cover'])
    print(datas['subInfo']['c2bsales_price']['AA'])
    print(datas['subInfo']['c2bsales_price']['A'])
    print(datas['subInfo']['c2bsales_price']['B'])
    print(datas['subInfo']['c2bsales_price']['C'])


