from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api.auth import CustomAuthToken #This path is for //3)Generate TOKEN by exposing an API endpoint//

#Creating Router Object
router=DefaultRouter()

#Register StudentViewSet with Router
router.register('stucreate', views.StudentModelViewSet, basename='student') #(IP/stucreste/) is our path to run this API
#We can write anything in the place of //student//, //router//, //stucreate//

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')), #For Login button in UI
    path('gettoken/', CustomAuthToken.as_view()), #This path is for //3)Generate TOKEN by exposing an API endpoint//
]