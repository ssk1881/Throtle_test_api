from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User, ActivityPeriod


class ResponseViewer(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    context = {}
    template = "throtle/home.html"
    return render(request, template, context)


def processing(request):
    if 'form_submit' in request.POST:
        user_id = request.POST.get("id_n", "")
        real_name = request.POST.get("real_name_n", "")
        time_zone = request.POST.get("time_zone_n", "")
        start_time = request.POST.get("start_time_n", "")
        end_time = request.POST.get("end_time_n", "")

        user_object = User(id=user_id, real_name=real_name, tz=time_zone)
        activity_object = ActivityPeriod(pid=user_object, start_time=start_time, end_time=end_time)
        user_object.save()
        activity_object.save()

    context = {}
    template = "throtle/home.html"
    return render(request, template, context)




