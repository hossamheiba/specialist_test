from django.shortcuts import render, redirect, get_object_or_404
from .models import JobInfo, JobApplication
from django.contrib import messages
from django.utils.translation import gettext as _

def submit_job_application(request):
    job_info = JobInfo.objects.first()  # جلب أول كائن موجود أو None إذا لم يوجد
    context = {"job_info": job_info}

    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('number', '').strip()
        job_title = request.POST.get('job_title', '').strip()
        experience_years = request.POST.get('experience_years', '').strip()
        resume = request.FILES.get('resume')
        portfolio = request.FILES.get('portfolio')
        about = request.POST.get('about', '').strip()

        if not name or not email or not job_title or not phone_number or not experience_years or not resume or not about:
            messages.error(request, _("Please fill in all required fields."))
            return render(request, 'Jobs.html', context)

        job_application = JobApplication.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            job_title=job_title,
            experience_years=experience_years,
            resume=resume,
            portfolio=portfolio,
            about=about
        )

        messages.success(request, _("Your application has been submitted successfully!"))
        return redirect('jobs') 

    return render(request, 'Jobs.html', context)