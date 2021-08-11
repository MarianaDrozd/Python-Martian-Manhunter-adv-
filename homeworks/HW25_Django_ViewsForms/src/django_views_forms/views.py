from django.views.generic import TemplateView


class MainPageTemplateView(TemplateView):
    template_name = 'index.html'
