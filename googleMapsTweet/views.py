from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
import requests
import json

keywords=['gym, fitness, health, hospital, yoga, diet, running, workout, jogging',
          'rental, nyc, monument, london, travelling, ranking, backpack, hotel, motel',
          'Religion, Christianity, Hindu, Islam, Jewish, Judaism, Buddhism, Atheism, Pope, Temple',
          'Lunch, Breakfast, Dinner, Brunch, Pizza, restaurant, food, drink, eating',
          'Leisure, Beach, camping, fishing, parks, picnic, outing, entertainment, gaming, playing, movies, songs,\
           reading, novels',
          'Hillary, Trump, Democrat, Republican, Elections',
          'Hockey, Football, messi, ronaldo, fifa, league, chelsea, cricket, virat kohli, wrestling,\
           arsenal, barcelona',
          'engineering, medicine, science, doctor, drugs, cyber, web, space, tesla, spacex, robotics,\
           machine, learning, AI, Apple, Microsoft, IBM, Google',
          'World, Continent',
          'Hollywood, Bollywood, North Face, Puma, Adidas, Nike, shopping, brands, jewellery']


def Index(Request):
    return render(Request, 'googleMapsTweet/base.html')

def Post(Request):
    if Request.method == "POST":
        msg = Request.POST.get('Search', None)

        host = ''

        def search(url, term):
            #term = 'pmoindia'
            #print(url,term)
            uri = url + term
            response = requests.get(uri)
            results = json.loads(response.text)
            #print(results)
            return results

        if msg == 'Health':
            k = 0
        elif msg == 'Explore and Travel':
            k = 1
        elif msg == 'Religion':
            k = 2
        elif msg == 'Food and Drink':
            k = 3
        elif msg == 'Leisure':
            k = 4
        elif msg == 'Elections':
            k = 5
        elif msg == 'Sports':
            k = 6
        elif msg == 'Science':
            k = 7
        elif msg == 'World':
            k = 8
        elif msg == 'Brands and Following':
            k = 9

        r = search(host, keywords[k])

        data = [res['_source']['coordinates'] for res in r['hits']['hits']]
        #print(data)
        hits = len(data)
        #print(hits)
        length = {'hits': hits}
        coordinates = {}
        for i in range(hits):
            coordinates[i] = {'lat': data[i][1], 'lng': data[i][0]}
            #print (coordinates[i])

        data = {'coordinates': coordinates, 'length': length}

        return JsonResponse(data)