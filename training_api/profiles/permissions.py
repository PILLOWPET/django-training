from rest_framework.permissions import BasePermission


class ownProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsValidAction(BasePermission):
    def has_permission(self, request, view):
        return view.action != "create"

    def has_object_permission(self, request, view, obj):
        allowed_actions = ["partial_update", "update"]
        return view.action in allowed_actions
