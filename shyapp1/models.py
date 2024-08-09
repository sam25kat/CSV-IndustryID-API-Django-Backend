from django.db import models
import os,time
import uuid

class CSVFile(models.Model):
    file = models.FileField(upload_to='csvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
    def file_name(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.file_name()
    
    
    
    
class IndustryID(models.Model):
    name = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.name
    
class FileRenameHistory(models.Model):
    original_name = models.CharField(max_length=255)
    new_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    epoch = models.IntegerField(default=int(time.time()))
    new_file_path = models.CharField(max_length=255)
    industryid = models.ForeignKey(IndustryID, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.original_name} -> {self.new_name} at {self.timestamp}'
    
    

