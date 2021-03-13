"""raptor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework import routers

from billings.views import ClaimViewSet, ClaimPaidViewSet
from patients.views import PatientsViewSet
from doctors.urls import ProviderNumberViewSet
from medications.views import AllergiesViewSet, MedicationsViewSet
from comorbidities.views import ComorbiditiesViewSet
from tasks.views import TasksViewSet
from consultations.views import ConsultationsViewSet, IssuesViewSet, LettersViewSet, InvestigationsViewSet
from socialhx.views import SocialHxViewSet
from templates.views import InvestigationsViewSet as TemplateInvestigationsViewSet, IssuesViewSet as TemplateIssuesViewSet
from diagnoses.views import DiagnosesViewSet

def response_notfound_handler(request, exception=None):
    return HttpResponse('<h1>Not found</h1>',status=404)


handler404 =  response_notfound_handler


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'patients', PatientsViewSet)
router.register(r'billings/claims', ClaimViewSet)
router.register(r'billings/claimspaid', ClaimPaidViewSet)
router.register(r'providernumbers', ProviderNumberViewSet)
router.register(r'allergies', AllergiesViewSet)
router.register(r'medications', MedicationsViewSet)
router.register(r'comorbidities',ComorbiditiesViewSet)
router.register(r'tasks',TasksViewSet)
router.register(r'consultations',ConsultationsViewSet)
router.register(r'issues',IssuesViewSet)
router.register(r'socialhx',SocialHxViewSet)
router.register(r'letters',LettersViewSet)
router.register(r'diagnoses', DiagnosesViewSet)
router.register(r'investigations', InvestigationsViewSet)
router.register(r'templates/issues',TemplateIssuesViewSet)
router.register(r'templates/investigations',TemplateInvestigationsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
