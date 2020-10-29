from django.urls import path
from . import views

urlpatterns = [
	path('',  views.Home, name = 'Home'),
    path('Home',  views.Home, name = 'Home'),
    path('FactCheck',  views.Fact_Check, name = 'Fact Check'),
    path('AboutUs',  views.About_Us, name = 'About Us'),
    path('OurAlgorithm',  views.Our_Algorithm, name = 'Our Algorithm'),
    path('ContactUs',  views.Contact_Us, name = 'Fact Check'),
    path('HomeD',  views.HomeD, name = 'Home'),
    path('FactCheckD',  views.Fact_CheckD, name = 'Fact Check'),
    path('AboutUsD',  views.About_UsD, name = 'About Us'),
    path('OurAlgorithmD',  views.Our_AlgorithmD, name = 'Our Algorithm'),
    path('ContactUsD',  views.Contact_UsD, name = 'Fact Check'),

    path('FactCheckD/FactD',  views.FactD, name = 'Fact'),
    path('FactCheckD/WebsiteD',  views.WebsiteD, name = 'Website'),
    path('FactCheck/Fact',  views.Fact, name = 'Fact'),
    path('FactCheck/Website',  views.Website, name = 'Wabsite'),

    path('FactCheckD/FactD/response',  views.FactDResponse, name = 'FactResponseD'),
    path('FactCheckD/WebsiteD/response',  views.URLDresponse, name = 'URLresponseD'),
    path('FactCheck/Fact/response',  views.FactResponse, name = 'FactResponse'),
    path('FactCheck/Website/response',  views.URLresponse, name = 'URLresponse'),
]

