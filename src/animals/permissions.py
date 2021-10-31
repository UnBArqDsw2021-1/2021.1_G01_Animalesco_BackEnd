from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from animals.models import Pet


class IsPetOwner(permissions.BasePermission):
    """
    Classe usada para verificar se o usuário logado é dono do pet que ele
    está tentando interagir.
    """

    message = (
        "Action rejected! To perform this action, the logged in user must own the Pet."
    )

    def has_permission(self, request, view):
        pet = get_object_or_404(Pet, pk=view.kwargs["pet_pk"])
        return pet.owner == request.user

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsRelatedPetOwner(permissions.BasePermission):

    message = (
        "Action rejected! To perform this action, the logged in user must own the Pet."
    )

    def has_permission(self, request, view):
        pet = get_object_or_404(Pet, pk=view.kwargs["pet_pk"])
        return pet.owner == request.user

    def has_object_permission(self, request, view, obj):
        return request.user == obj.pet.owner
