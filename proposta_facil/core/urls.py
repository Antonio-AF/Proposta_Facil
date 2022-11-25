from django.urls import path

from .views import index, painel, dologin, store, signup, proposta, dashboard

urlpatterns = [

    path('', index, name='index'),
    path('painel/', painel, name='painel'),
    path('dologin/', dologin),
    path('signup/', signup, name='signup'),
    path('store/', store, name='store'),
    path('proposta/', proposta, name='proposta'),
    path('dashboard/', dashboard, name='dashboard'),

]

