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
from lineas.models import Linea, Posicion, Calle, Zona, Posicion_Calle
from lineas.form import LineaForm, MapaForm, CalleForm, ZonaForm

@permission_required('lineas.add_linea', login_url='/login')
def mis_lineas(request):
    asociacion = Asociacion.objects.get(usuario = request.user)
    lineas = Linea.objects.filter(asociacion = asociacion)
    return render(request, 'lineas/mis_lineas.html',{
        'lineas':lineas,
    })

@permission_required('lineas.add_linea', login_url='/login')
def add_mi_linea(request):
    asoci = Asociacion.objects.get(usuario = request.user)
    if request.method == 'POST':
        formulario = LineaForm(request.POST)
        if formulario.is_valid():
            l = formulario.save()
            l.asociacion = asoci
            l.save()
            admin_log_addition(request, l, 'Linea Creada')
            admin_log_change(request, asoci, 'Linea Creada')
            sms = "Linea <strong>%s</strong> Creada Correctamente"% (l.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(mis_lineas))
    else:
        formulario = LineaForm()
    return render(request, 'lineas/new_linea.html',{
        'formulario':formulario,
    })

def select_linea_add(request):
    lineas = Linea.objects.all()
    return render(request, 'lineas/select_linea_add_inicio.html',{
        'lineas':lineas
    })

def add_inicio(request, linea_id):
    linea = get_object_or_404(Linea, pk = linea_id)
    if request.method == 'POST':
        formulario = MapaForm(request.POST)
        if formulario.is_valid():
            po = formulario.save()
            po.linea = linea
            po.inicio = True
            po.save()
            sms = "Punto Inicial Creado Correctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(add_point, args=(linea.id,)))
    else:
        formulario = MapaForm()
    return render(request, 'lineas/posicion_inicial.html',{
        'formulario':formulario,
        'linea':linea,
    })


def add_point_subida(request, linea_id):
    linea = get_object_or_404(Linea, pk = linea_id)
    if Posicion.objects.filter(linea = linea, inicio = True, subida=True):
        inicio = Posicion.objects.get(linea = linea, inicio = True, subida=True)
    else:
        inicio = None
    if Posicion.objects.filter(linea = linea, fin = True, subida=True):
        fin = Posicion.objects.get(linea = linea, fin = True, subida=True)
    else:
        fin = None
    posiciones = Posicion.objects.filter(linea = linea, subida = True)
    if request.method == 'POST':
        formulario = MapaForm(request.POST)
        calleform = CalleForm(request.POST)
        if formulario.is_valid() and calleform.is_valid():
            position = formulario.save()
            position.linea = linea
            position.subida = True
            position.save()
            zona = calleform.cleaned_data['zona']
            calle = calleform.cleaned_data['nombre']
            z = Zona.objects.get(nombre = zona)
            if Calle.objects.filter(zona = z, nombre = calle):
                c = Calle.objects.get(zona = z, nombre = calle)
            else:
                c = Calle.objects.create(
                    zona = z,
                    nombre = calle,
                    )
            print c.id
            Posicion_Calle.objects.create(
                calle_id = c.id,
                posicion_id = position.id,
                )
            sms = "Punto Creado Correctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(add_point_subida, args=(linea.id,)))
    else:
        formulario = MapaForm()
        calleform = CalleForm()
    return render(request, 'lineas/add_point.html',{
        'linea':linea,
        'posiciones':posiciones,
        'formulario':formulario,
        'calleform':calleform,
        'inicio':inicio,
        'fin':fin,
    })

def add_point_bajada(request, linea_id):
    linea = get_object_or_404(Linea, pk = linea_id)
    if Posicion.objects.filter(linea = linea, inicio = True, bajada=True):
        inicio = Posicion.objects.get(linea = linea, inicio = True, bajada=True)
    else:
        inicio = None
    if Posicion.objects.filter(linea = linea, fin = True, bajada=True):
        fin = Posicion.objects.get(linea = linea, fin = True, bajada=True)
    else:
        fin = None
    posiciones = Posicion.objects.filter(linea = linea, bajada = True)
    if request.method == 'POST':
        formulario = MapaForm(request.POST)
        calleform = CalleForm(request.POST)
        if formulario.is_valid() and calleform.is_valid():
            position = formulario.save()
            position.linea = linea
            position.bajada = True
            position.save()
            zona = calleform.cleaned_data['zona']
            calle = calleform.cleaned_data['nombre']
            z = Zona.objects.get(nombre = zona)
            if Calle.objects.filter(zona = z, nombre = calle):
                c = Calle.objects.get(zona = z, nombre = calle)
            else:
                c = Calle.objects.create(
                    zona = z,
                    nombre = calle,
                    )
            print c.id
            Posicion_Calle.objects.create(
                calle_id = c.id,
                posicion_id = position.id,
                )
            sms = "Punto Creado Correctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(add_point_bajada, args=(linea.id,)))
    else:
        formulario = MapaForm()
        calleform = CalleForm()
    return render(request, 'lineas/add_point.html',{
        'linea':linea,
        'posiciones':posiciones,
        'formulario':formulario,
        'calleform':calleform,
        'inicio':inicio,
        'fin':fin,
    })

def calles_zona_ajax(request):
    if request.is_ajax():
        calles = list(Calle.objects.all().values('nombre'))
        print calles
        return JsonResponse(calles, safe = False)
    else:
        raise Http404


def select_linea_ruta(request):
    lineas = Linea.objects.all()
    return render(request, 'lineas/select_linea_ruta.html',{
        'lineas':lineas
    })

def ver_ruta_linea(request, linea_id):
    linea = get_object_or_404(Linea, pk = linea_id)
    posiciones = Posicion.objects.filter(linea = linea)
    posiciones1 = Posicion.objects.filter(linea = linea, inicio = False, fin = False)#.exclude(inicio = True, fin = True)
    return render(request, 'lineas/ruta_linea.html',{
        'linea':linea,
        'posiciones':posiciones,
        'posiciones1':posiciones1,
    })

@permission_required('lineas.add_zona', login_url='/login')
def index_zona(request):
    zonas = Zona.objects.all()
    return render(request, 'zonas/index.html',{
        'zonas':zonas,
    })

@permission_required('lineas.add_zona', login_url='/login')
def new_zona(request):
    if request.method == "POST":
        formulario = ZonaForm(request.POST)
        if formulario.is_valid():
            z = formulario.save()
            admin_log_addition(request, z, 'Zona Creada')
            sms = "Zona <strong>%s</strong> Creada Correctamente"% (z.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_zona))
    else:
        formulario = ZonaForm()
    return render(request, 'zonas/new_zona.html',{
        'formulario':formulario,
    })
