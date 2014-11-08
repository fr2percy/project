#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

from rutas.log_admin import admin_log_addition, admin_log_change
from rutas.reportes import generar_pdf

from asociaciones.models import Asociacion
from asociaciones.form import AsociacionForm

@permission_required('asociaciones.add_asociacion', login_url='/login')
def index_asociacion(request):
    asociaciones = Asociacion.objects.all()
    return render(request, 'asociaciones/index.html',{
        'asociaciones':asociaciones,
    })

@permission_required('asociaciones.add_asociacion', login_url='/login')
def new_association(request):
    if request.method == 'POST':
        formulario = AsociacionForm(request.POST)
        if formulario.is_valid():
            a = formulario.save()
            u = User.objects.create_user(a.email, a.email, a.email)
            a.usuario = u
            a.save()
            admin_log_addition(request, a, 'Asociacion Creada')
            sms = "Asociacion <strong>%s</strong> Creada Corrctamente" %(a.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_asociacion))
    else:
        formulario = AsociacionForm()
    return render(request, 'asociaciones/new_association.html',{
        'formulario':formulario,
    })


@permission_required('asociaciones.change_asociacion', login_url='/login')
def list_association_update(request):
    associations = Asociacion.objects.all()
    return render(request, 'asociaciones/list_association_update.html',{
        'associations':associations,
    })

@permission_required('asociaciones.change_asociacion', login_url='/login')
def update_association(request, association_id):
    association = get_object_or_404(Asociacion, pk = association_id)
    if request.method == 'POST':
        formulario = AsociacionForm(request.POST, instance=association)
        if formulario.is_valid():
            a = formulario.save()
            admin_log_change(request, a, 'Asociacion Modificada')
            sms = "Asociacion <strong>%s</strong> Modificada Corrctamente" %(a.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(list_association_update))
    else:
        formulario = AsociacionForm(instance=association)
    return render(request, 'asociaciones/update_association.html',{
        'formulario':formulario,
    })

@permission_required('asociaciones.detail_asociacion', login_url='/login')
def list_detail_association(request):
    associations = Asociacion.objects.all()
    return render(request, 'asociaciones/list_detail_association.html',{
        'associations': associations,
    })


def mapa_association_ajax(request):
    if request.is_ajax():
        id_asso = int(request.GET['id'])
        association = get_object_or_404(Asociacion, pk = id_asso)
        html = render_to_string('asociaciones/ajax/mapa_asociacion.html',{
            'association':association,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@permission_required('asociaciones.mi_asociacion', login_url='/login')
def mi_association(request):
    asociacion = Asociacion.objects.get(usuario = request.user)
    return render(request, 'asociaciones/mi_association.html',{
        'asociacion':asociacion,
    })