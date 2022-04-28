from .models import Mark, MarkItem
from .views import _mark_id


def counter(request):
    mark_count = 0
    if 'admin' in request.path:
        return {}
    else: 
        try:
            mark = Mark.objects.filter(mark_id=_mark_id(request))
            if request.user.is_authenticated:
                mark_items = MarkItem.objects.all().filter(user=request.user)
            else:
                mark_items = MarkItem.objects.all().filter(mark=mark[:1])


        except Mark.DoesNotExist:
            mark_count = 0
    return dict(mark_count = mark_count)


