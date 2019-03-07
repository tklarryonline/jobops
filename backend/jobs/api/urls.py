from rest_framework.routers import SimpleRouter

from jobs.api.viewsets import CompanyViewSet, JobViewSet

router = SimpleRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'jobs', JobViewSet)
