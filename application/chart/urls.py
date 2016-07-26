from django.conf.urls import url
from .views.chart import Chart
from .views.get_users_per_channel import GetUsersPerChannle
from .views.get_top_pages import GetTopPages
from .views.get_top_posts import GetTopPosts

from .views.bicycling import Bicycling
from .views.get_posts_BI import GetBIPosts
from .views.get_BI_users import GetBIUsers

from .views.womenshealth import Womenshealth
from .views.get_posts_WH import GetWHPosts
from .views.get_WH_users import GetWHUsers

from .views.runnersworld import Runnersworld
from .views.get_posts_RW import GetRWPosts
from .views.get_RW_users import GetRWUsers

from .views.menshealth import Menshealth
from .views.get_posts_MH import GetMHPosts
from .views.get_MH_users import GetMHUsers

from .views.prevention import Prevention
from .views.get_posts_PVN import GetPVNPosts
from .views.get_PVN_users import GetPVNUsers

from .views.organiclife import Organiclife
from .views.get_posts_ROL import GetROLPosts
from .views.get_ROL_users import GetROLUsers

from .views.rodalewellness import Rodalewellness
from .views.get_posts_WE import GetWEPosts
from .views.get_WE_users import GetWEUsers

urlpatterns = [
    url(r'^$', Chart.as_view(), name="chart"),
    url(r'^network$', Chart.as_view(), name="chart"),
    url(r'^get_users_per_channel', GetUsersPerChannle.as_view(), name="get_users_per_channel"),
    url(r'^get_top_pages', GetTopPages.as_view(), name="get_top_pages"),
    url(r'^get_top_posts', GetTopPosts.as_view(), name="get_top_posts"),
    
    
    url(r'^bicycling$', Bicycling.as_view(), name="bicycling"),
    url(r'^get_posts_BI', GetBIPosts.as_view(), name="get_posts_BI"),
    url(r'^get_BI_users', GetBIUsers.as_view(), name="get_BI_users"),
        
    url(r'^runnersworld$', Runnersworld.as_view(), name="runnersworld"),
    url(r'^get_posts_RW', GetRWPosts.as_view(), name="get_posts_RW"),
    url(r'^get_RW_users', GetRWUsers.as_view(), name="get_RW_users"),
        
    url(r'^prevention$', Prevention.as_view(), name="prevention"),
    url(r'^get_posts_PVN', GetPVNPosts.as_view(), name="get_posts_PVN"),
    url(r'^get_PVN_users', GetPVNUsers.as_view(), name="get_PVN_users"),
        
    url(r'^menshealth$', Menshealth.as_view(), name="menshealth"),
    url(r'^get_posts_MH', GetMHPosts.as_view(), name="get_posts_MH"),
    url(r'^get_MH_users', GetMHUsers.as_view(), name="get_MH_users"),
        
    url(r'^womenshealth$', Womenshealth.as_view(), name="womenshealth"),
    url(r'^get_posts_WH', GetWHPosts.as_view(), name="get_posts_WH"),
    url(r'^get_WH_users', GetWHUsers.as_view(), name="get_WH_users"),
        
    url(r'^organiclife$', Organiclife.as_view(), name="organiclife"),
    url(r'^get_posts_ROL', GetROLPosts.as_view(), name="get_posts_ROL"),
    url(r'^get_ROL_users', GetROLUsers.as_view(), name="get_ROL_users"),
        
    url(r'^rodalewellness$', Rodalewellness.as_view(), name="rodalewellness"),
    url(r'^get_posts_WE', GetWEPosts.as_view(), name="get_posts_WE"),
    url(r'^get_WE_users', GetWEUsers.as_view(), name="get_WE_users"),
    ]