from django.shortcuts import render
from django.http import HttpResponse, request
from datetime import datetime
from .models import Contact
from django.contrib.messages import constants as messages
import requests
from bs4 import BeautifulSoup
import urllib, json
import pandas as pd
from .Abuse import abuse
from .API import Factcheck
from .Dom_Org import domorg
from .Dom_Reg import domreg
from .Org_Name import orgname
from .Reg_name import regname
from .Web_Age import webage
from .ML import ML_PRED
from .google_search import googleSearch
from requests.api import request, request

def HomeD(request):
    return render(request, 'index.html') 

def Fact_CheckD(request):
    return render(request, 'FactCheck.html')

def About_UsD(request):
    return render(request, 'AboutUs.html') 

def Our_AlgorithmD(request):
    return render(request, 'OurAlgo.html')

def Contact_UsD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date = datetime.today())
        contact.save()
    return render(request, 'ContactUs.html') 

def Home(request):
    return render(request, 'indexNor.html') 

def Fact_Check(request):
    return render(request, 'FactCheckNor.html')

def About_Us(request):
    return render(request, 'AboutUsNor.html') 

def Our_Algorithm(request):
    return render(request, 'OurAlgoNor.html')

def Contact_Us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date = datetime.today())
        contact.save()
    return render(request, 'ContactUsNor.html') 



def Fact(request):
    #INPUTfact = request.GET.get('EnterFact')
    #INPUTkey = request.GET.get('EnterKey')
    return render(request, 'FactNor.html') 

def FactD(request):
    
    return render(request, 'Fact.html')

def Website(request):
    return render(request, 'WebsiteNor.html') 

def WebsiteD(request):
    #inputURL = request.GET.get('EnterURDL')
    return render(request, 'Website.html')



def FactResponse(request):
    INPUTfact = request.GET.get('EnterFact')
    INPUTkey = request.GET.get('EnterKey')

    A=Factcheck(INPUTkey)

    if type(A) == str or None:
        a = "Sorry! This Fact Has Not yet been reviewed by Google"
        b = ""
        c = ""
        d = ""
        e = ""
        P = ""
        Q = ""
        R = ""
        S = ""
        T = ""

    else:
        a = A['TEXT'][0]
        b = A['TEXT'][1]
        c = A['TEXT'][2]
        d = A['TEXT'][3]
        e = A['TEXT'][4]
        P = A['RATING'][0]
        Q = A['RATING'][1]
        R = A['RATING'][2]
        S = A['RATING'][3]
        T = A['RATING'][4]


    B = ML_PRED(INPUTfact)

    C = googleSearch(INPUTfact)

    b0 = C[0]
    b1 = regname(C[0])
    b2 = domreg(C[0])
    b3 = orgname(C[0])
    b4 = domorg(C[0])
    b5 = webage(C[0])
    b6 = abuse(C[0])

    c0 = C[1]
    c1 = regname(C[1])
    c2 = domreg(C[1])
    c3 = orgname(C[1])
    c4 = domorg(C[1])
    c5 = abuse(C[1])
    c6 = webage(C[1])

    d0 = C[2]
    d1 = regname(C[2])
    d2 = domreg(C[2])
    d3 = orgname(C[2])
    d4 = domorg(C[2])
    d5 = abuse(C[2])
    d6 = webage(C[2])

    e0 = C[3]
    e1 = regname(C[3])
    e2 = domreg(C[3])
    e3 = orgname(C[3])
    e4 = domorg(C[3])
    e5 = abuse(C[3])
    e6 = webage(C[3])

    f0 = C[4]
    f1 = regname(C[4])
    f2 = domreg(C[4])
    f3 = orgname(C[4])
    f4 = domorg(C[4])
    f5 = abuse(C[4])
    f6 = webage(C[4])

    FACTparams = {
        "T1": a,
        "T2": b,
        "T3": c,
        "T4": d,
        "T5": e,
        "T6": P,
        "T7": Q,
        "T8": R,
        "T9": S,
        "T10": T,
        "ML_out": B,
        "YourFact": INPUTfact,
        "V0": b0,
        "V1": b1,
        "V2": b2,
        "V3": b3,
        "V4": b4,
        "V5": b5,
        "V6": b6,
        "W0": c0,
        "W1": c1,
        "W2": c2,
        "W3": c3,
        "W4": c4,
        "W5": c5,
        "W6": c6,
        "X0": d0,
        "X1": d1,
        "X2": d2,
        "X3": d3,
        "X4": d4,
        "X5": d5,
        "X6": d6,
        "Y0": e0,
        "Y1": e1,
        "Y2": e2,
        "Y3": e3,
        "Y4": e4,
        "Y5": e5,
        "Y6": e6,
        "Z0": f0,
        "Z1": f1,
        "Z2": f2,
        "Z3": f3,
        "Z4": f4,
        "Z5": f5,
        "Z6": f6,
    }
    return render(request, 'Factresponse.html', FACTparams) 



def FactDResponse(request):
    INPUTfactD = request.GET.get('EnterFactD')
    INPUTkeyD = request.GET.get('EnterKeyD')

    A=Factcheck(INPUTkeyD)

    if type(A) == str or None:
        a = "Sorry! This Fact Has Not yet been reviewed by Google"
        b = ""
        c = ""
        d = ""
        e = ""
        P = ""
        Q = ""
        R = ""
        S = ""
        T = ""

    else:
        a = A['TEXT'][0]
        b = A['TEXT'][1]
        c = A['TEXT'][2]
        d = A['TEXT'][3]
        e = A['TEXT'][4]
        P = A['RATING'][0]
        Q = A['RATING'][1]
        R = A['RATING'][2]
        S = A['RATING'][3]
        T = A['RATING'][4]

    

    B = ML_PRED(INPUTfactD)

    C = googleSearch(INPUTfactD)

    b0 = C[0]
    b1 = regname(C[0])
    b2 = domreg(C[0])
    b3 = orgname(C[0])
    b4 = domorg(C[0])
    b5 = webage(C[0])
    b6 = abuse(C[0])

    c0 = C[1]
    c1 = regname(C[1])
    c2 = domreg(C[1])
    c3 = orgname(C[1])
    c4 = domorg(C[1])
    c5 = webage(C[1])
    c6 = abuse(C[1])

    d0 = C[2]
    d1 = regname(C[2])
    d2 = domreg(C[2])
    d3 = orgname(C[2])
    d4 = domorg(C[2])
    d5 = webage(C[2])
    d6 = abuse(C[2])

    e0 = C[3]
    e1 = regname(C[3])
    e2 = domreg(C[3])
    e3 = orgname(C[3])
    e4 = domorg(C[3])
    e5 = webage(C[3])
    e6 = abuse(C[3])

    f0 = C[4]
    f1 = regname(C[4])
    f2 = domreg(C[4])
    f3 = orgname(C[4])
    f4 = domorg(C[4])
    f5 = webage(C[4])
    f6 = abuse(C[4])

    FACTDparams = {
        "T1": a,
        "T2": b,
        "T3": c,
        "T4": d,
        "T5": e,
        "T6": P,
        "T7": Q,
        "T8": R,
        "T9": S,
        "T10": T,
        "ML_out": B,
        "YourFact": INPUTfactD,
        "V0": b0,
        "V1": b1,
        "V2": b2,
        "V3": b3,
        "V4": b4,
        "V5": b5,
        "V6": b6,
        "W0": c0,
        "W1": c1,
        "W2": c2,
        "W3": c3,
        "W4": c4,
        "W5": c5,
        "W6": c6,
        "X0": d0,
        "X1": d1,
        "X2": d2,
        "X3": d3,
        "X4": d4,
        "X5": d5,
        "X6": d6,
        "Y0": e0,
        "Y1": e1,
        "Y2": e2,
        "Y3": e3,
        "Y4": e4,
        "Y5": e5,
        "Y6": e6,
        "Z0": f0,
        "Z1": f1,
        "Z2": f2,
        "Z3": f3,
        "Z4": f4,
        "Z5": f5,
        "Z6": f6,
    }
    
    return render(request, 'FactresponseD.html', FACTDparams)



def URLresponse(request):
    inputURL = request.GET.get('EnterURL')
    a1 = regname(inputURL)
    a2 = domreg(inputURL)
    a3 = orgname(inputURL)
    a4 = domorg(inputURL)
    a5 = webage(inputURL)
    a6 = abuse(inputURL)

    Web_Params = {
        'zero': inputURL,
        'one': a1,
        'two' : a2,
        'three' : a3,
        'four' : a4,
        'five' : a5,
        'six' : a6,
    }

    return render(request, 'URLresponse.html', Web_Params) 




def URLDresponse(request):
    inputURLD = request.GET.get('EnterURL')
    a1 = regname(inputURLD)
    a2 = domreg(inputURLD)
    a3 = orgname(inputURLD)
    a4 = domorg(inputURLD)
    a5 = webage(inputURLD)
    a6 = abuse(inputURLD)

    WebD_Params = {
        'zero': inputURLD,
        'one': a1,
        'two' : a2,
        'three' : a3,
        'four' : a4,
        'five' : a5,
        'six' : a6,
    }

    return render(request, 'URLresponseD.html', WebD_Params)