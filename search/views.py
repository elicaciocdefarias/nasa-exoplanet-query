from django.views.generic import TemplateView, RedirectView
from .models import Exoplanet


class IndexView(TemplateView):
    template_name = "search/index.html"


class UploadCSVOrListView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        exoplanet = Exoplanet.objects.all().first()
        url = "upload/" if exoplanet is None else "list/"
        return url
