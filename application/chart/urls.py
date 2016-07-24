from django.conf.urls import url
from .views.chart import Chart
from .views.get_users_per_channel import GetUsersPerChannle
from .views.get_top_pages import GetTopPages
from .views.get_top_posts import GetTopPosts
from .views.get_concurrents import GetConcurrents

urlpatterns = [
    url(r'^$', Chart.as_view(), name="chart"),
    url(r'^get_users_per_channel', GetUsersPerChannle.as_view(), name="get_users_per_channel"),
    url(r'^get_top_pages', GetTopPages.as_view(), name="get_top_pages"),
    url(r'^get_top_posts', GetTopPosts.as_view(), name="get_top_posts"),
    ]