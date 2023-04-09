
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from Routes.models import *
from .models import *
from rest_framework.views import APIView
from .serializers import *
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.


class TicketView(APIView):
    def post(self, request):
        if request.user.is_authenticated == False:
            return Response({"error": "Unathorized"})

        route_id = request.data["route_id"]
        route = get_object_or_404(Route, pk=route_id)
        seats = int(request.data["seats"])

        obj = Ticket.objects.create(
            starting_point = route.starting_point.name,
            ending_point = route.ending_point.name,
            fair = route.fair * seats,
            booked_by = request.user.username,
            counterman_metadata = {
                "phone_no" : request.user.phone_no
            },
        )

        ser = TicketSerializer(obj)
        
        return Response({
            'ticket' : ser.data
        })

@api_view()
def sells_view(request):
    if request.user.is_authenticated == False:
        return Response({"error": "Unathorized"})

    date = request.GET.get("date", "")

    ticket_objs = ShortRouteTicket.objects.filter(booked_by=request.user.username, date=date)
    return Response({
        'tickets' : TicketSerializer(ticket_objs, many=True).data
    })
    
