from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def count(request):
    fullText = request.GET['fullText']

    wordList = fullText.split()

    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            #increase
            wordDictionary[word] += 1
        else:
            #add to wordDictionary
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fullText':fullText, 'count':len(wordList), 'sortedWords':sortedWords})
