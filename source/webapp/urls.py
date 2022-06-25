from django.urls import path

from webapp.views import AdListView, AdCreateView, AdView, AdDeleteView, AdUpdateView, AdReviewListView, AdApproveView

app_name = 'webapp'

urlpatterns = [
    path('', AdListView.as_view(), name="index"),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/', AdView.as_view(), name='ad_view'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name="ad_delete"),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('ad_review/', AdReviewListView.as_view(), name='ad_review_list'),
    path('<int:pk>/approve/', AdApproveView.as_view(), name='ad_approve_detail'),

]