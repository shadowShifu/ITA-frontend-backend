from rest_framework import serializers
from .models import *

class PersonalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class DocenteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class CarreraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class EstudianteSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Estudiante
        fields = '__all__'

class CursosEstudianteSerializers(serializers.ModelSerializer):
    class Meta:
        model = CursosEstudiante
        fields = '__all__'

class MatriculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'