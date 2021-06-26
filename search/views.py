from search.helpers import get_next_five_pages
from django.views.generic import TemplateView, ListView
from search.models import Exoplanet


class IndexView(TemplateView):
    template_name = "search/index.html"


class ExoplanetListView(ListView):
    template_name = "search/list.html"
    paginate_by = 5
    model = Exoplanet

    def get_queryset(self):
        return super().get_queryset().order_by("pk")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_page = context["page_obj"].number
        last_page = context["page_obj"].paginator.num_pages
        context["next_fives_pages"] = get_next_five_pages(
            current_page,
            last_page,
        )

        return context
