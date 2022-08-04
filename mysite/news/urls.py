from django import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    # path('article/<int:year>/<int:month>/', views.month_archive),
    # path('article/<int:year>/<int:month>/<int:pk>/', views.article.detail),
]
