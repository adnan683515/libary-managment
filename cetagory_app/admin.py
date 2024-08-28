from django.contrib import admin
from cetagory_app.models import Cetagory
# Register your models here.
class cetagory_model(admin.ModelAdmin):
    prepopulated_fields = {'slug':('cetagory_name',)}
    list_display = ['cetagory_name','slug']
    
    
admin.site.register(Cetagory,cetagory_model)