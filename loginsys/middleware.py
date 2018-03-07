from django.shortcuts import redirect

  #Require SSL com only. If we get anything else, redirect to https /
class RequireSSL:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        host=request.get_host()
        url=request.build_absolute_uri().split(host)[-1]
        print(url)
        if not request.is_secure() and url=='/auth/login':
            return redirect('https://%s/auth/login' % request.get_host())
        return response

