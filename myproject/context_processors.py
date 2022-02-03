from django.conf import settings # import the settings file

def admin_media(request):
    # return the value you want as a dictionary. you may add multiple values in there.
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_URL': settings.SITE_URL,
        'COMPANY_NAME': settings.COMPANY_NAME,
        'COMPANY_CONTACT_EMAIL': settings.COMPANY_CONTACT_EMAIL,
        'THEME_NAME': settings.THEME_NAME
    }