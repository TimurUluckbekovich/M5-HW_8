from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Просмотр доступен всем. 
    Редактирование/удаление — только автору услуги или администратору.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff