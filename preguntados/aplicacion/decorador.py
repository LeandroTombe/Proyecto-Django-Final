from django.http import HttpResponse




def allowed_user(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):

            group= None
            if request.user.groups.exists():
                group= request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('no tienes permiso para entrar a esta pagina, debes registrarte para poder acceder como usuario participante o loguearte')

                
                
        return wrapper_func
    return decorators
