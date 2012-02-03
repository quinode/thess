from django.conf import settings
        
def site_settings(request):
    return {'SITE_TITLE' : settings.SITE_TITLE,
            'SITE_AUTHOR' : settings.SITE_AUTHOR,}        