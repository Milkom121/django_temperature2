from tempRecord.models import TempRecord
from rest_framework import serializers


class TempRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model=TempRecord
        fields = "__all__"
