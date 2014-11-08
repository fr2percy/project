from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'users.views.home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #USUARIOS
    url(r'^login/$', 'users.views.iniciar_sesion'),
    url(r'^logout/$', 'users.views.cerrar_sesion'),
    url(r'^users/$', 'users.views.privado'),
    url(r'^users/new/$', 'users.views.new_user'),
    url(r'^users/edit/$', 'users.views.edit_perfil'),
    url(r'^users/reset/pass/$', 'users.views.cambiar_password'),

    url(r'^zona/calle/ajax/$', 'users.views.buscar_calle_ajax'),

    #ASOCIACIONES
    url(r'^association/$', 'asociaciones.views.index_asociacion'),
    url(r'^association/new/$', 'asociaciones.views.new_association'),
    url(r'^association/list/update/$', 'asociaciones.views.list_association_update'),
    url(r'^association/(?P<association_id>\d+)/update/$', 'asociaciones.views.update_association'),
    url(r'^association/list/detail/$', 'asociaciones.views.list_detail_association'),

    url(r'^association/my/$', 'asociaciones.views.mi_association'),

    url(r'^association/mapa/ajax/$', 'asociaciones.views.mapa_association_ajax'),

    #LINEAS
    url(r'^line/my/$', 'lineas.views.mis_lineas'),
    url(r'^line/my/add/$', 'lineas.views.add_mi_linea'),
    url(r'^line/select/position/$', 'lineas.views.select_linea_add'),
    url(r'^line/(?P<linea_id>\d+)/add/$', 'lineas.views.add_inicio'),
    url(r'^line/(?P<linea_id>\d+)/add/point/subida/$', 'lineas.views.add_point_subida'),
    url(r'^line/(?P<linea_id>\d+)/add/point/bajada/$', 'lineas.views.add_point_bajada'),
    url(r'^line/select/ruta/$', 'lineas.views.select_linea_ruta'),
    url(r'^line/(?P<linea_id>\d+)/view/ruta/$', 'lineas.views.ver_ruta_linea'),


    #ZONAS
    url(r'^zona/$', 'lineas.views.index_zona'),
    url(r'^zona/new/$', 'lineas.views.new_zona'),

    url(r'^zona/calles/ajax/$', 'lineas.views.calles_zona_ajax'),

    #BUSQUEDAS
    url(r'^zona/(?P<zona>\d+)/calle/(?P<calle>\d+)/$', 'users.views.zona_calle_lineas'),
    url(r'^ruta/linea/(?P<linea_id>\d+)/(?P<tramo>\d+)/$', 'users.views.ver_ruta_linea_tramo'),

    url(r'^search/$', 'users.views.zona_calle_lineas',{'zona': 'Villa Copacabana', 'calle':'San Alberto'}),


    url(r'^rutas/linea/(?P<tramo>\d+)/$', 'users.views.ruta_linea_ajax'),

    url(r'^zonas/all/$', 'users.views.zonas_ajax'),


)
