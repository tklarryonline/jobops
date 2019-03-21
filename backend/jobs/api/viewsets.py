from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from jobs.api.serializers import CompanySerializer, JobSerializer
from jobs.models import Company, Job


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [AllowAny]


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.select_related('company').all().order_by('pk')
    permission_classes = [AllowAny]
