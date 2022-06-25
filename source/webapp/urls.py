from django.urls import path, include

from webapp.views.ad_views import AdListView, AdCreateView, AdView, AdDeleteView, AdUpdateView, AdReviewListView, AdApproveView
from webapp.views.api import set_status_accept, set_status_reject

app_name = 'webapp'

api_urlpatterns = [
    path("accept/ad/", set_status_accept),
    path("reject/ad/", set_status_reject),
]

urlpatterns = [
    path('', AdListView.as_view(), name="index"),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/', AdView.as_view(), name='ad_view'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name="ad_delete"),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('ad_review/', AdReviewListView.as_view(), name='ad_review_list'),
    path('<int:pk>/approve/', AdApproveView.as_view(), name='ad_approve_detail'),
    path("api/", include(api_urlpatterns))
]