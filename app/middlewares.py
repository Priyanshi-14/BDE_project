from django.shortcuts import redirect

def firstmiddleware(get_response):
    def middleware(request):
        returnUrl = ''
        print(request.META['PATH_INFO'])
        if not request.session.get('user'):
            return redirect('login')
        response = get_response(request)
        return response
    return middleware
