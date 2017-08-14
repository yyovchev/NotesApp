from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.views import generic


from .models import Note


# Create your views here.

class IndexView(TemplateView):
    model = Note
    template_name = 'notes/index.html'


def add_note(request):
    if request.method == "POST":
        key = request.POST['key']

        if key == '':
            return render(request, 'notes/index.html', {'error': 'key cant be empty', })

        text = request.POST['text']
        if text == '':
            return render(request, 'notes/index.html', {'error': 'text cant be empty', })

        note = Note(text=text, key=key)
        note.save()
        return render(request, 'notes/index.html', {'message': 'note add successfully', })

    else:
        return redirect('notes:index')


def search(request):
    if request.method == "POST":
        try:
            selected_note = Note.objects.get(
                pk=request.POST['key']
            )
        except (KeyError, Note.DoesNotExist):
            return render(request, 'notes/index.html', {'error': 'Note doesnt exist', })
        else:
            return HttpResponseRedirect(reverse('notes:show_note',
                                                args=(selected_note.key,)))
    else:
        return redirect('notes:index')


class ShowNote(generic.DetailView):
    model = Note
    template_name = 'notes/show_note.html'
