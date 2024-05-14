from django.contrib import admin
from .models import Something, Menu_Items, Logo_pic, Carousel_Items, Donors, News_Items, OnA_Items, Story_Items, Staff_Cast, Trailer, Music, Podcast, SNS, Goods, Category, Contact

class Menu_Items_Admin(admin.ModelAdmin):
    list_display = ("id","ItemName","Url")
admin.site.register(Menu_Items, Menu_Items_Admin)

class LogoAdmin(admin.ModelAdmin):
    list_display = ("id","Img", "Alt")
admin.site.register(Logo_pic, LogoAdmin)

class CarouselItemsAdmin(admin.ModelAdmin):
    list_display = ("Carousel_id", "Img", "description", "alt",)
admin.site.register(Carousel_Items,CarouselItemsAdmin)

class DonorAdmin(admin.ModelAdmin):
    list_display = ("id","FaviconDonors", "Url", "Alt")
admin.site.register(Donors, DonorAdmin)

class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("id","Title", "ImgThumb", "UpdateAt",)
admin.site.register(News_Items, NewsItemAdmin)

class OnAirItemAdmin(admin.ModelAdmin):
    list_display = ("Title", "Date", "Detail",)
admin.site.register(OnA_Items,OnAirItemAdmin)

class StoryItemAdmin(admin.ModelAdmin):
    list_display = ("Title", "ImgThumb", "SubTitle",)
admin.site.register(Story_Items,StoryItemAdmin)

class StaffCastAdmin(admin.ModelAdmin):
    list_display = ("id", "Img", "Name", "Url", "Movie", "job",)
admin.site.register(Staff_Cast,StaffCastAdmin)

class TrailerAdmin(admin.ModelAdmin):
    list_display = ("id","Img", "Name", "Url",)
admin.site.register(Trailer,TrailerAdmin)

class MusicAdmin(admin.ModelAdmin):
    list_display = ("id", "Img", "Name", "Type",)
admin.site.register(Music, MusicAdmin)

class PodcastAdmin(admin.ModelAdmin):
    list_display = ("Name", "Img", "Url",)
admin.site.register(Podcast,PodcastAdmin)

class SNSAdmin(admin.ModelAdmin):
    list_display = ("Name", "Img", "Url",)
admin.site.register(SNS,SNSAdmin)

class GoodsAdmin(admin.ModelAdmin):
    list_display = ("id","Name", "Img", "SellDate" , "Price", "Category", "Url",)
admin.site.register(Goods, GoodsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "Description")
admin.site.register(Category,CategoryAdmin)

@admin.register(Contact)#a diffrent way to regist admin site
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "zip_code", "phone", "web", "email_address")


class SomethingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(Something, SomethingAdmin)


