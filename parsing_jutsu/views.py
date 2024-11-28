from django.views import generic
from . import models, forms
from django.http import HttpResponse


class JutsuListView(generic.ListView):
    template_name = "jutsu/jutsu_list.html"
    context_object_name = "jutsu"
    model = models.Jutsu
    paginate_by = 10  
    def get_queryset(self):
        return self.model.objects.all().order_by("-id")


class JutsuFormView(generic.FormView):
    template_name = "jutsu/jutsu_form.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()  
            return HttpResponse("200 OK")
        else:
            return super(JutsuFormView, self).post(request, *args, **kwargs)
