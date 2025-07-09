from django.urls import path
from .views import DashboardView
from dashboard import views

app_name = "dashboard"  

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("dashboard/delete/<int:pk>/", views.PostDeleteView.as_view(), name="post_delete"),
    path("dashboard/update/<int:pk>/",views.PostUpdateView.as_view(),name="post_update"),
    path("dashboard/add/",views.PostAddView.as_view(),name="post_add"),
]
