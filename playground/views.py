from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.


def say_hello(request):
    query_set = Product.objects.all()
    # To evaluate QuerySet we need to:
        # iterate over it
            # for product in query_set:
            #     print(product)
        # convert it to a list
            # list(query_set)
        # access individual element or slice it
            # query_set[0:5]
    
    return render(request, 'hello.html', {'name': rows_in_table})
