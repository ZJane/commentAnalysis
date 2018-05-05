#!/usr/bin/python 
# -*- coding:utf-8 -*-

from django.shortcuts import render

def show_index(request):
    return render(request,"index.html")
