from django.urls import path

from AppCoder.views import ProfesorCreateView, ProfesorDeleteView, ProfesorDetailView, ProfesorListView, ProfesorUpdateView, buscar, busqueda_camada, crear_curso, cursos, cursos_formulario, inicio, profesor_add, profesor_delete, profesor_update, profesores

urlpatterns = [
    path('crearcurso/<camada>', crear_curso),
    path('', inicio, name='inicio'),
    path('cursos', cursos, name='cursos'),
    path('cursosFormulario', cursos_formulario, name='cursos_formulario'),
    path('busquedaCamada', busqueda_camada, name='busqueda_camada'),
    path('buscar', buscar, name='buscar'),
    # path('profesores', profesores, name='profesores'),
    # path('profesores/add', profesor_add, name='profesor_add'),
    # path('profesores/delete/<id_profe>', profesor_delete, name='profesor_delete'),
    # path('profesores/update/<id_profe>', profesor_update, name='profesor_update'),
    path('profesores', ProfesorListView.as_view(), name='profesores'),
    path('profesores/add', ProfesorCreateView.as_view(), name='profesor_add'),
    path('profesores/update/<pk>', ProfesorUpdateView.as_view(), name='profesor_update'),
    path('profesores/delete/<pk>', ProfesorDeleteView.as_view(), name='profesor_delete'),
    path('profesores/view/<pk>', ProfesorDetailView.as_view(), name='profesor_view'),
]