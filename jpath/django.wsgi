import os
import sys
import django.core.handlers.wsgi

path = '/run/media/giulliano/Desenvolvimento/workspace/python/jsonpath/jpath/'
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
