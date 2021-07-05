from django.contrib import admin
from django.urls import path, include
from ita import views
from rest_framework import routers

routerPersonal = routers.DefaultRouter()
routerPersonal.register(r'personales', views.PersonalView, 'personal')

routerDocente = routers.DefaultRouter()
routerDocente.register(r'docentes', views.DocenteView, 'docente')

routerCarrera = routers.DefaultRouter()
routerCarrera.register(r'carreras', views.CarreraView, 'carrera')

routerCurso = routers.DefaultRouter()
routerCurso.register(r'cursos', views.CursoView, 'curso')

routerEstudiante = routers.DefaultRouter()
routerEstudiante.register(r'estudiantes', views.EstudianteView, 'estudiante')

routerCursosEstudiante = routers.DefaultRouter()
routerCursosEstudiante.register(r'cursosEstudiante', views.CursosEstudianteView, 'cursosEstudiante')

routerMatricula = routers.DefaultRouter()
routerMatricula.register(r'matriculas', views.MatriculaView, 'matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routerPersonal.urls)),
    path('api/', include(routerDocente.urls)),
    path('api/', include(routerCarrera.urls)),
    path('api/', include(routerCurso.urls)),
    path('api/', include(routerEstudiante.urls)),
    path('api/', include(routerCursosEstudiante.urls)),
    path('api/', include(routerMatricula.urls)),
]
