from django.contrib import admin
from home.models import Contact, Home, Base_Details, Home_Slide_Images

# Register your models here.

# admin.site.register((Contact, Home))

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message', 'date_time']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'subscribe', ]


@admin.register(Base_Details)
class BaseDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'photo']


@admin.register(Home_Slide_Images)
class HomeSlideImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'images']