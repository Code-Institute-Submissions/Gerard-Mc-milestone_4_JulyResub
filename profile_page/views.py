from django.shortcuts import render


def profile(request):
    """ Display the user's profile. """

    template = 'profile_page/profile_page.html'
    context = {}

    return render(request, template, context)
