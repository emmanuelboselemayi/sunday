from django.shortcuts import render, redirect
from django import template


def homepage(request):
    return render(request, "site/home.html", {})
