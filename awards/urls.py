from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from awards.forms import SignupForm
from .views import home, project_view, signup, profile, edit_profile, upload, index

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^project/<post>', project_view, name='project'),
    url(r'^signup/', signup, name='signup'),
    url(r'^upload/', upload, name='upload'),
    url(r'^profile/<username>/', profile, name='profile'),
    url(r'^profile/<username>/settings', edit_profile, name='edit'),
    url(r'^account/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







