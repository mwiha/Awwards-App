from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include


from .views import home, project_view, signup, profile, edit_profile, upload, index

urlpatterns = [
    url('', home, name='home'),
    url('project/<post>', project_view, name='project'),
    url('signup/', signup, name='signup'),
    url('upload/', upload, name='upload'),
    url('profile/<username>/', profile, name='profile'),
    url('profile/<username>/settings', edit_profile, name='edit'),
    url('account/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
