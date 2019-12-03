from django.shortcuts import render


def index(request):
    return render(request, 'contacts/home.html')


def programing_languages(request):
    return render(request, 'contacts/programing_languages.html', {
        'languages': ["Python", "JavaScript", 'Java', "C++", 'C#', 'C', 'PHP']
    })