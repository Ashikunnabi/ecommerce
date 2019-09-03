from django.shortcuts import render
from django.views.generic import ListView, TemplateView

class IndexView(TemplateView):
    template_name = 'product/index.html'
    
    def get_context_data(self, **kwargs):    
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a Title of response page
        context['title'] = 'Home'
        return context
        
# change the view as list view        
class ProductListView(TemplateView):
    template_name = 'product/category.html'
    
    def get_context_data(self, **kwargs):    
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a Title of response page
        context['title'] = 'CategoryName'
        return context
        
# change the view as detail view        
class ProductDetailView(TemplateView):
    template_name = 'product/single-product.html'
    
    def get_context_data(self, **kwargs):    
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a Title of response page
        context['title'] = 'ProductName'
        return context