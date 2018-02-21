import sys
from os import getcwd

from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.template.loader import render_to_string

settings.configure(
    DEBUG=True,
    SECRET_KEY='A-random-secret-key!',
    ROOT_URLCONF=sys.modules[__name__],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates', 
            'DIRS': [
                getcwd()
                ],
            },
        ]
)


def index(request):
    return HttpResponse("""<p><a href="./about/">About</a></p> 
            <h1>Minimal Django!</h1>""")

def about(request):
    title = 'Tinyapp'
    author = 'Akinwunmi Oluwaseun'
    html = render_to_string('about.html', {'title':title, 'author': author,})
    return HttpResponse(html)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
