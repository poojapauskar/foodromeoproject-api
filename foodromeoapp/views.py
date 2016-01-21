# from django.shortcuts import render_to_response
# from django.template.context import RequestContext
# from django.template import loader

# def home(request):
#    context = RequestContext(request,
#                            {'user': request.user})
#    # template = loader.get_template('foodromeoapp/home.html')
#    return render_to_response('foodromeoapp/home.html',
#                              context_instance=context)

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('foodromeoapp/home.html',
                             context_instance=context)