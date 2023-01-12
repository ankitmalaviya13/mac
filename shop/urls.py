from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="ShopHome"),
    path('about', views.about,name="AboutUs"),
    path('contact', views.contact,name="ConatctUs"),
    path('tracker', views.tracker,name="trackinstatus"),
    path('search', views.search,name="Search"),
    path('Productview/<int:myid>', views.productview,name="productview"),
    path('checkout', views.checkout,name="Checkput"),
    path('handlerequest', views.handlerequest,name="handlerequest"),
]


