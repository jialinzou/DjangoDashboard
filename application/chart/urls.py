from django.conf.urls import url
from .views.chart import Chart
from .views.get_data_linechart import GetDataLine
from .views.get_data_diffchart import GetDataDiff
from .views.get_data_barchart import GetDataBar

urlpatterns = [
    url(r'^$', Chart.as_view(), name="chart"),
    url(r'^get_data_barchart', GetDataBar.as_view(), name="get_data_barchart"),
    url(r'^get_data_diffchart', GetDataDiff.as_view(), name="get_data_diffchart"),
    url(r'^get_data_linechart', GetDataLine.as_view(), name="get_data_linechart"),
    ]