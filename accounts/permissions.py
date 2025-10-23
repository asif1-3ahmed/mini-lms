from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsInstructorOrAdminOrReadOnly(BasePermission):
    """
    Custom permission:
    - Students can only view (GET, HEAD, OPTIONS)
    - Instructors/Admins can create, update, or delete
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Everyone can read
        return (
            request.user.is_authenticated and
            request.user.role in ['admin', 'instructor']
        )
