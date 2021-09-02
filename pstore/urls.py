from django.urls import path
from . import views as store
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', store.home, name='home'),
    path('register/', store.register, name='register'),
    path('login/', store.login_request, name='login_request'),
    path('logout/', store.logoutUser, name='logout'),
    path('team/dashboard/', store.teamDash, name='team_dash'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
