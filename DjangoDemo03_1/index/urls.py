from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^10-queryall/$',views.queryall_views),
    url(r'^11-querybyid_1/(\d+)/$',views.querybyid_views),
    url(r'^12-delete/(\d+)/$',views.delete_views),
    url(r'^13-updateall/$',views.updateall_views),
]

urlpatterns += [
    url(r'^14-oto/$',views.oto_views),
    url(r'^15-otm/$',views.otm_views),
    url(r'^16-otm-exer/(\d*)$',views.otmexer_views),
]