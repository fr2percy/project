#encoding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_unicode
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.contrib import messages

from users.form import EmailForm, PerfilForm

from lineas.models import Zona, Calle, Posicion_Calle, Posicion, Linea

def home(request):
    zonas = Zona.objects.all()
    return render(request,'base.html',{
        'zonas':zonas,
        })

def buscar_calle_ajax(request):
    if request.is_ajax():
        nombre = request.GET['nombre'];
        calles = Calle.objects.filter(zona__nombre = nombre)
        #tipos = Tipo.objects.filter(categoria__nombre = nombre)
        html = render_to_string('users/ajax/calles_zona_ajax.html',{
            'calles':calles,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404

def zona_calle_lineas(request, zona, calle):
    zonas = Zona.objects.all()
    z = get_object_or_404(Zona, pk = zona)
    calle = get_object_or_404(Calle, pk = calle)
    c_p = Posicion_Calle.objects.filter(calle = calle)
    p = Posicion.objects.filter(id__in = c_p.values('posicion_id'))
    lineas = Linea.objects.filter(id__in = p.values('linea_id'))
    return render(request, 'busquedas/zonas_calle_lineas.html',{
        'lineas':lineas,
        'calle':calle,
        'zonas':zonas,
    })

def ver_ruta_linea_tramo(request, linea_id, tramo):
    linea = Linea.objects.get(id = linea_id)
    if int(tramo) == 1:
        posiciones = Posicion.objects.filter(linea = linea, subida = True)
        posiciones1 = Posicion.objects.filter(linea = linea, inicio = False, fin = False, subida = True)
        tramo = 'Subida'
    else:
        posiciones = Posicion.objects.filter(linea = linea, bajada = True)
        posiciones1 = Posicion.objects.filter(linea = linea, inicio = False, fin = False, bajada = True)
        tramo = 'Bajada'
    zonas = Zona.objects.all()
    return render(request, 'busquedas/ruta_linea_tramo.html',{
        'posiciones':posiciones,
        'posiciones1':posiciones1,
        'linea':linea,
        'tramo':tramo,
        'zonas':zonas,
    })




def zonas_ajax(request):
    if request.is_ajax():
        zonas = Zona.objects.all()
        html = render_to_string('zonas_ajax.html', {
            'zonas':zonas
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404


def ruta_linea_ajax(request, tramo):
    if request.is_ajax():
        linea_id = int(request.GET['id'])
        linea = Linea.objects.get(id = linea_id)
        if int(tramo) == 1:
            posiciones = Posicion.objects.filter(linea = linea, subida = True)
            posiciones1 = Posicion.objects.filter(linea = linea, inicio = False, fin = False, subida = True)
            tramo = 'Subida'
        else:
            posiciones = Posicion.objects.filter(linea = linea, bajada = True)
            posiciones1 = Posicion.objects.filter(linea = linea, inicio = False, fin = False, bajada = True)
            tramo = 'Bajada'

        html = render_to_string('busquedas/ajax/ruta_linea.html',{
            'posiciones':posiciones,
            'posiciones1':posiciones1,
            'linea':linea,
            'tramo':tramo,
        }, context_instance=RequestContext(request))
        return JsonResponse(html, safe=False)
    else:
        raise Http404
        
        
        
def new_user(request):
    if request.method == 'POST':
        formuser = UserCreationForm(request.POST)
        formemail = EmailForm(request.POST)
        if formemail.is_valid() and formuser.is_valid() :
            u = formuser.save()
            u.email = formemail.cleaned_data['email']
            u.save()

            msm = "Su Cuenta fue creada Correctamente"
            messages.add_message(request, messages.INFO, msm)
            return HttpResponseRedirect('/')
    else:
        formuser = UserCreationForm()
        formemail = EmailForm()
    zonas = Zona.objects.all()
    return render(request, 'users/new_user.html', {
        'formuser':formuser,
        'formemail':formemail,
        'zonas':zonas,
    })


def iniciar_sesion(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(privado))
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    sms = 'Sesión Iniciada Correctamente'
                    messages.success(request, sms, )
                    if 'next' in request.GET:
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        return HttpResponseRedirect(reverse(privado))
                else:
                    sms = 'Su Cuenta de Usuario No Esta Activada'
                    messages.warning(request, sms,)
                    return HttpResponseRedirect(reverse(iniciar_sesion))
            else:
                sms = 'Usted No Es Usuario Registrado'
                #messages.warning(request, sms,)
                messages.error(request, sms, 'danger')
                #messages.info(request, sms, )
                #messages.success(request, sms, )
                return HttpResponseRedirect(reverse(iniciar_sesion))
    else:
        formulario = AuthenticationForm()
    zonas = Zona.objects.all()
    return render(request, 'users/login.html', {
        'formulario':formulario,
        'zonas':zonas,
    })

@login_required(login_url='/login')
def cerrar_sesion(request):
    logout(request)
    sms = 'Sesión Terminada Correctamente'
    messages.add_message(request, messages.INFO, sms)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def edit_perfil(request):
    if request.method == 'POST':
        formulario = PerfilForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            sms = "Perfil Completado Corrctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(privado))
    else:
        formulario = PerfilForm(instance=request.user)
    return render(request, 'users/edit_perfil.html',{
        'formulario':formulario,
    })

@login_required(login_url='/login')
def privado(request):
    #empleado = Empleado.objects.get(usuario = request.user)
    return render(request, 'users/index.html', {
        #'empleado':empleado,
    })

@login_required(login_url='/login')
def cambiar_password(request):
    if request.method == 'POST' :
        formulario = AdminPasswordChangeForm(user=request.user, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse(iniciar_sesion))
    else:
        formulario = AdminPasswordChangeForm(user=request.user)
    return  render(request, 'users/reset_pass.html', {
        'formulario' :formulario,
        })


