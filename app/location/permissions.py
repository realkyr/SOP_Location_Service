from rest_framework.permissions import BasePermission, SAFE_METHODS
import requests

class DockterOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
        #     return True
        # if 'Authorization' in request.META.keys():
        #     info = requests.get('http://35.236.184.82:8888/api/v1.0/me', headers={'Authorization': request.META[]})
        # print(info.text)
        return request.method in SAFE_METHODS
