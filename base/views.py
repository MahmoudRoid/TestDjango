import csv
from datetime import datetime

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView

from base.models import Product



def home(request):
    now = datetime.now()
    return render(request , 'home.html', {'time': now})


class ProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'product.html', {'product': product})



# def product(request , product_id):
#     product = get_object_or_404(Product , pk = product_id )
    # return HttpResponse()
    # return render(request,'product.html', { 'Product': Product } )



class AboutView(TemplateView):
    template_name = 'about.html'


@user_passes_test(lambda u: u.is_staff)
def report(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="MyReport.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response