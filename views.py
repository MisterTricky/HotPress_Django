from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def simple_api_view(request):
    response = JsonResponse({
        'data': [
            'This is a Test Call to the API'
        ]

    })
    return response
