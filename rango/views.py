from django.shortcuts import render


def index(request):
    # Data we want to show in the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Render the template 'rango/index.html' with the context
    return render(request, 'rango/index.html', context=context_dict)