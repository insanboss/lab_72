from rest_framework import permissions


class QuotePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update']:
            return request.user.is_authenticated and request.user.has_perm('quote_app.change_quote')
        if view.action == "destroy":
            return request.user.is_authenticated and request.user.has_perm('quote_app.delete_quote')
        if view.action == 'retrieve':
            if obj.status == 'new':
                return request.user.is_authenticated and request.user.has_perm('quote_app.view_quote')
        return True
