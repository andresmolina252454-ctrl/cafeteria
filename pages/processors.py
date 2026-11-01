from .models import Page

def ctx_dict(request):
    ctx = {}
    ctx['pages'] = Page.objects.all()
    return ctx