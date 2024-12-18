from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileUpdateForm

def send_otp(phone_number):
    otp = 1234 
    print(f"OTP sent to {phone_number}: {otp}")
    return otp

def register_view(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")

        if not phone_number:
            return render(request, 'register.html', {'message': 'Phone number is required', 'message_type': 'error'})

        user_model = get_user_model()
        if user_model.objects.filter(phone_number=phone_number).exists():
            return render(request, 'register.html', {'message': 'This phone number is already registered', 'message_type': 'error'})

        otp = send_otp(phone_number)
        request.session['otp'] = otp
        request.session['phone_number'] = phone_number
        request.session['is_registration'] = True

        next_url = request.GET.get('next', '/')
        request.session['next_url'] = next_url

        return redirect('verify_otp')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")

        if not phone_number:
            return render(request, 'login.html', {'message': 'Phone number is required', 'message_type': 'error'})

        user_model = get_user_model()
        if not user_model.objects.filter(phone_number=phone_number).exists():
            return render(request, 'login.html', {'message': 'User with this phone number does not exist', 'message_type': 'error'})

        otp = send_otp(phone_number)
        request.session['otp'] = otp
        request.session['phone_number'] = phone_number
        request.session['is_registration'] = False

        next_url = request.GET.get('next', '/')
        request.session['next_url'] = next_url

        return redirect('verify_otp')

    return render(request, 'login.html')


# عرض التحقق من OTP
def verify_otp_view(request):
    if request.method == "POST":
        otp1 = request.POST.get("otp1", "")
        otp2 = request.POST.get("otp2", "")
        otp3 = request.POST.get("otp3", "")
        otp4 = request.POST.get("otp4", "")
        entered_otp = otp1 + otp2 + otp3 + otp4  
        stored_otp = request.session.get('otp')
        phone_number = request.session.get('phone_number')
        is_registration = request.session.get('is_registration')

        if not phone_number or not stored_otp:
            return render(request, 'verify_otp.html', {'message': 'Session expired. Please try again.', 'message_type': 'error'})

        if entered_otp == str(stored_otp):
            user_model = get_user_model()

            if is_registration:
                user, created = user_model.objects.get_or_create(phone_number=phone_number)
            else:
                user = user_model.objects.get(phone_number=phone_number)

            login(request, user)
            if is_registration:
                return redirect('update_profile')  

            next_url = request.session.get('next_url', '/')
            return redirect(next_url) 

        else:
            return render(request, 'verify_otp.html', {'message': 'Invalid OTP', 'message_type': 'error'})

    phone_number = request.session.get('phone_number')
    return render(request, 'verify_otp.html', {'phone_number': phone_number})


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile/view_profile.html',)


@login_required
def update_profile_view(request):
    user = request.user

    next_url = request.GET.get('next', '/')

    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(next_url)  
    else:
        form = UserProfileUpdateForm(instance=user)

    return render(request, 'profile/update_profile.html', {'form': form, 'next': next_url})
