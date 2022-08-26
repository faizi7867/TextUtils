# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'name': 'faizi', 'place': 'bangalore'})


def analyze(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get("removepunc", 'off')
    capitalize = request.POST.get("capitalize", 'off')
    uppers = request.POST.get("upper", 'off')
    punc = '?!,'
    analyzed = ""
    if text:
        if removepunc != 'off':
            for c in text:
                if c not in punc:
                    analyzed += c

        elif capitalize != 'off':
            analyzed = " ".join([t.capitalize() for t in text.split(' ')])

        elif uppers != 'off':
            analyzed = text.upper()

    params = {'analyzedTxt': analyzed}
    return render(request, 'analyze.html', params)
