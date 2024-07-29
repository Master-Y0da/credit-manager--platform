
from functools import wraps
from .middlewares import LoanManagerMiddleware

def custom_middleware(view_func):
    @wraps(view_func)
    def _wrapped_view(viewset,request, *args, **kwargs):
        print("custom_middleware", request.data)
        middleware = LoanManagerMiddleware(lambda req: view_func(viewset,req, *args, **kwargs))
        # Call the middleware with the request
        return middleware.process_view(request, view_func,*args,**kwargs) or middleware(request)
    return _wrapped_view
