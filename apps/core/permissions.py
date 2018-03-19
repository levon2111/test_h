from rest_framework import permissions


class BasePermission(permissions.BasePermission):
    def _is_corporate(self, request):
        return request.user.is_authenticated() and request.user.auth_type == 'corporate'

    def _is_company(self, request):
        return request.user.is_authenticated() and request.user.auth_type == 'company'

    def _is_admin(self, request):
        return request.user.is_authenticated() and request.user.auth_type == 'admin'

    def _is_individual(self, request):
        return request.user.is_authenticated() and request.user.auth_type == 'individual'


class IsAdminOrSafeMethod(BasePermission):
    """
    Permission check for admin or access for safe methods
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated() and request.user.role == 'admin'


class IsAdmin(BasePermission):
    """
    Permission check for admin
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated() and request.user.role == 'admin'
