# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from models import SlowQueries, Queries
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def get_statistics(req):
    result = {'slow_requests': {}, 'queries': {}}

    #finding slow queries
    slow_queries = SlowQueries.objects.all()
    for query in slow_queries:
        result['slow_requests'][query.endPoint] = str(query.time)

    #finding queries count
    queries = Queries.objects.all()
    for query in queries:
        result['queries'][query.endPoint] = str(query.count)
    return HttpResponse(json.dumps(result), content_type='application/json')

def add_slow_queries(endPoint, time):
    try:
        q = SlowQueries.objects.get(endPoint=endPoint)
        if q.time < time:
            q.time = time
    except ObjectDoesNotExist, e:
        q = SlowQueries(endPoint=endPoint, time=time)
    q.save()

def add_query_count(endPoint):
    try:
        q = Queries.objects.get(endPoint=endPoint)
        q.count += 1
    except ObjectDoesNotExist, e:
        q = Queries(endPoint=endPoint, count=1)
    q.save()
