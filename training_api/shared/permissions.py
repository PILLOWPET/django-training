from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        print(request.user.is_staff)
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        print(request.user)
        return request.user.is_staff
