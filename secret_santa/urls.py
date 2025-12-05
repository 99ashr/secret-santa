from django.urls import path
from . import views

app_name = 'secret_santa'

urlpatterns = [
    path('', views.index, name='index'),
    path('participant/', views.participant_page, name='participant'),
    path('api/generate-draw/', views.generate_draw, name='generate_draw'),
    path('api/show-tokens/', views.show_tokens, name='show_tokens'),
    path('api/clear-draw/', views.clear_draw, name='clear_draw'),
    path('api/reveal/', views.reveal_recipient, name='reveal_recipient'),
]
