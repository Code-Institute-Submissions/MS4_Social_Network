from django.shortcuts import render
from django.views import View

# Landing page 
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')
