from rest_framework.permissions import SAFE_METHODS, BasePermission


class ownPostChange(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user)
        print(obj.id)
        return False


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
