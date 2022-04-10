# text analyzer 
# IT will analyze the text and display the content on template which satisfy the condition

from django.shortcuts import render
from django.http import HttpResponse

def textanalyze(request):
    return render(request,'textanalyzer.html')
    
def analyzeresult(request):
    removepunc = request.GET.get('removepunc','off')
    enteredtext= request.GET.get('textanalyze', 'default')
    resulttext ={'result': enteredtext}
    punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzextext = ''
    if removepunc == 'on':
        for char in enteredtext:
            if char not in punctuations:
                analyzextext= analyzextext + char
            print(analyzextext)
        print(analyzextext)
        resulttext = {'result':analyzextext}
    
    return render(request, 'analyzeresult.html',resulttext )
    