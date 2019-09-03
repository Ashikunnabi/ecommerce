from django.urls import path

from .views import IndexView, ProductListView, ProductDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/', ProductListView.as_view(), name='product_list'),
    path('details/', ProductDetailView.as_view(), name='product_detail'),
]