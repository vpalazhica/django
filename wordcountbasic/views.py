
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'mercury.html')

def about(request):
    return render(request, 'about.html')


def wordcounter(request):
    result = request.GET['alltext']
    wordlist = result.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    print(result)
    return render(request, 'count.html', {'alltext': result, 'count': len(wordlist), 'worddict': sortedwords})