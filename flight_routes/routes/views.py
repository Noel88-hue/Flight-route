from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import AirportRoute
from .forms import AirportRouteForm, SearchForm


def add_route(request):
    form = AirportRouteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_route')
    return render(request, 'add_route.html', {'form': form})


def find_nth_node(request):
    result = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data['duration']
            position = form.cleaned_data['position']
            n = form.cleaned_data['n']

            target_pos = duration
            if position == 'left':
                for _ in range(n):
                    target_pos = target_pos * 2
            else:
                for _ in range(n):
                    target_pos = target_pos * 2 + 1
                    
            result = AirportRoute.objects.filter(position=str(target_pos)).first()
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'result': result})


def longest_route(request):
    route = AirportRoute.objects.order_by('-duration').first()
    return render(request, 'longest.html', {'route': route})


def shortest_between(request):
    result = None

    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')

        routes = AirportRoute.objects.filter(
            airport_code__in=[start, end]
        ).order_by('duration')

        result = routes.first()

    return render(request, 'shortest.html', {'result': result})
