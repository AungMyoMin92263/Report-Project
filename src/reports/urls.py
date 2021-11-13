from django.urls import path
from .views import (
    create_report_view,
    ReportListView,
    ReportDetailView,
    render_pdf_view,
    UploadTemplateView,
    csv_uploadview,
    )

app_names = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(),name='main'),
    path('save/', create_report_view, name='create-report'),
    path('from_file/', UploadTemplateView.as_view(), name='from-file'),
    path('upload/', csv_uploadview, name='upload-file'),
    path('<pk>', ReportDetailView.as_view(),name='detail'),
    path('<pk>/pdf/', render_pdf_view, name='pdf'),
]