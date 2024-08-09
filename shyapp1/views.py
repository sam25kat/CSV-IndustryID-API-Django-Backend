import os
import time
from django.conf import settings
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CSVFile, FileRenameHistory,IndustryID
from .serializers import CSVFileSerializer
from django.http import JsonResponse
import uuid

class UploadCSVView(APIView):
    def post(self, request, format=None):
        # Get the secret key from headers
        secret_key = request.headers.get('X-Secret-Key')

        if not secret_key:
            return JsonResponse({'error': 'Secret key is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Check if the secret key matches any industryid
            industryid = IndustryID.objects.get(secret_key=secret_key)
        except industryid.DoesNotExist:
            return JsonResponse({'error': 'Invalid secret key'}, status=status.HTTP_403_FORBIDDEN)
        
        
        
        serializer = CSVFileSerializer(data=request.data)
        if serializer.is_valid():
           
            csv_file_instance = serializer.save()

            
            original_file_path = csv_file_instance.file.path
            original_file_name = os.path.basename(original_file_path)

           
            epoch_time = int(time.time()) 
            new_file_name = f'{epoch_time}.csv'

            
            current_directory = os.getcwd()
            new_file_path = os.path.join(current_directory, new_file_name)

           
            os.rename(original_file_path, new_file_path)

           
            FileRenameHistory.objects.create(
                original_name=original_file_name,
                new_name=new_file_name,
                timestamp=timezone.now(),
                epoch=epoch_time,
                new_file_path=new_file_path,
                industryid=industryid
            )

            return Response({'status': f'File uploaded and renamed to {new_file_name}'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class IndustryIDKeyView(APIView):
    
    def get(self, request, format=None):
        name = request.data.get('name')
        
        if not name:
            return JsonResponse({'error': 'IndustryID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            industryid = IndustryID.objects.get(name=name)
            return JsonResponse({'name': IndustryID.name, 'secret_key': IndustryID.secret_key}, status=status.HTTP_200_OK)
        except IndustryID.DoesNotExist:
            return JsonResponse({'error': 'IndustryID not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, format=None):
        name = request.data.get('name')
        
        if not name:
            return JsonResponse({'error': 'IndustryID name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        industryid, created = IndustryID.objects.get_or_create(name=name)
        
        
        
        if created:
            # Generate a new secret key if the IndustryID was newly created
            industryid.secret_key = str(uuid.uuid4())
            industryid.save()
            return JsonResponse({'name': industryid.name, 'secret_key': industryid.secret_key, 'message': 'New industryid created'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'name': industryid.name, 'secret_key':industryid.secret_key, 'message': 'industryid already exists'}, status=status.HTTP_200_OK)
