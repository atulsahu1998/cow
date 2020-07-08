from django.shortcuts import render
from .models import OurTeam
# Create your views here.
def index(request):
    members = OurTeam.objects.all()

    return render(request, "index.html", {'members': members})
