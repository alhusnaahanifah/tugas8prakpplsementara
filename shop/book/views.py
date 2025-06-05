from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import ProductForm

def product_list(request):
    products = Book.objects.all()
    
    # Hitung statistik
    total_books = Book.objects.count()
    total_genres = Book.objects.values('genre').distinct().count()
    total_authors = Book.objects.values('author').distinct().count()
    
    context = {
        'products': products,
        'total_books': total_books,
        'total_genres': total_genres,
        'total_authors': total_authors,
    }
    return render(request, 'product_list.html', context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil ditambahkan!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diperbarui!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Book, pk=pk)
    product.delete()
    messages.success(request, 'Produk berhasil dihapus!')
    return redirect('product_list')
