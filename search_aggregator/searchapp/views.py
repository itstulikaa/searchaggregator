from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json
import random
from django.shortcuts import render
import traceback
from django.http import HttpResponse
from .models import Product


searchkey = ['Microsoft TV', 'Apple TV']

url_list = ["http://api.shopclues.com/api/v11/search?q="+searchkey[1]+"&z=1&key=d12121c70dda5edfgd1df6633fdb36c0&page=2",
"https://search.paytm.com/v2/search?userQuery="+searchkey[1]+"&page_count=5&items_per_page=100"]

# Hitting random url from the list---
url = random.choice(url_list)
response = requests.request("GET", url).json()

# Search fuction to find data in the API---
def searchaggview(request):
    try:
        noofresults =response['grid_layout']
        length = len(response['grid_layout'])
    except:
        noofresults =response['products']
        length = len(response['products'])
    print(length)
    product=[]
    prod_list=[]
    for i in range(0,length):
        try:
            product_id=noofresults[i]['product_id']
        except:
            product_id='NA'
        
        try:
            name=noofresults[i]['name']
        except:
            name=noofresults[i]['product']

        try:
            url=noofresults[i]['url']
        except:
            url=noofresults[i]['product_url']

        try:
            image_url=noofresults[i]['image_url']
        except:
            image_url='NA'

        try:
            offer_price=noofresults[i]['offer_price']
        except:
            offer_price=noofresults[i]['list_price']

        try:
            actual_price=noofresults[i]['actual_price']
        except:
            actual_price=noofresults[i]['retail_price']

        product=[product_id,name,url,image_url,offer_price,actual_price]
        prod_list.append(product)


        # Saving the fetched data into the database---
        product_db = Product()
        product_db.product_id = product_id
        product_db.name = name
        product_db.url = url
        product_db.image_url = image_url
        product_db.offer_price = offer_price
        product_db.actual_price = actual_price
        product_db.save()


    # Paginator to show 50 data per page---
    paginator = Paginator(prod_list, 50)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    print(page_obj)

    return render(request, 'searchapp.html',{"prod_list" : page_obj})


