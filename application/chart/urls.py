from django.conf.urls import url
from .views.chart import Chart
from .views.get_data_linechart import GetDataLine
from .views.get_data_diffchart import GetDataDiff
from .views.get_data_barchart import GetDataBar
from .views.get_data_bullet import GetDataBullet
from .views.get_users_per_channel import GetUsersPerChannle

urlpatterns = [
    url(r'^$', Chart.as_view(), name="chart"),
    url(r'^get_data_barchart', GetDataBar.as_view(), name="get_data_barchart"),
    url(r'^get_data_diffchart', GetDataDiff.as_view(), name="get_data_diffchart"),
    url(r'^get_data_linechart', GetDataLine.as_view(), name="get_data_linechart"),
    url(r'^get_data_bullet', GetDataBullet.as_view(), name="get_data_bullet"),
    url(r'^get_users_per_channel', GetUsersPerChannle.as_view(), name="get_users_per_channel"),
    ]