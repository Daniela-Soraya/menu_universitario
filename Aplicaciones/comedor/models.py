from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    carrera = models.CharField(max_length=100)
    preferencias_alimenticias = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)  # Ejemplo: entrada, principal, postre
    calorias = models.IntegerField()
    proteinas = models.DecimalField(max_digits=5, decimal_places=2)
    carbohidratos = models.DecimalField(max_digits=5, decimal_places=2)
    grasas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    fecha = models.DateField()
    platillos = models.ManyToManyField(Platillo)

    def __str__(self):
        return f"Menú {self.fecha}"

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()  # Ejemplo: de 1 a 5
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.estudiante} - {self.platillo}"

class Comentario(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f"Comentario de {self.estudiante}"
