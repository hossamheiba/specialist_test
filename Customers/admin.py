from django.contrib import admin
from .models import User, UserProfile

class UserProfileInline(admin.StackedInline):  # أو يمكن استخدام admin.TabularInline بدلاً من StackedInline
    model = UserProfile
    list_display = ('user', 'first_name', 'last_name', 'phone_number')
    list_display_links = ('user', 'first_name', 'last_name', 'phone_number')  
    search_fields = ('first_name', 'last_name', 'phone_number')  
    ordering = ('user',)  
    readonly_fields = ('user', 'first_name', 'last_name', 'phone_number', 'profile_image')
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('last_login', )
    list_display = ('first_name', 'last_name', 'phone_number',  'is_staff' ,'is_superuser' ,'is_active','last_login')
    list_display_links = ('first_name', 'last_name', 'phone_number')  
    search_fields = ('first_name', 'last_name', 'phone_number')
    exclude = ('first_name', 'last_name',   'password')
    

    inlines = [UserProfileInline] 
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.set_password(form.cleaned_data["password"])
        obj.save()

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number')
    list_display_links = ('user', 'first_name', 'last_name', 'phone_number')  
    search_fields = ('first_name', 'last_name', 'phone_number')  
    ordering = ('user',)  
    readonly_fields = ('user', 'first_name', 'last_name', 'phone_number', 'profile_image')

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
