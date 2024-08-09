from rest_framework import serializers
from .models import CSVFile

class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFile
        fields = ('file','uploaded_at')
        
class FileRenameHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFile
        fields = ('original_name',' new_name','timestamp','epoch')
