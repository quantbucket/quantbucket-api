from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
import users.views
import algorithms.views
import analysis.views
import datasets.views
import visualizations.views

router = routers.DefaultRouter()
router.register(r'users', users.views.UserViewSet)
router.register(r'algorithms', algorithms.views.AlgorithmViewSet)
router.register(r'analysis', analysis.views.AnalysisViewSet)
router.register(r'datasets', datasets.views.DatasetViewSet)
router.register(r'visualizations', visualizations.views.VisualizationViewSet)
router.register(r'mappings', visualizations.views.VisualizationMappingViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^admin/', include(admin.site.urls)),
]
