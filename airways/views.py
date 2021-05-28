from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.apps import apps


def form_factory(cls):
    class Form(ModelForm):
        class Meta:
            exclude = []
            model = models_dict[cls]
    return Form


models_dict = {model.__name__.lower(): model for model in apps.get_app_config('airways').get_models()}
forms = {model: form_factory(model) for model in models_dict.keys()}


class IndexView(generic.TemplateView):
    template_name = 'airways/index.html'


def read(request, cls):
    return render(request, f'airways/models/{cls}.html', {'items': models_dict[cls].objects.all()})


def create(request, cls):
    form = forms[cls](request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('airways:Read', cls)
    return render(request, 'airways/form_create.html', {'form': form})


def update(request, cls, id):
    item = get_object_or_404(models_dict[cls], pk=id)
    form = forms[cls](request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('airways:Read', cls)
    return render(request, 'airways/form_update.html', {'form': form})


def delete(request, cls, id):
    item = get_object_or_404(models_dict[cls], pk=id)
    if request.method == "POST":
        item.delete()
        return redirect('airways:Read', cls)
    return render(request, 'airways/form_delete.html', {cls+'_id': item})

