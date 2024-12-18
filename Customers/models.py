from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, password=None):
        if not phone_number:
            raise ValueError('The Phone Number must be set')
        if not first_name:
            raise ValueError('The First Name must be set')
        if not last_name:
            raise ValueError('The Last Name must be set')

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, first_name, last_name, password): 
        user = self.create_user(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name' ,'last_name']

    objects = UserManager()


    def __str__(self):
        # إذا لم يتم تعبئة الاسم الأول والأخير، ارجع القيم الافتراضية
        default_first_name = "اسم افتراضي"
        default_last_name = "مستخدم"
        return f"{self.first_name if self.first_name else default_first_name} {self.last_name if self.last_name else default_last_name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, editable=False, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/default_profile.jpg')

    def __str__(self):
        profile_first_name = self.first_name if self.first_name else self.user.first_name or "اسم افتراضي"
        profile_last_name = self.last_name if self.last_name else self.user.last_name or "مستخدم"
        return f"Profile of {profile_first_name} {profile_last_name}"
    
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            first_name=instance.first_name or "اسم افتراضي",
            last_name=instance.last_name or "مستخدم",
            phone_number=instance.phone_number,
            profile_image=instance.profile_image
        )
    else:
        try:
            profile = instance.profile
            profile.first_name = instance.first_name or "اسم افتراضي"
            profile.last_name = instance.last_name or "مستخدم"
            profile.profile_image = instance.profile_image
            profile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(
                user=instance,
                first_name=instance.first_name or "اسم افتراضي",
                last_name=instance.last_name or "مستخدم",
                phone_number=instance.phone_number,
                profile_image=instance.profile_image
            )
