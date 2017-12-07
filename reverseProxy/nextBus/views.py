from django.http import HttpResponse
import requests
import json
import pylru
from time import time
from django.conf import settings
from statistics.views import add_slow_queries, add_query_count

URL = 'http://webservices.nextbus.com/service/publicXMLFeed?command='

def apiCall(url, api_name):
    start_time = time()
    try:
        r = requests.get(url, verify=False, timeout=settings.TIMEOUT)
        print r.status_code
        end_time = time()
        update(api_name, start_time, end_time)
        if r.ok:
            #updating the cache entry before sending response
            settings.CACHE[api_name] = r.text
            return HttpResponse(content=r.text, content_type='text/xml', status=r.status_code)

    except requests.ConnectTimeout, e:
        if api_name in settings.CACHE.keys():
            return HttpResponse(content=settings.CACHE[api_name], content_type='text/xml')
        return HttpResponse('Timeout', status=504)
    except requests.ReadTimeout, e:
        if api_name in settings.CACHE.keys():
            return HttpResponse(content=settings.CACHE[api_name], content_type='text/xml')
        return HttpResponse('Timeout', status=504)

def agencyList(req):
    url = URL + 'agencyList'
    params = req.get_full_path().split('?')
    if len(params) > 1:
        url += ('&'+params[1])
    return apiCall(url, '/agencyList')


def routeList(req):
    url = URL + 'routeList'
    agency = req.GET.get('a', None)
    if agency:
        params = req.get_full_path().split('?')[1]
        url += ('&' + params)
        return apiCall(url, '/routeList')
    else:
        response = 'agency parameter "a" must be specified in query string'
        return HttpResponse(response, content_type='text/html', status=400)

def routeConfig(req):
    url = URL + 'routeConfig'
    agency = req.GET.get('a', None)
    route = req.GET.get('r', None)

    if agency and route:
        params = req.get_full_path().split('?')[1]
        url += ('&' + params)
        return  apiCall(url, '/routeConfig')
    else:
        if agency:
            response = 'route parameter "r" must be specified in query string'
        else:
            response = 'agency parameter "a" must be specified in query string'
        return HttpResponse(response, content_type='text/html', status=400)

def prediction(req):
    url = URL + 'predictions'
    agency = req.GET.get('a', None)
    route = req.GET.get('r', None)
    stop = req.GET.get('s', None)
    response = None

    if not agency:
        response = 'agency parameter "a" must be specified in query string'

    if not route:
        response = 'route parameter "r" must be specified in query string'

    if not stop:
        response = 'stop parameter "s" must be specified in query string'

    if response:
        return HttpResponse(response, content_type='text/html', status=400)
    else:
        params = req.get_full_path().split('?')[1]
        url += ('&'+params)
        return apiCall(url, '/predictions')


def update(api, start_time, end_time):
    #calculating the time elapsed
    time_elapsed = end_time - start_time
    if time_elapsed >= settings.THRESHOLD:
        add_slow_queries(api, time_elapsed)

    #Calculation for number of queries
    add_query_count(api)
