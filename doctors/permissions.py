from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
         # Read permissions is allowed to any user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # But Write permission is only allowed to the user who has created these patient.
        return obj.user == request.user