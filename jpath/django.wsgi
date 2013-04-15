import os
import sys
import django.core.handlers.wsgi

#desenv
sys.path.append('/run/media/giulliano/Desenvolvimento/workspace/python/jsonpath/jpath/')
#prod
sys.path.append('/var/www/jsonpath/jpath/jpath/')
sys.path.append('/var/www/jsonpath/jpath/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
