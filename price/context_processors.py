from .models import Priceplan

def menu_link(request):
    link = Priceplan.objects.all()
    return dict(link=link)
