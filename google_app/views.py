from django.shortcuts import render
import requests
from django.http import JsonResponse

def text_search(request):
    api_key = "AIzaSyAw0aedhWlgleIkh8bpHUayjzJU3m7OS7w"
    query = request.GET.get("query", ' ')
    next_page_token = request.GET.get("next_page_token")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s"%(query, api_key)


    if next_page_token is not None:
        url+="&pagetoken=%s"%(next_page_token)
    response = requests.get(url)

    

    # return JsonResponse(response.json(), safe=False)
    return render(request, "text.html", {'response': response.json() })




def place_detail(request):
    api_key = "AIzaSyAw0aedhWlgleIkh8bpHUayjzJU3m7OS7w"
    key = "AIzaSyB5XuVdmhVEIlWzYauOx47opn7FXyMpAnI"
    reference = request.GET.get("reference", ' ')
    next_page_token = request.GET.get("next_page_token")
    url = "https://maps.googleapis.com/maps/api/place/details/json?reference=%s&key=%s"%(reference, api_key)
    response = requests.get(url)
    


    # return JsonResponse(response.json(), safe=False)
    return render(request, "detail.html", {'response': response.json(), 'key': key })




def nearby_search(request):
    api_key = "AIzaSyAw0aedhWlgleIkh8bpHUayjzJU3m7OS7w"
    location = request.GET.get('location')
    radius= request.GET.get('radius', ' ')
    # query = request.GET.get("query", ' ')
    # next_page_token = request.GET.get("next_page_token")
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&key=%s"%(location, radius, api_key)

    # if next_page_token is not None:
    #     url+="&pagetoken=%s"%(next_page_token)
    response = requests.get(url)
    # return JsonResponse(response.json(), safe=False)
    return render(request, "nearby.html", {'response': response.json() })



