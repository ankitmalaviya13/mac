from django.shortcuts import render
from .models import Product, Contact, Orders, orderUpdate
from django.http import HttpResponse
import math
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
# from paytm import Checksum
# Create your views here.
MERCHANT_KEY = 'kbzkb1DSbJiv_O3p5'

def index(request):
    allprods = []
    cateprods = Product.objects.values('category', 'id')
    cates = {item['category'] for item in cateprods}
    for cat in cates:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nofslides = n//4+ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nofslides), nofslides])
    params = {'allprods': allprods}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    thank = False;
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        desc = request.POST.get('desc', "")
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank= True;


    return render(request, "shop/contact.html",{'thank':thank})

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', "")
        email = request.POST.get('email', "")
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order = Orders.objects.filter(order_id=orderId,email=email)
            # return HttpResponse(order)
            if(len(order)>0):
                update = orderUpdate.objects.filter(order_id=orderId)
                
                updates = []
                for item in update:
                    updates.append({'text':item.updatedesc,'time':item.timestamp})
                
                # return HttpResponse(updates)
                response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")
    return render(request, "shop/tracker.html")

def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "shop/prodview.html", {'product': product[0]})
    # return HttpResponse("we are at productview")


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson',"")
        name = request.POST.get('name', "")
        amount = request.POST.get('amount', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')        
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip_code = request.POST.get('zip_code', "")
        phone = request.POST.get('phone', "")
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,state=state, Zip_code=zip_code, phone=phone,amount=amount)        
        order.save()
        update = orderUpdate(order_id=order.order_id,updatedesc = "The order is placed")
        update.save()
        thank = True
        id = order.order_id
        # request paytm 

        param_dict={
            'MID': 'WorldP64425807474247',
            'ORDER_ID': order.order_id,
            'TXN_AMOUNT': '1',
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlepayment/'
            }
        # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, "shop/paytm.html",{'param_dict':param_dict})

    return render(request,"shop/checkout.html")


def search(request):
    return render(request, "shop/search.html")
    # return HttpResponse("we are at search")

@csrf_exempt
def handlerequest(request):
    return HttpResponse('done')

    # return render(request, "shop/search.html")


# Python program to count
# occurrence of days in a month


# # function to find occurrences
# def occurrenceDays( n, firstday):

# 	# stores days in a week
# 	days = [ "Monday", "Tuesday", "Wednesday",
# 		"Thursday", "Friday", "Saturday",
# 		"Sunday" ]

    # Initialize all counts as 4.
    # count= [4 for i in range(0,7)]

    # # find index of the first day
    # pos=-1
    # for i in range(0,7):

    # print(i)
    # if (firstday == days[i]):
    # 	pos = i
    # 	break

    # # number of days whose occurrence will be 5
    # inc = n - 28

    # # mark the occurrence to be 5 of n-28 days
    # for i in range( pos, pos + inc):
    # 	if (i > 6):
    # 		count[i % 7] = 5
    # 	else:
    # 		count[i] = 5

    # # print the days
    # for i in range(0,7):
    # 	print (days[i] , " " , count[i])
