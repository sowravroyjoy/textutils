# I have created this file - Sowrav
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Sowrav', 'place': 'BD'}
    return render(request, 'index.html', params)
    # return HttpResponse('''Hello <a href = "https://www.youtube.com/"> Youtube </a>''')


def about(request):
    return HttpResponse("About")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {
            'purpose': 'Changed to Uppercase',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {
            'purpose': 'Removed NewLines',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {
            'purpose': 'Extra Space Remover',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = ""
        count = 0
        for char in djtext:
            analyzed = analyzed + char
            if char == " " or char == "\n":
                pass
            else:
                count += 1

        params = {
            'purpose': 'Char Count',
            'analyzed_text': analyzed,
            'charcount': count
        }
        djtext = analyzed
    return render(request, 'analyze.html', params)

def ex1(request):
    return HttpResponse('''Hello <a href = "https://www.youtube.com/"> Youtube </a>''')


