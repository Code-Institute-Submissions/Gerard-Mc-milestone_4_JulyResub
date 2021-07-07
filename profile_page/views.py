from django.shortcuts import render


def profile_page(request):
    """ Returns the profile page """

    return render(request, 'profile_page/profile_page.html')
