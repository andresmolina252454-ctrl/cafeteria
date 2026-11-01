from .models import Redsocial

def ctx_dict(request):
    ctx = {}
    links = Redsocial.objects.all()
    for link in links:
        # Crea claves como 'twitter', 'facebook', 'instagram'
        key = link.name.lower().replace(" ", "")
        ctx[key] = link.link
    return ctx