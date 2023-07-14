from django.urls import path
from . import views
from app.middlewares import firstmiddleware
urlpatterns = [
   path("",views.login,name="login"),
   path('project/', firstmiddleware(views.project), name='project'),
   path('dashboard/', firstmiddleware(views.dashboard), name='dashboard'), 
   path('success/', firstmiddleware(views.success), name='success'),
   path('logout/', views.logout, name='logout'),   
   path('delete/<int:project_id>/', views.delete, name='delete'), 
   path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
   path("round1/<int:project_id>/",views.round1,name="round1"),
   path("round2/<int:project_id>/",views.round2,name="round2"),
   path("round3/<int:project_id>/",views.round3,name="round3"),
]
