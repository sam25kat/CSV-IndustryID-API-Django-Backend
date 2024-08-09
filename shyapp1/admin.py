from django.contrib import admin
from .models import CSVFile, FileRenameHistory, IndustryID

class CSVFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded_at')

class FileRenameHistoryAdmin(admin.ModelAdmin):
    list_display = ('original_name', 'new_name', 'timestamp','epoch','new_file_path','industryid')
    
class IndustryIDAdmin(admin.ModelAdmin):
    list_display = ('name', 'secret_key')

admin.site.register(CSVFile, CSVFileAdmin)
admin.site.register(FileRenameHistory, FileRenameHistoryAdmin)
admin.site.register(IndustryID, IndustryIDAdmin)