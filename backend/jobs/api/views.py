from rest_framework.viewsets import ModelViewSet

from jobs.api.serializers import CompanySerializer, JobSerializer
from jobs.models import Company, Job


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
