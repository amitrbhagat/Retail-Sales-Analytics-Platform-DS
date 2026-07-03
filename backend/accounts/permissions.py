from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Admin").exists()
    

class IsManager(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Manager").exists()
    

class IsAnalyst(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Analyst").exists()    
    
   