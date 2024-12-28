from tasks.models import Tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("domain---", request.META.get('HTTP_HOST', ''))
        domain = request.META.get('HTTP_HOST', '').split(':')[0]
        print("after domain  :", domain)
        try:
            request.tenant = Tenant.objects.get(domain=domain)
        except Tenant.DoesNotExist:
            request.tenant = None
        return self.get_response(request)