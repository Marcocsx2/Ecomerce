from django.shortcuts import get_object_or_404, render
from . import models

Producto = models.Producto

template_index = 'index.html'
template_producto = 'producto.html'

# Create your views here.
def index(request):
    product_list =Producto.objects.order_by('nombre')[:6]
    context = {'product_list' : product_list}
    return render(request, template_index, context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, template_producto, {'producto': producto})
    