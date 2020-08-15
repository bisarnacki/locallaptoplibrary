from django.shortcuts import render
from django.views import generic
from catalog.models import Laptop, Manufacturer, LaptopInstance, Make

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Laptop.objects.all().count()
    num_instances = LaptopInstance.objects.all().count()
    
    # Available laptops (status = 'a')
    num_instances_available = LaptopInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_manufacturers = Manufacturer.objects.count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class LaptopListView(generic.ListView):
    model = Laptop
    paginate_by = 10

"""class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location"""

def get_queryset(self):
    return Laptop.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

class BookDetailView(generic.DetailView):
    model = Laptop