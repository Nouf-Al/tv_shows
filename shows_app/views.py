from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def root(request):
    return redirect('/shows')


def all_shows(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, 'all_shows.html', context)


def new_show(request):
    return render(request, 'new_show.html')


def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        title = request.POST['title']
        network = request.POST['network']
        desc = request.POST['desc']
        release_date = request.POST['release_date']
        new_show = Show.objects.create(title=title,network=network,desc=desc,release_date=release_date)
        messages.success(request, "Show successfully created")
        # redirect to a success route
        return redirect('view_show', new_show.id)


def view_show(request, id):
    context = {'show': Show.objects.get(id=id)}
    return render(request, 'view_show.html', context)


def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')


def edit_show(request, id):
    context = {'show_edited': Show.objects.get(id=id)}
    return render(request, 'edit_show.html', context)


def update_show(request, id):
    errors = Show.objects.update_validator(request.POST,id)
    if len(errors) >0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value,id)
        # redirect the user back to the form to fix the errors
        return redirect('edit_show',id)
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.desc = request.POST['desc']
        show.release_date = request.POST['release_date']
        show.save()
        messages.success(request, "Show successfully updated")
        return redirect('view_show',id)