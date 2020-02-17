from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$',views.home, name='home'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.handle_login,name='login'),
    url('logout/',views.handle_logout,name='logout'),
    url('profile/<str:username>/',views.user_profile,name='profile'),
    url('profile/project/upload/',views.handle_project_upload,name='project_upload'),
    url('project/<int:project_id>/',views.project_details,name="project_details"),
    url(r'^ajax/ratings/(\d+)/$',views.ratings,name='ratings'),
    url('profile/update/pic/', views.handle_profile_pic, name='upload_pic'),
    url('search/', views.search_projects,name='search_project'),
    url('^api/profiles/$', views.ProfileList.as_view(), name='api_profiles'), 
    url('^api/projects/$', views.ProjectList.as_view(), name='api_projects'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
