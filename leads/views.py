import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from leads.models import Lead, Brokerage
from leads.producer import publish
from leads.serializers import LeadSerializer


class LeadViewSet(viewsets.ViewSet):
    def list(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LeadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('lead_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        lead = Lead.objects.get(id=pk)
        serializer = LeadSerializer(lead)
        return Response(serializer.data)

    def update(self, request, pk=None):
        lead = Lead.objects.get(id=pk)
        serializer = LeadSerializer(instance=lead, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('lead_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        lead = Lead.objects.get(id=pk)
        lead.delete()
        publish('lead_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrokerageAPIView(APIView):
    def get(self, _):
        brokerages = Brokerage.objects.all()
        brokerage = random.choice(brokerages)
        return Response({
            'id': brokerage.id
        },
            status=status.HTTP_200_OK
        )
