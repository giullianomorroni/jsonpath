#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from parser.query_parser import QueryParser
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext

def _404(request):
    return render_to_response('404.html');

def _500(request):
    return render_to_response('500.html');

@requires_csrf_token
def query(request):
    data = request.POST['data']
    query = request.POST['query']
    parser = QueryParser()
    tmp = parser.parse(query, data)
    data = indent(data)

    result = []
    for t in tmp:
        if isinstance(t, dict):
            for key in t:
                result.append( str(key) + ':' + str(t[key]) )
        elif isinstance(t, list):
            for t2 in t:
                if isinstance(t2, dict):
                    for key in t2:
                        result.append( str(key) + ':' + str(t2[key]) )
                else:
                    result.append( str(t2) )
        else:
            result.append( str(t) )

    return render_to_response('index.html', {'result':result, 'data':data, 'query':query}, context_instance=RequestContext(request));

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request));

def how_to_en(request):
    return render_to_response('how-to_en_US.html');

def how_to_pt(request):
    return render_to_response('how-to_pt_BR.html');


def indent(data):
    return data
    #import json
    #return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))