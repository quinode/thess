# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

def home(request):
    rdict = {'scheme_id':1}   
    return render_to_response('home.html',rdict,RequestContext(request))
    