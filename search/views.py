import requests
import json
from django.shortcuts import render
from django.views import View


# Create your views here.
class Search(View):
    def get(self, request):
        return render(request, 'search/search.html')

    def post(self, request):
        search = request.POST['search']
        res = requests.get('https://itunes.apple.com/search',
                           params={'term': search})
        print(res.url)
        ret = json.loads(res.text)
        return render(request,
                      'search/search.html',
                      context={'results': ret['results']})
