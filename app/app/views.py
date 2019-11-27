from django.shortcuts import render
import requests as axios
import json

def index(request):
    return render(request, 'index.html', {})

def create_hospital(request):
    return render(request, 'CreateHospital.html', {})

def hospital_detail(request, id):
    data = axios.get('http://localhost:8000/location/' + str(id))
    if ("Not found" in data.text):
        return render(request, '404.html')
    context = json.loads(data.text) 
    return render(request, 'Hospital.html', context)

def edit_hospital(request, id):
    data = axios.get('http://localhost:8000/location/' + str(id))
    if ("Not found" in data.text):
        return render(request, '404.html')
    context = json.loads(data.text)
    return render(request, 'EditHospital.html', context)

def login(request):
    return render(request, 'login.html')