from django.shortcuts import render
from django.db.models import Q
from store.models import Product
# Create your views here.


def say_hello(request):
    # 🚀 Mastering Django Database Queries! 🚀

    # Django provides powerful ways to query the database, from simple lookups to complex filters! Here’s a rundown of the most essential methods & tricks for efficient data retrieval. 📋

    # 1️⃣ Basic Retrieval:
    #     all(): Gets all records as a QuerySet (like a collection of objects).
    #     get(): Fetches a single object based on criteria, or raises an error if no match or multiple results.
    #     filter(): Retrieves a QuerySet matching specific conditions.
    #     exclude(): Retrieves all records not matching certain criteria.
    # 2️⃣ Common Lookups for Filter:
    #     exact / iexact: Matches a specific value (case-sensitive or insensitive).
    #     contains / icontains: Checks for substring matches.
    #     gt / gte / lt / lte: Greater, greater or equal, less, or less or equal than.
    #     startswith / endswith: Field starts or ends with a substring.
    #     isnull=True: Checks if a field is null.
    # 3️⃣ Complex Lookups with Q Objects:
    # For advanced logic, Q objects let you use AND, OR, NOT:
    #     from django.db.models import Q
    #     results = Model.objects.filter(Q(field1=value1) | ~Q(field2=value2))
    # Combine multiple conditions with &, |, and ~ for AND, OR, NOT conditions.
    # Master these for ultimate query control! 🔍💡

    queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    
    return render(request, 'hello.html', {'name': "Bini", 'products': list(queryset)})
