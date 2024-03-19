
from django.contrib import admin
from django.urls import path

from company.views import homeView, listCompanyView, showCompanyView
from company.views import updateCompanyView, deleteCompanyView, createCompanyView


from job.views import listJobView, showJobView, createJobView
from job.views import updateJobView, deleteJobView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView),

    path('list-companies', listCompanyView),
    path('create-company', createCompanyView),
    path('show-company/<int:id>', showCompanyView),
    path('update-company/<int:id>', updateCompanyView),
    path('delete-company/<int:id>', deleteCompanyView),

    path('list-jobs', listJobView),
    path('create-job', createJobView),
    path('show-job/<int:id>', showJobView),
    path('update-job/<int:id>', updateJobView),
    path('delete-job/<int:id>', deleteJobView)
]
