# apps/comedor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('menu_del_dia/', views.menu_del_dia, name='menu_del_dia'),
    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    path('platillos/', views.listar_platillos, name='listar_platillos'),
    path('platillos/crear/', views.crear_platillo, name='crear_platillo'),
    path('platillos/editar/<int:id>/', views.editar_platillo, name='editar_platillo'),
    path('platillo/eliminar/<int:id>/', views.eliminar_platillo, name='eliminar_platillo'),

    path('menus/', views.listar_menus, name='listar_menus'),
    path('menu/crear/', views.crear_menu, name='crear_menu'),
    path('menu/editar/<int:id>/', views.editar_menu, name='editar_menu'),
    path('menu/eliminar/<int:id>/', views.eliminar_menu, name='eliminar_menu'),

    path('calificaciones/', views.listar_calificaciones, name='listar_calificaciones'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('calificaciones/editar/<int:id>/', views.editar_calificacion, name='editar_calificacion'),
    path('calificaciones/eliminar/<int:id>/', views.eliminar_calificacion, name='eliminar_calificacion'),

    path('comentarios/', views.listar_comentarios, name='listar_comentarios'),
    path('comentarios/crear/', views.crear_comentario, name='crear_comentario'),
    path('comentarios/editar/<int:id>/', views.editar_comentario, name='editar_comentario'),
    path('comentarios/eliminar/<int:id>/', views.eliminar_comentario, name='eliminar_comentario'),
]