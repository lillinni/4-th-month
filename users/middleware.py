from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin

class SalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            level = request.POST.get("level")
            if level not in ["Junior", "Middle", "Senior"]:
                return HttpResponseBadRequest("Invalid qualification level.")
        return None
