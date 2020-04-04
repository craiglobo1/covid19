from django.shortcuts import render
# from django.http import HttpResponse
from .Combination import WebGA



def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


popSize = 100
elitePercent = 0.3
mutationRate = 0.01
generations= 100



paths = WebGA(popSize,elitePercent,mutationRate,generations)
# Create your views here.
def path(request):
    context ={
        'paths':paths
    }
    return render(request,'paths\index.html',context)