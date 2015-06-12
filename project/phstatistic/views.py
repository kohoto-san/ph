from django.shortcuts import render
from django.http import HttpResponse

import requests
import json
import collections

import datetime

from phstatistic.models import Product

from django.shortcuts import get_object_or_404


def create(request):

    if request.method == 'GET':
        day = request.GET['day']

    if day:

        # Получение токена приложения
        headers = auth()

        # ?days_ago=2
        url = 'https://api.producthunt.com/v1/posts'

        # year, month, day
        # first day: 2013-11-24
        start_date = datetime.date(2013, 11, 24)

        # start_date = datetime.date(2015, 6, 9)

        #current_date = date(int(day[:4]), int(day[4:6]), int(day[6:]))
        current_date = datetime.date.today()

        days = current_date - start_date
        y = 0

        while y <= days.days:

            param_day = current_date - datetime.timedelta(y)

            # date_param = day[:4] + '-' + day[4:6] + '-' + day[6:]

            r = requests.get(url, headers=headers, params={'day': param_day})

            text = json.loads(r.text)

            length = len(text["posts"])

            i = 0

            if(length > 5):
                length = 5

            meta_days = (param_day - start_date).days

            while i < length:

                votes_count = text['posts'][i]['votes_count']
                name = text['posts'][i]['name']
                tagline = text['posts'][i]['tagline']

                discussion_url = text['posts'][i]['discussion_url']
                redirect_url = text['posts'][i]['redirect_url']

                created_at = text['posts'][i]['created_at']

                comments_count = text['posts'][i]['comments_count']

                i += 1

                p = Product.objects.create(name=name,
                                           day=meta_days,
                                           tagline=tagline,
                                           created_at=created_at,
                                           votes_count=votes_count,
                                           redirect_url=redirect_url,
                                           discussion_url=discussion_url,
                                           comments_count=comments_count,
                                           )

            # return HttpResponse(days.days)

            y += 1

        return HttpResponse(y)


# Аутенфикация приложения
def auth():

    client_id = '5b6ff8718c4743411d4939e2a8f8b53134913b9bdd141b0d557997c80dcaa736'
    client_secret = '64e4d76d5d552bce52b3d469225f5259410bd761336f300a62ab6ee7614664d8'
    grant_type = 'client_credentials'

    payload = {'client_id': client_id, 'client_secret': client_secret,
               'grant_type': grant_type}

    url = 'https://api.producthunt.com/v1/oauth/token'

    r = requests.post(url, params=payload)

    access_token = json.loads(r.text)
    access_token = access_token['access_token']

    headers = {'Authorization': 'Bearer ' + access_token}
    return headers


def timehunt(request):
    return render(request, 'timehunt.html')


def index(request):
    return render(request, 'index.html')


def detail(request):

    if request.method == 'GET':
        day = request.GET['day']

    products = Product.objects.filter(day=day)

    product_list = []

    for product in products:
        d = collections.OrderedDict()

        d["votes_count"] = product.votes_count
        d["name"] = product.name
        d["tagline"] = product.tagline

        d["discussion_url"] = product.discussion_url
        d["redirect_url"] = product.redirect_url

        d["created_at"] = product.created_at

        d["comments_count"] = product.comments_count

        product_list.append(d)

    j = json.dumps(product_list)

    return HttpResponse(j)

"""
    d = {"posts" : [
            {
                "votes_count": product.votes_count,
                "name": product.name,
                "tagline": product.tagline,

                "discussion_url": product.discussion_url,
                "redirect_url": product.redirect_url,

                "created_at": product.created_at,
            },
            {
                "votes_count": product.votes_count,
                "name": product.name,
                "tagline": product.tagline,

                "discussion_url": product.discussion_url,
                "redirect_url": product.redirect_url,

                "created_at": product.created_at,
            }
        ]}
"""

        # "children":[{'name':key,"size":value} for key,value in sample.items()]
