from rest_framework.permissions import BasePermission, SAFE_METHODS

class DealershipAPIPermission(BasePermission):
    """Basic permissions for the Dealership API"""

    def has_permission(self, request, view):
        """Create and List Read permissions"""
        if request.method != 'POST':
            return True
        else:
            return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """Detail object permissions"""
        #  Read permission
        if request.method in SAFE_METHODS:
            return True

        # Allow admins to work on this object
        user = request.user
        if request.user.is_superuser:
            return True

        # Allow web admins of this dealership to work on this object
        if obj.web_admin == user:
            return True

        return False
