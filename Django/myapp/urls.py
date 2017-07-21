from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # auth/
    url(r'^login$', views.login, name="login"),
    url(r'^register$', views.register, name="register"),
    url(r'^blog-id$', views.default_weblog, name="default_weblog"),
    # blog/
    url(r'^posts$', views.show_posts, name="show_posts"),
    url(r'^default/posts$', views.default_weblog_posts, name="default_weblog_posts"),
    url(r'^post$', views.create_post, name="create_post"),
    url(r'^comments$', views.show_comments, name="show_comments"),
    url(r'^comment$', views.create_comment, name="create_comment"),
    url(r'^search$', views.search, name="search"),
    #url(r'^token/$', views.token_generation, name="token"),
    url(r'^(?P<pk>[0-9]+)/$', views.showw, name="aaaa"),
]