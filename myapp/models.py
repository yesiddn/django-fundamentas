from django.db import models

# Create your models here.

"""
Cuando se usa (models.Model) significa que estas clases están heredando de models.Model, que es la clase base para todos los modelos en Django.

Cuando una clase hereda de models.Model:

Adquiere funcionalidad: La clase obtiene automáticamente métodos como save(), delete(), y objects (para realizar consultas).

Integración con la base de datos: Django puede mapear la clase a una tabla en la base de datos.

ORM (Object-Relational Mapping): Permite interactuar con la base de datos usando objetos Python en lugar de SQL directo.
"""
class Project(models.Model): # model.Model es la clase base de todos los modelos de Django que permite crear tablas en la base de datos.
  name = models.CharField(max_length=100)  # CharField es un campo de texto con una longitud máxima.
# 1, crear web

class Task(models.Model):
  title = models.CharField(max_length=200)  # Título de la tarea.
  description = models.TextField()  # Descripción de la tarea.
  project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Relación con el modelo Project.
# 1, instalar dependencias, instalar Django, 1 