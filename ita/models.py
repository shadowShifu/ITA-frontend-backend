from django.db import models
from django.db.models.deletion import CASCADE

class Personal(models.Model):
    carnet_personal = models.CharField(max_length=20, primary_key=True)
    apellidoP_personal = models.CharField(max_length=30)
    apellidoM_personal = models.CharField(max_length=30)
    nombre_personal = models.CharField(max_length=30)    
    correo_personal = models.EmailField(max_length=100)
    usuario_personal = models.CharField(max_length=50)
    contra_personal = models.CharField(max_length=50)
    tipo_personal = models.CharField(max_length=20)
    estado = models.BooleanField(default=False)

class Docente(models.Model):
    carnet_docente = models.CharField(max_length=20, primary_key=True)
    apellidoP_docente = models.CharField(max_length=30)
    apellidoM_docente = models.CharField(max_length=30)
    nombre_docente = models.CharField(max_length=30)    
    correo_docente = models.EmailField(max_length=100)
    usuario_docente = models.CharField(max_length=50)
    contra_docente = models.CharField(max_length=50)
    sexo_docente = models.CharField(max_length=1)
    estado = models.BooleanField(default=False)

class Carrera(models.Model):
    id_carrera = models.CharField(max_length=20, primary_key=True)
    nombre_carrera = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=3)

class Curso(models.Model):
    id_curso = models.CharField(max_length=20, primary_key=True)
    nombre_curso = models.CharField(max_length=50)
    cantidad_estudiantes = models.IntegerField()
    gestion = models.PositiveIntegerField(default=1)
    pre_requisito = models.CharField(max_length=30)
    horas = models.PositiveIntegerField(default=2)
    id_carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    carnet_docente = models.ForeignKey(Docente, null=False, blank=False, on_delete=models.CASCADE)

class Estudiante(models.Model):
    carnet_est = models.CharField(max_length=20, primary_key=True)
    apellidoP_est = models.CharField(max_length=30)
    apellidoM_est = models.CharField(max_length=30)
    nombre_est = models.CharField(max_length=30) 
    fecha_nacimiento = models.DateField()   
    correo_est = models.EmailField(max_length=100)
    usuario_est = models.CharField(max_length=50)
    contra_est = models.CharField(max_length=50)
    sexo_est = models.CharField(max_length=1)
    vigencia = models.BooleanField(default=True)
    nuevo = models.BooleanField(default=True)
    turno = models.CharField(max_length=10)
    estado = models.BooleanField(default=False)
    id_carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)

class CursosEstudiante(models.Model):
    id = models.AutoField(primary_key=True)
    carnet_est = models.ForeignKey(Estudiante,null=False, blank=False, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    aprobado = models.BooleanField(default=False)

class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    carnet_est = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matriculacion = models.DateTimeField(auto_now_add=True)
    id_carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)


