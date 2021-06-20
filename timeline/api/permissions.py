from rest_framework import permissions


class isAdminOrReadOnly(permissions.BasePermission):
    """
    Everyone can read 
    Only admin or staff users change 
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.is_staff)


class isProfileOwnerOrReadonly(permissions.BasePermission):
    """
    Everyone can read 
    Only profile owner change 
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class isTimeLineMessageOwnerOrReadonly(permissions.BasePermission):
    """
    Everyone can read 
    Only Time line message owner change 
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.user == request.user
