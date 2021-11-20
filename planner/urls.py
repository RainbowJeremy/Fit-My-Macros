from django.db import router
from rest_framework import routers, urlpatterns
from .views import  recipe_viewset

app_name = 'planner'


router = routers.SimpleRouter()
router.register('planner',recipe_viewset,basename = 'planner')


urlpatterns = router.urls

