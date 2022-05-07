from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Pizza

# Create your views here.

def index(request):
    '''The Home Page for Pizzeria.'''
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all() # foreign key is accessed using '_set'
    comments = pizza.comment_set.all()

    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments}

    return render(request, 'pizzas/pizza.html', context)

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
       #CREATES BLANK FORM
        form = CommentForm()
    else:
        
        form = CommentForm(data=request.POST)
      

        if form.is_valid():
          # MAKESURE THE FORM IS FILLED OUT
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)



    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html', context)