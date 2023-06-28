# Importing library
import cv2
from pyzbar.pyzbar import decode
import requests
import json
from django.shortcuts import render, redirect

from checkbookprice.form import PhotoForm
from checkbookprice.models import Photo


# Make one method to decode the barcode

def checkbookprice(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            barcode = form.save(commit=False)
            barcode.save()
            return redirect('price:settingbarcode')
    else:
        form = PhotoForm()
    context = {'form': form}
    return render(request, 'checkbookprice/checkbookprice.html',context)

def settingbarcode(request):
    image_list = Photo.objects.all()
    context = {'image_list': image_list}
    return render(request, 'checkbookprice/setting.html', context)

def BarcodeReader(request, image_id):

    photo = Photo.objects.all().get(id=image_id)
    # read the image in numpy array using cv2
    img = cv2.imread(f"media/{photo.image}")

    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If not detected then print the message
    if not detectedBarcodes:
        print("바코드 인식 실패.")
        photo.delete()
        return redirect('price:checkbookprice')
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
                isbn = int(barcode.data)
                # 키와 url 정의
                key = "ttbhbh53530957001"
                url = f"http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={key}&itemIdType=ISBN&ItemId={isbn}&output=js&Version=20131101&OptResult=c2binfo"
                # request 보내기
                response = requests.get(url)
                # 받은 response를 json 타입으로 바뀌주기
                response_json = json.loads(response.text)
                # 확인
                datas = response_json['item'][0]

                title = datas['title']
                link = datas['link']
                cover = datas['cover']
                isbn13 = datas['isbn13']
                priceSales = datas['priceSales']
                priceStandard = datas['priceStandard']
                '''
                priceSales = datas['priceSales']
                priceStandard = datas['priceStandard']
                '''
                photo.delete()
                return render(request, 'checkbookprice/apiprocess.html',
                              {'title': title, 'link': link, 'cover': cover, 'isbn13': isbn13,
                               'price':priceSales,'pricestandard':priceStandard})


def Reader(request):

    barcode = request.GET.get('barcode')
    print(barcode)
    # 키와 url 정의
    key = "ttbhbh53530957001"
    url = f"http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={key}&itemIdType=ISBN&ItemId={barcode}&output=js&Version=20131101&OptResult=c2binfo"
    # request 보내기
    response = requests.get(url)
    # 받은 response를 json 타입으로 바뀌주기
    response_json = json.loads(response.text)
    # 확인
    datas = response_json['item'][0]

    title = datas['title']
    link = datas['link']
    cover = datas['cover']
    isbn13 = datas['isbn13']
    priceSales = datas['priceSales']
    priceStandard = datas['priceStandard']

    return render(request, 'checkbookprice/apiprocess.html',
                  {'title': title, 'link': link, 'cover': cover, 'isbn13': isbn13,
                   'price':priceSales,'pricestandard':priceStandard})
'''
def aladin_api(request, isbn):
    # 키와 url 정의
    key = "ttbhbh53530957001"
    url = f"http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={key}&itemIdType=ISBN&ItemId={isbn}&output=js&Version=20131101&OptResult=c2binfo"
    # request 보내기
    response = requests.get(url)
    # 받은 response를 json 타입으로 바뀌주기
    response_json = json.loads(response.text)
    # 확인
    datas = response_json['item'][0]

    title = datas['title']
    link = datas['link']
    cover = datas['cover']
    isbn13 = datas['isbn13']
    priceSales = datas['priceSales']
    priceStandard = datas['priceStandard']

    return render(request, 'checkbookprice/apiprocess.html',
                  {'title':title,'link':link,'cover':cover,'isbn13':isbn13,
                   'price':priceSales,'pricestandard':priceStandard})
'''
'''
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
'''