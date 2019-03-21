from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import serializers
import requests
from bs4 import BeautifulSoup


@csrf_exempt
@api_view(['POST'])
def get_followers(request):
    if request.method == 'POST':
        link = 'https://twitter.com/'
        serializer = serializers.Followers(request.data)
        username = serializer.data['username']
        link += username
        html = requests.get(link).text
        soup = BeautifulSoup(html,'html.parser')
        alist = soup.find_all('a','ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor')
        for tag in alist:
            if tag['data-nav'] == 'followers':
                return JsonResponse({'title': tag['title']})
        return JsonResponse({'error':True})
@csrf_exempt
def follower_page(request):
    return render(request,template_name = 'followers/index.html')
