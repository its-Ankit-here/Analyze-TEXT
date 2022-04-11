# text analyzer 
# IT will analyze the text and display the content on template which satisfy the condition

from ctypes.wintypes import tagPOINT
from django.shortcuts import render
from django.http import HttpResponse

def textanalyze(request):
    return render(request,'textanalyzer.html')
    
def analyzeresult(request):
    removepunc = request.GET.get('removepunc','off')
    charcount = request.GET.get('charcount', 'off')
    enteredtext= request.GET.get('textanalyze', 'default')
    
    resulttext ={'result': enteredtext}
    punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzetext =''
    if removepunc == 'on':
        # condition to remove punctuation marks 
        for char in enteredtext:
            if char not in punctuations:
                analyzetext= analyzetext + char
        print(enteredtext)
        enteredtext = analyzetext
    else:
        analyzetext = enteredtext    
    if charcount == "on":
        # condition to find total character number
        char_count = len(enteredtext)
        
    resulttext = {'result':enteredtext, 'after':char_count}
    #render(request, 'analyzeresult.html',total_count)
    return render(request, 'analyzeresult.html',resulttext )