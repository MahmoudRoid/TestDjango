import csv

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from base import Consts
from base.forms import SignupForm, LoginForm
from base.models import Product


@login_required
def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, Consts.PRODUCT_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)
    return render(request, "home.html", {'product_page': page})


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


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')


def signup(request):
    form = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            bb = form.save()
            return redirect(reverse('login'))  # reverse create a url and paseed to redirect

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def signin(request):
    form = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                # login(request,user)
                return redirect(reverse('home'))

    form = LoginForm()

    return render(request, 'login.html', {'form': form})
