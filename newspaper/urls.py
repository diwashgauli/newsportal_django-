from django.urls import path
from newspaper import views
urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("post-list/",views.PostListView.as_view(),name="post-list"),
    path("post-detail/<int:pk>/",views.PostDetailView.as_view(),name="post-detail"),
    path("about/",views.AboutView.as_view(),name="about"),
    path("contact/",views.ContactCreateView.as_view(),name="contact"),
    path("post-by-category/<int:category_id>/",views.PostByCategoryView.as_view(),name="post-by-category"),
    path("all-categories/",views.CategoryListView.as_view(),name="all-categories"),
    path("all-tags/",views.TagsView.as_view(),name="all-tags"),
    path("post-by-tag/<int:tag_id>/",views.PostByTagView.as_view(),name="post-by-tag"),
    path("comment/",views.CommentView.as_view(),name="comment"),
    path("newsletter/",views.NewsletterView.as_view(),name="newsletter"),
    path("search/",views.PostSearchView.as_view(),name="search"),



]