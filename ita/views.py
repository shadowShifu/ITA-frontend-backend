from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class PersonalView(viewsets.ModelViewSet):
    serializer_class = PersonalSerializers
    
    def get_queryset(self):
        queryset = Personal.objects.all()
        usuario_personal = self.request.query_params.get('usuario_personal', None)
        contra_personal = self.request.query_params.get('contra_personal', None)
        if usuario_personal is not None and contra_personal is not None:
            queryset = queryset.filter(usuario_personal=usuario_personal, contra_personal=contra_personal)
        return queryset

class DocenteView(viewsets.ModelViewSet):
    serializer_class = DocenteSerializers

    def get_queryset(self):
        queryset = Docente.objects.all()
        usuario_docente = self.request.query_params.get('usuario_docente', None)
        contra_docente = self.request.query_params.get('contra_docente', None)
        if usuario_docente is not None and contra_docente is not None:
            queryset = queryset.filter(usuario_docente=usuario_docente, contra_docente=contra_docente)
        return queryset

class CarreraView(viewsets.ModelViewSet):
    serializer_class = CarreraSerializers
    queryset = Carrera.objects.all()

class CursoView(viewsets.ModelViewSet):
    serializer_class = CursoSerializers
    
    def get_queryset(self):
        queryset = Curso.objects.all()
        carrera = self.request.query_params.get('id_carrera', None)
        gestion = self.request.query_params.get('gestion', None)
        if gestion is not None and carrera is not None:
            queryset = queryset.filter(gestion=gestion, id_carrera=carrera)
        return queryset
        
class EstudianteView(viewsets.ModelViewSet):
    serializer_class = EstudianteSerializers
    
    def get_queryset(self):
        queryset = Estudiante.objects.all()
        usuario_est = self.request.query_params.get('usuario_est', None)
        contra_est = self.request.query_params.get('contra_est', None)
        if usuario_est is not None and contra_est is not None:
            queryset = queryset.filter(usuario_est=usuario_est, contra_est=contra_est)
        return queryset

class CursosEstudianteView(viewsets.ModelViewSet):
    serializer_class = CursosEstudianteSerializers
    
    def get_queryset(self):
        queryset = CursosEstudiante.objects.all()
        carnet_est = self.request.query_params.get('carnet_est', None)
        if carnet_est is not None:
            queryset = queryset.filter(carnet_est=carnet_est)
        return queryset

class MatriculaView(viewsets.ModelViewSet):
    serializer_class = MatriculaSerializers
    queryset = Matricula.objects.all()





