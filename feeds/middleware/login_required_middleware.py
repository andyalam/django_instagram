from django.shortcuts import redirect

class FilterUnauthUsers(object):
    def process_request(self, request):
        allowed_paths = ['/login/', '/signup/', '/admin/', '/admin/login/']
        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect('login')
        return None
