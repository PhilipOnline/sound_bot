from django.shortcuts import redirect

  #Require SSL com only. If we get anything else, redirect to https /
class RequireSSL:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        secure_list=['/auth/','/profile/']
        if not request.is_secure() and any(s in request.path_info for s in secure_list):
            return redirect('https:'+ request.get_host()+ request.path_info)
        elif request.is_secure() and any(s in request.path_info for s in secure_list):
            return redirect('http:'+ request.get_host()+ request.path_info)
        return response

