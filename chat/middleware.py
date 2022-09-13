
from django.middleware.csrf import CsrfViewMiddleware
#--------function based middleware---------------
# def my_middleware(get_response):
#     print("one time initialzation bhadd")
#     def my_function(request):
#         print("this is before view")
#         response = get_response(request)
#         print("this is after view")
#         return response
#     return my_function

#---------------class based middleware-----------
class ClsMiddleware:
     def __init__(self, get_response):
      self.get_response = get_response
      print("one time initialization")#one time
     
     def __call__(self, request):
        print("this is before view")#before view call
        response = self.get_response(request)
        print("this is after view")
        return response

class Cls2Middleware:
     def __init__(self, get_response):
      self.get_response = get_response
      print("one time   cls2 initialization")#one time
     
     def __call__(self, request):
        print("this is before cls2 view")#before view call
        response = self.get_response(request)
        print("this is after cls2 view")
        return response

     
class Cls3Middleware:
     def __init__(self, get_response):
      self.get_response = get_response
      print("one time   cls3 initialization")#one time
     
     def __call__(self, request):
        print("this is before cls3 view")#before view call
        response = self.get_response(request)
        print("this is after cls3 view")
        return response



class CustomMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        csrf_skip_header = request.META.get('HTTP_SKIP_CSRF_CHECK')
        if csrf_skip_header:
                return None
        else:
            return super(CustomMiddleware, self).process_view(request, callback, callback_args, callback_kwargs)

