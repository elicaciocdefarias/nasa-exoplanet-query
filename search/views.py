from search.handlers import HandleFile
from search.forms import ExoplanetUploadCSVFileForm
from django.views.generic import TemplateView, FormView, ListView
from search.models import Exoplanet


class IndexView(TemplateView):
    template_name = "search/index.html"


class ExoplanetListView(ListView):
    template_name = "search/list.html"
    model = Exoplanet


class ExoplanetUploadView(FormView):
    template_name = "search/upload_csv.html"
    form_class = ExoplanetUploadCSVFileForm
    success_url = "/list/"

    def form_valid(self, form):
        file = form.cleaned_data["file"]
        handle_file = HandleFile(file)
        if handle_file.is_type_csv() and handle_file.structure_is_valid():
            for record in handle_file.records():
                print(record)
            return super().form_valid(form)
        return super().form_invalid(form)
