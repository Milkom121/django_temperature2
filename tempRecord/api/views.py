from rest_framework import generics
from tempRecord.models import TempRecord
from tempRecord.api.serializers import TempRecordSerializer

class TempRecordCreateAPIView(generics.ListCreateAPIView):
    queryset = TempRecord.objects.all().order_by('id')
    serializer_class = TempRecordSerializer

class TempRecordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TempRecord.objects.all()
    serializer_class = TempRecordSerializer
