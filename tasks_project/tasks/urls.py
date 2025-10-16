from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView, mark_task_complete, mark_task_incomplete, UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', mark_task_complete, name='task-complete'),
    path('tasks/<int:pk>/incomplete/', mark_task_incomplete, name='task-incomplete'),
]
