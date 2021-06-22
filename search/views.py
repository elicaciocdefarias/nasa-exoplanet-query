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
