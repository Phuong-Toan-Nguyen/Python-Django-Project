from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Something, Menu_Items, Logo_pic, Carousel_Items, Donors, News_Items, OnA_Items, Story_Items, Staff_Cast, Trailer, Music, Podcast, SNS, Goods, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

from .forms import ContactForm
from django.core.mail import send_mail

def main(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.first()
    carousels = Carousel_Items.objects.all() #truy van .url phai de object
    donors = Donors.objects.all()
    newsItems = News_Items.objects.all().order_by('-id')
    OnAirItems = OnA_Items.objects.all().order_by('-id')
    StoryItems = Story_Items.objects.all().order_by('-id')
    StaffCast = Staff_Cast.objects.all().order_by('-id')
    trailer = Trailer.objects.all().order_by('-id')
    music = Music.objects.all().order_by('-id')
    podcast = Podcast.objects.all().order_by('-id')
    sns = SNS.objects.all().order_by('-id')
    goods = Goods.objects.all().order_by('-id')
    
    template = loader.get_template('mainpage.html')
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'carousels': carousels,
        'donors': donors,
        'newsItems' : newsItems,
        'OnAirItems': OnAirItems,
        'StoryItems': StoryItems,
        'StaffCast': StaffCast,
        'trailers': trailer,
        'musics': music,
        'podcasts': podcast,
        'sns': sns,
        'goods': goods,
    }
    return HttpResponse(template.render(context, request))

def NewsDetail(request, id):
    newsItems = News_Items.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('NewsDetail.html')
    context = {
        'newsItems': newsItems,
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
    }
    return HttpResponse(template.render(context, request))
    
def MoreNews(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    newsItems = News_Items.objects.all().order_by('-id')
    #paginator
    paginator = Paginator(newsItems, 4)
    page = request.GET.get('page', 1)
    newsPaging = paginator.get_page(page)
    #newsPaging = paginator.page(page)
    try: 
        elidedPageRange = paginator.get_elided_page_range(page,on_each_side=1,on_ends=2)
    except PageNotAnInteger:
        elidedPageRange = paginator.get_elided_page_range(1,on_each_side=2,on_ends=2)
    except EmptyPage:
        elidedPageRange = paginator.get_elided_page_range(paginator.num_pages,on_each_side=1,on_ends=2)
    except InvalidPage:
        elidedPageRange = paginator.get_elided_page_range(1,on_each_side=2,on_ends=2)

    template = loader.get_template('News.html')
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
        'newsItems': newsItems,
        'newsPaging':newsPaging,
        'elidedPageRange':elidedPageRange,
    }
    return HttpResponse(template.render(context, request))

def StoryDetail(request, id):
    storyItems = Story_Items.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('StoryDetail.html')
    context = {
        'storys': storyItems,
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
    }
    return HttpResponse(template.render(context, request))

def MoreStorys(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    storyItems = Story_Items.objects.all().order_by('-id')
    #paginator
    paginator = Paginator(storyItems, 6)
    page = request.GET.get('page', 1)
    storyPaging = paginator.get_page(page)
    
    try: 
        elidedPageRange = paginator.get_elided_page_range(page,on_each_side=2,on_ends=2)
    except PageNotAnInteger:
        elidedPageRange = paginator.get_elided_page_range(1,on_each_side=2,on_ends=2)
    except EmptyPage:
        elidedPageRange = paginator.get_elided_page_range(paginator.num_pages,on_each_side=2,on_ends=2)
    except InvalidPage:
        elidedPageRange = paginator.get_elided_page_range(1,on_each_side=2,on_ends=2)
    
    template = loader.get_template('Storys.html')
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
        'StoryItems': storyItems,
        'storyPaging':storyPaging,
        'elidedPageRange':elidedPageRange,
    }
    return HttpResponse(template.render(context, request))

def StaffCast(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    StaffCast = Staff_Cast.objects.all().order_by('-id')
    #paginator
    paginator = Paginator(StaffCast, 2)
    page = request.GET.get('page', 1)
    StaffCastPaging = paginator.get_page(page)
    try: 
        elidedPageRange = paginator.get_elided_page_range(number = page,on_each_side=2,on_ends=2)
    except InvalidPage:
        elidedPageRange = paginator.get_elided_page_range(number = 1,on_each_side=2,on_ends=2)
    
    template = loader.get_template('Staff&Cast.html')
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
        'staffcast': StaffCast,
        'StaffCastPaging':StaffCastPaging,
        'elidedPageRange':elidedPageRange,
    }
    return HttpResponse(template.render(context, request))

def TrailerDetail(request, id):
    trailer = Trailer.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('TrailerDetail.html')
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
        'trailers': trailer,
    }
    return HttpResponse(template.render(context, request))

def MoreTrailers(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    trailer = Trailer.objects.all().order_by('-id')
    #paginator
    paginator = Paginator(trailer, 6)
    page = request.GET.get('page', 1)
    trailerPaging = paginator.get_page(page)
    try: 
        elidedPageRange = paginator.get_elided_page_range(number = page,on_each_side=2,on_ends=2)
    except InvalidPage:
        elidedPageRange = paginator.get_elided_page_range(number = 1,on_each_side=2,on_ends=2)
    
    template = loader.get_template('Trailers.html')
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
        'trailers': trailer,
        'trailerPaging':trailerPaging,
        'elidedPageRange':elidedPageRange,
    }
    return HttpResponse(template.render(context, request))

def MusicDetail(request, id):
    music = Music.objects.get(id=id)
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    template = loader.get_template('MusicDetail.html')
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
        'musics': music,
    }
    return HttpResponse(template.render(context, request))

def GoodsDetail(request, id):
    goods = Goods.objects.get(id=id)
    template = loader.get_template('GoodsDetail.html')
    context = {
        'goods': goods
    }
    return HttpResponse(template.render(context, request))

def MoreGoods(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    goods = Goods.objects.all().order_by('-id')
    category = Category.objects.all()
    template = loader.get_template('Goods.html')
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
        'goods': goods,
        'category':category,
    }
    return HttpResponse(template.render(context, request))

def add_contact(request):
    menuitems = Menu_Items.objects.all().values()
    favicon = Logo_pic.objects.get(id=1)
    donors = Donors.objects.all()
    form = ContactForm
    
    submitted = False #bien dung cho redirect 
    if request.method == "POST": 
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            
            username = form.cleaned_data['name']#nen xai cai nay
            user_email = form.cleaned_data['email_address']
            
            #send an email
            send_mail(
                'message from ' + username, #subject the email
                'this is a notification email to you!', # message the email
                '' , # from email
                [user_email], # to email
            )
            
            form = ContactForm()
            context = {
                'username':username,
                'MenuItems': menuitems,
                'Favicon': favicon,
                'donors': donors,
                'form': form,
                'submitted':submitted,
                
                
            }
            
            return render(request, 'Form/upload.html', context)
            #return HttpResponseRedirect('/contact?submitted=True') #cach cu, khong dua du lieu ten hay email nguoi dung len man hinh dc
    else:
        form = ContactForm
        if 'submitted' in request.GET:#bien dung cho ham redirect nham xuat dong thong bao luu data thanh cong
            submitted = True
            
    template = loader.get_template('Form/upload.html')
    
    context = {
        'MenuItems': menuitems,
        'Favicon': favicon,
        'donors': donors,
        'form': form,
        'submitted':submitted,
    }
    return HttpResponse(template.render(context, request))








def testing(request):
    mydata = Something.objects.all().values()
    template = loader.get_template('testing.html')
    context = {
        'mydatadata': mydata
    }
    return HttpResponse(template.render(context, request))
