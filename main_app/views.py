from django.shortcuts import render, redirect
from .models import ProjectCategory, Project, Team, AboutGallery
from .forms import ContactForm

def main_view(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('/')

    categories = ProjectCategory.objects.all()
    contact_form = ContactForm(request.POST)
    team = Team.objects.all()
    image = AboutGallery.objects.all()

    return render(request, 'main_page.html', context={
        'portfolio': categories,
        'contact_form': contact_form,
        'team': team,
        'image': image

    })
