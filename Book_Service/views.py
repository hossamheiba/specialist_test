from datetime import datetime, time as dt_time 
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from datetime import datetime
from django.contrib import messages
from Contact_Us.models import ContactUs
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def send_appointment_email(appointment_details):
    subject = f"حجز موعد جديد من {appointment_details['first_name']} {appointment_details['last_name']}"
    message = f"""
    تم حجز موعد جديد:

    الاسم: {appointment_details['first_name']} {appointment_details['last_name']}
    رقم الهاتف: {appointment_details['phone_number']}
    ماركة السيارة: {appointment_details['car_brand']}
    طراز السيارة: {appointment_details['car_model']}
    نوع المحرك: {appointment_details['engine_type']}
    سنة التصنيع: {appointment_details['manufacturing_year']}
    تاريخ الموعد: {appointment_details['appointment_date']}
    وقت الموعد: {appointment_details['appointment_time']}
    الملاحظات: {appointment_details['notes']}
    """
    if appointment_details.get('coupon_code'):
        message += f"\n\nالكوبون: {appointment_details['coupon_code']}\nقيمة الخصم: {appointment_details['discount_percentage']}%"
        
    recipient_emails = ['hossamheiba6@gmail.com', 'hossamheiba7@gmail.com']
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_emails, fail_silently=False)


def validate_coupon(coupon_code):
    try:
        coupon = DiscountCoupon.objects.get(code=coupon_code, is_active=True)
        coupon.deactivate_if_expired()  
        return coupon if coupon.is_active else None
    except DiscountCoupon.DoesNotExist:
        return None  
    
def check_coupon(request):
    if request.method == "POST":
        coupon_code = request.POST.get("coupon_code", "").strip()  
        coupon = validate_coupon(coupon_code)
        if coupon:
            discount_percentage = round(coupon.discount_value, 2)  
            discount_percentage = f"{discount_percentage}" 
            return JsonResponse({
                "valid": True,
                "message": "تم تطبيق الكوبون بنجاح",
                "discount_percentage": discount_percentage  
            })
        else:
            return JsonResponse({
                "valid": False,
                "message": "الكوبون غير صالح أو انتهت صلاحيته."
            })
    return JsonResponse({"error": "طلب غير صالح."}, status=400)




@login_required
def book_appointment(request):
    car_brands = CarBrand.objects.all()
    contact = ContactUs.objects.first()
    unavailable_dates = [date_obj.date.isoformat() for date_obj in UnavailableDate.objects.all()]
    selected_brand_id = request.GET.get("car_brand")
    car_models = CarModel.objects.filter(brand_id=selected_brand_id) if selected_brand_id else []
    engine_types = EngineType.objects.all()
    coupons = DiscountCoupon.objects.filter(is_active=True)
    coupon_message = None
    discount_percentage = None

    if request.method == "POST":
        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")
        first_name = request.user.first_name
        last_name = request.user.last_name
        phone_number = request.user.phone_number
        car_brand = request.POST.get("car_brand")
        car_model = request.POST.get("car_model")
        engine_type = request.POST.get("engine_type")
        manufacturing_year = request.POST.get("manufacturing_year")
        notes = request.POST.get("notes", "")
        coupon_code = request.POST.get("coupon_code", "").strip()
        coupon = validate_coupon(coupon_code)
        discount_value = coupon.discount_value if coupon else 0 
        discount_percentage = round(discount_value, 2) if coupon else None
        
        

        if not appointment_time:
            return JsonResponse({"message": "يرجى اختيار وقت الموعد."}, status=400)

        try:
            time_obj = datetime.strptime(appointment_time, "%I:%M %p").time()  # تحويل AM/PM
            
            if not (dt_time(8, 0) <= time_obj <= dt_time(19, 0)):
                return JsonResponse(
                    {"message": "الوقت خارج النطاق المسموح به (من 8 صباحًا إلى 7 مساءً)."},
                    status=400
                )

            appointment_time = time_obj.strftime("%H:%M")
        except ValueError:
            return JsonResponse(
                {"message": "الوقت المدخل غير صحيح. يرجى استخدام تنسيق HH:MM AM/PM."},
                status=400
            )


        is_booked = Appointment.objects.filter(
            appointment_date=appointment_date, appointment_time=appointment_time
        ).exists()
        
        if is_booked:
            messages.error(request, "الموعد محجوز مسبقًا. الرجاء اختيار موعد آخر.")
            return render(request, 'appointment_form.html', {
                'data': request.POST.dict(),
                'car_brands': car_brands,
                'car_models': car_models,
                'engine_types': engine_types,
                'unavailable_dates': unavailable_dates,
                'contact': contact,
                'manufacturing_year': manufacturing_year,
                'selected_brand_id': selected_brand_id,
                'coupon_message': coupon_message
            })

        if coupon_code:
            coupon = validate_coupon(coupon_code)
            if not coupon:
                coupon_message = "الكوبون غير صالح أو انتهت صلاحيته."
            else:
                coupon_message = "تم تطبيق الكوبون بنجاح!"
                discount_percentage = f"{coupon.discount_value}%"

        appointment = Appointment.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            car_brand_id=car_brand,
            car_model_id=car_model,
            engine_type_id=engine_type,
            manufacturing_year=manufacturing_year,
            appointment_date=appointment_date,
            appointment_time=appointment_time, 
            notes=notes,
            discount_value=discount_value,  

        )

        send_appointment_email({
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'car_brand': car_brand,
            'car_model': car_model,
            'engine_type': engine_type,
            'manufacturing_year': manufacturing_year,
            'appointment_date': appointment_date,
            'appointment_time': appointment_time,
            'notes': notes,
            'coupon_code': coupon_code if coupon_code else None,
            'discount_percentage': discount_percentage if discount_percentage is not None else 'لا يوجد'
        })

        return redirect('Book_Service:done_appointment')

    today = datetime.now().isoformat()[:10]
    current_year = datetime.now().year
    years = list(range(current_year - 30, current_year + 1))

    return render(request, "appointment_form.html", {
        "years": years,
        "car_brands": car_brands,
        "car_models": car_models,
        "engine_types": engine_types,
        "unavailable_dates": unavailable_dates,
        "contact": contact,
        "selected_brand_id": selected_brand_id,
        "coupons": coupons,
        "coupon_message": coupon_message,
        "discount_percentage": discount_percentage
    })

@login_required
def get_car_models(request):
    car_brand_id = request.GET.get("car_brand")
    if car_brand_id:
        car_models = CarModel.objects.filter(brand_id=car_brand_id).values("id", "name")
        return JsonResponse({"models": list(car_models)}, safe=False)
    return JsonResponse({"models": []}, safe=False)

# _______________________________________________________________________________________________________________________________________________

def send_location_email(first_name, last_name, phone_number, latitude, longitude):
    subject = f"موقع جديد من {first_name} {last_name}"
    
    google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    
    message = f"""
    تم إرسال موقع جديد:

    الاسم: {first_name} {last_name}
    رقم الهاتف: {phone_number}
    خط العرض: {latitude}
    خط الطول: {longitude}
    
    الرابط على Google Maps: {google_maps_link}
    """
    
    recipient_emails = ['hossamheiba6@gmail.com', 'hossamheiba7@gmail.com']
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  
        recipient_emails,  
        fail_silently=False,
    )

@login_required
def submit_location(request):
    if request.method == "POST":
        first_name = request.user.first_name
        last_name = request.user.last_name
        phone_number = request.user.phone_number
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # التحقق من أن الحقول غير فارغة
        if not latitude or not longitude:
            messages.error(request, "يرجى تقديم إحداثيات الموقع.")
            return redirect('Book_Service:submit_location')
        
        # تحويل الإحداثيات إلى أرقام إذا كانت قيم صحيحة
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            messages.error(request, "الإحداثيات غير صحيحة. يرجى تقديم قيم صحيحة.")
            return redirect('Book_Service:submit_location')

        # إذا كانت القيم صحيحة، قم بحفظ الموقع وإرسال البريد الإلكتروني
        save_location(first_name, last_name, phone_number, latitude, longitude)
        send_location_email(first_name, last_name, phone_number, latitude, longitude)

        return redirect('Book_Service:done_location')
    
    return render(request, "location_form.html")

def save_location(first_name, last_name, phone_number, latitude, longitude):
    Date_of_submission = datetime.now()
    location, created = Location.objects.get_or_create(
        first_name=first_name, 
        last_name=last_name, 
        phone_number=phone_number,
        latitude=latitude,
        longitude=longitude,
        Date_of_submission=Date_of_submission,
    )
    location.save()




@login_required
def appointments_view(request):
    user = request.user
    
    # appointments = Appointment.objects.filter(phone_number=user.phone_number, appointment_date__gte=now())

    appointments = Appointment.objects.filter(phone_number=user.phone_number)

    return render(request, 'appointments.html', {'user': user, 'appointments': appointments})


def location_appointment(request):
    return render(request, 'loc_app.html')

def success_done_appointment(request):
    return render(request, 'done_appointment.html')

def success_done_location(request):
    return render(request, 'done_location.html')


# اذا يتم التحديث فقط 
# def save_location(first_name, last_name, phone_number, latitude, longitude):
#     Date_of_submission = datetime.now()
#     location, created = Location.objects.get_or_create(
#         first_name=first_name, 
#         last_name=last_name, 
#         phone_number=phone_number,
#     )
#     location.latitude = latitude
#     location.longitude = longitude
#     location.Date_of_submission = Date_of_submission
#     location.save()

# def success_page(request):
#     return render(request, 'done_appointment.html')









# def send_location_email(first_name, last_name, phone_number, latitude, longitude):
#     subject = f"موقع جديد من {first_name} {last_name}"
    
#     google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    
#     # تنسيق الرسالة باستخدام HTML
#     message = f"""
#     <html>
#     <head>
#         <style>
#             body {{
#                 font-family: Arial, sans-serif;
#                 background-color: #f4f4f9;
#                 color: #333;
#                 line-height: 1.6;
#                 margin: 0;
#                 padding: 20px;
#             }}
#             .container {{
#                 background-color: #ffffff;
#                 border-radius: 8px;
#                 padding: 20px;
#                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             }}
#             h2 {{
#                 color: #f26b3c;
#             }}
#             .info {{
#                 margin: 10px 0;
#                 padding: 10px;
#                 background-color: #f9f9f9;
#                 border-left: 5px solid #f26b3c;
#             }}
#             a {{
#                 color: #f26b3c;
#                 text-decoration: none;
#             }}
#             .footer {{
#                 font-size: 12px;
#                 color: #777;
#                 margin-top: 20px;
#             }}
#         </style>
#     </head>
#     <body>
#         <div class="container">
#             <h2>تم إرسال موقع جديد</h2>
#             <div class="info">
#                 <strong>الاسم:</strong> {first_name} {last_name}<br>
#                 <strong>رقم الهاتف:</strong> {phone_number}<br>
#                 <strong>خط العرض:</strong> {latitude}<br>
#                 <strong>خط الطول:</strong> {longitude}<br>
#             </div>
#             <p>يمكنك مشاهدة الموقع على الخريطة من خلال الرابط التالي:</p>
#             <p><a href="{google_maps_link}" target="_blank">عرض الموقع على Google Maps</a></p>
#         </div>
#         <div class="footer">
#             <p>شكراً لاستخدامك خدمتنا!</p>
#         </div>
#     </body>
#     </html>
#     """
    
#     recipient_emails = ['hossamheiba6@gmail.com', 'hossamheiba7@gmail.com']
    
#     send_mail(
#         subject,
#         message,
#         settings.DEFAULT_FROM_EMAIL,  
#         recipient_emails,  
#         fail_silently=False,
#         html_message=message  # التأكيد على إرسال الرسالة بتنسيق HTML
#     )














