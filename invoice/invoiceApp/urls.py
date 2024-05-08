from django.urls import path
from .views import GetInvoice,OneInvoice,SetInvoice,InvoiceAddItem
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path("new",csrf_exempt(SetInvoice.as_view())),
    path("",csrf_exempt(GetInvoice.as_view())),
    path("<str:pk>",csrf_exempt(OneInvoice.as_view())),
    path("<str:pk>/items",csrf_exempt(InvoiceAddItem.as_view()))
]