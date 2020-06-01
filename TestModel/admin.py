from django.contrib import admin
from TestModel.models import C21Students,GroupInformation,PrivateInformation

# Register your models here.
admin.site.register([C21Students,GroupInformation,PrivateInformation])