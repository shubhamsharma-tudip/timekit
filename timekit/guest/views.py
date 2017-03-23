import json
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from .models import user, calender


def index(request):
    print"i am in indexs"
    return render(request,"guest/welcome.html")

def auth(request):
    return render(request,"guest/auth.html")




def calender1(request):
    return render(request, "guest/calender.html")


def userauth(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        print "email is", email
        print "password is ", password
        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        auth = ('virat17@tudip.nl', '123456')

        data = json.dumps({'email': email,
                             'password': password})

        print '******', data
        login_response = requests.post('https://api.timekit.io/v2/auth', headers=headers, data=data)
        decoded = login_response.json()


        print"total response", login_response
        print"total rxxxxxxxxxxxxxxxxxxxxxxxxxxxxesponse", decoded
        return render(request,'guest/calender.html',{'email':email})

        # return render(request,"guest/calender.html")
    else:
        print "in else"
        return HttpResponse('hello')


def usercalender(request):
    if request.method == "POST":
        calender1 = request.POST["calender"]
        description = request.POST["description"]
        user_email = request.POST["email"]
        token = user.objects.get(email=user_email).api_token


        user_name = user.objects.get(email=user_email)
        print '*******',user_email
        print "xxxxxxx",user_name
        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        auth = (user_email, token)

        data = json.dumps({'name': calender1,
                           'description': description})

        login_response = requests.post('https://api.timekit.io/v2/calendars', headers=headers, auth=auth, data=data)
        decoded = login_response.json()
        print"xxxxxxxxxxx", decoded


        create_calender = calender.objects.create(cal_id=decoded['data']['id'],
                                                   name=decoded['data']['name'],
                                                   description=decoded['data']['description'],
                                                   user=user_name

                                                  )


        create_calender.save()
        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        data = json.dumps({"type": "client-token",
                             "scopes": "widget",
                             "description":"dsgfhfhg",
                             "referrer": "http://chhegg.com"})
        login_response1 = requests.post('https://api.timekit.io/v2/credentials', headers=headers, auth=auth, data=data)
        print"xxxxxxxxxxx",login_response1
        decoded1 = login_response1.json()

        print"total response", login_response1
        print"total response", decoded1


        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        data = json.dumps({"emails": [
             "paresh@tudip.nl",
             "chintu@tudip.nl"

           ],
           "filters": {
             "or": [
               { "specific_day_and_time": {"day": "wednesday", "start": 21, "end": 23, "timezone": "America/Los_Angeles"}},
               { "specific_day_and_time": {"day": "Friday", "start": 13, "end": 16, "timezone": "America/Los_Angeles"}}
             ],
             "and": [
               { "daytime": {"timezone": "Europe/Copenhagen"}}
             ]
           },
           "future": "1 weeks",
           "length": "2 hour"})
        login_response1 = requests.post('https://api.timekit.io/v2/findtime', headers=headers, auth=auth, data=data)
        print"xxxxxxxzffffffffffffffffffffffffffffffffffxxxx", login_response1
        decoded1 = login_response1.json()

        print"total response", login_response1
        print"total response", decoded1


        # return HttpResponse('done successfully')
        return render(request, 'guest/findmy.html')



        # return render(request,"guest/calender.html")
    else:
        print "in else"
        return HttpResponse('hello')






def usersubmit(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        user_timezone = request.POST["timezone"]
        user_first = request.POST["first_name"]
        user_last_name=request.POST["last_name"]
        user_password=request.POST["password"]

        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        data = json.dumps({'email': user_email, 'timezone': 'America/Los_Angeles',
                           'first_name': user_first,
                           'last_name': user_last_name,
                            'password': user_password})

        login_response = requests.post('https://api.timekit.io/v2/users', headers=headers, data=data)
        decoded = login_response.json()
        create_user = user.objects.create(first_name=decoded['data']['first_name'],
                                    email=decoded['data']['email'],
                                    last_name=decoded['data']['last_name'],
                                    created_at=decoded['data']['created_at'],
                                    updated_at=decoded['data']['updated_at'],
                                    timezone=decoded['data']['timezone'],
                                    api_token=decoded['data']['api_token']
                                    )
        create_user.save()
        return render(request, 'guest/welcome.html')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def findtime(request):
#     headers = {'Timekit-App': 'python2', 'content-type': 'application/json', 'Accept': 'text/plain'}
#     data = json.dumps({
#            "emails": [
#                "ram1@tudip.nl"
#
#            ],
#            "filters": {
#              "or": [
#                { "specific_day_and_time": {"day": "Tuesday", "start": 15, "end": 18, "timezone": "America/Los_Angeles"}},
#                { "specific_day_and_time": {"day": "Friday", "start": 13, "end": 17, "timezone": "America/Los_Angeles"}}
#              ],
#              "and": [
#                { "daytime": {"timezone": "America/Los_Angeles"}}
#              ]
#            },
#            "future": "4 weeks",
#            "length": "3 hour"
#           })
#
#     auth = ('ram1@tudip.nl', 'H70uJ2GAqia2yLBkrqvFbwtKPpRcZRix')
#
#     login_response = requests.post('https://api.timekit.io/v2/findtime', auth=auth ,headers=headers, data=data)
#     decoded = login_response.json()
#     print"WWWWsfffffffffffffffffffffffffWWWW", decoded
#     return render(request, 'guest/findmy.html')

# def bookingtime(request):
#     headers = {'Timekit-App': 'python2', 'content-type': 'application/json', 'Accept': 'text/plain'}
#
#
#     data = json.dumps({
#
#         "graph": "confirm_decline",
#         "action": "create",
#         "event": {
#             "start": "2017-03-22T08:00:00+00:00",
#             "end": "2017-03-27T13:00:00+00:00",
#             "what": "Mens haircut",
#             "where": "Sesame St, Middleburg, FL 32068, USA",
#             "calendar_id": "8aefb5a9-cbff-4c17-9f33-f5f7105d4d1a",
#             "description": "Please arrive 10 minutes before you time begin"
#         },
#         "customer": {
#             "name": "pranay khilari",
#             "email": "pranay1@tudip.nl",
#             "phone": "1-591-001-5403",
#             "voip": "McFly",
#             "timezone": "America/Los_Angeles"
#         }
#     })
#
#     auth = ('ram1@tudip.nl', 'H70uJ2GAqia2yLBkrqvFbwtKPpRcZRix')
#
#     login_response = requests.post('https://api.timekit.io/v2/bookings', auth=auth, headers=headers, data=data)
#     decoded = login_response.json()
#     print"WWWWWWWW", decoded
#     return render(request, 'guest/findmy.html')
def user_login(request):
    email = request.POST['email']
    password = request.POST["password"]
    print '**********',email

    headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
    data = json.dumps({'email': email,
                       'password': password})
    login_response = requests.post('https://api.timekit.io/v2/auth', headers=headers, data=data)

    if login_response.status_code == 200:
        return render(request, 'guest/calender.html', {'email': email})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def signup(request):
    return render(request, 'guest/index.html')