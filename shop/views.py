from django.shortcuts import render, reverse, redirect
from shop.forms import BillItemForm, BillForm
from django.http import HttpResponseRedirect
from shop.models import Product


# Create your views here.
def show_bill(request):
    # we should get the bill from session but here we have only one product
    # so we are going with this now
    if request.method == 'GET':
        if 'count' in request.GET:
            try:
                count = int(request.GET['count'])
            except Exception as e:
                return render(request, 'shop/bill.html', context={
                    'errors': [
                        'no items specified we cant show bill.'
                    ],
                    'error_only': True
                })
            else:
                # todo:permanently
                product = Product.objects.first()
                bill = [
                    (product, count, product.price * count)
                ]
                total_price = product.price * count
                form = BillForm()
                return render(request, 'shop/bill.html', context={
                    'form': form,
                    'bill': bill,
                    'total_price': total_price
                })

        else:
            return render(request, 'shop/bill.html', context={
                'errors': [
                    'no items specified we cant show bill.'
                ],
                'error_only': True
            })
    elif request.method == 'POST':
        pass


def detail(request, product_id=1):
    if request.method == 'POST':
        form = BillItemForm(request.POST)
        if form.is_valid():
            # here we are passing bill item information (count only for now) in get parameters
            # it should change to basket model
            return redirect(f"{reverse('shop:bill')}?count={form.cleaned_data['count']}")
        else:
            return render(request, template_name='shop/detail.html', context={'form': form, 'errors': form.errors})
    else:
        form = BillItemForm()
        return render(request, template_name='shop/detail.html', context={'form': form})


# def return from bank

def order_status(request):
    pass
