# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns
# from django.urls import path, include
# from django.contrib import admin
# from Home.views import home_section_view

# urlpatterns = [
#     path('i18n/', include('django.conf.urls.i18n')),  # مسار تغيير اللغة
# ]

# # استخدام i18n_patterns مع جعل اللغة الافتراضية بدون `/ar/` في الرابط
# urlpatterns += i18n_patterns(
#     path('admin/', admin.site.urls),
#     path('', home_section_view, name='home'),
#     # prefix_default_language=False  # منع ظهور اللغة الافتراضية في الرابط
# )

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin
# from django.utils.translation import gettext_lazy as _  

from Home.views import home_section_view , add_comment
from About_Us.views import about_view
from Our_Center.views import map_view
from Contact_Us.views import loc_view
from Jobs.views import submit_job_application
from Our_Offers.views import offer_section_view
from Media_Center.views import news_section_view
from FAQ.views import faq_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  
]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),  
    path('map/', include('map.urls')),  
    path('accounts/', include('Customers.urls')),  

    path('', home_section_view, name='Home'),  
    path('add-comment/', add_comment, name='add_comment'),
    path('About_Us/', about_view, name='About_Us'),
    path('jobs/', submit_job_application, name='jobs'), 
    path('Our_Center/', map_view, name='Our_Center'),  
    path('Contact_Us/', loc_view, name='Contact_Us'), 
    path('Our_Services/', include('Our_Services.urls')),  
    path('Our_Offers/', offer_section_view, name='Our_Offers'), 
    path('Media_Center/', news_section_view, name='Media_Center'), 
    path('FAQ/', faq_view, name='FAQ'), 
    path('Book_Service/', include('Book_Service.urls')),  
    
    
    
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
