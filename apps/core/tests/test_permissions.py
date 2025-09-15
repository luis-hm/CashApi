from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from unittest.mock import Mock
from apps.core.permissions import IsOwner

User = get_user_model()

class IsOwnerPermissionTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", email="user1@test.com")
        self.user2 = User.objects.create_user(username="user2", email="user2@test.com")
        self.permission = IsOwner()
        self.factory = APIRequestFactory()

    def test_owner_has_permission(self):
        request = self.factory.get("/")
        request.user = self.user1

        obj = Mock()
        obj.usuario = self.user1

        self.assertTrue(self.permission.has_object_permission(request, None, obj))

    def test_non_owner_has_no_permission(self):
        request = self.factory.get("/")
        request.user = self.user1

        obj = Mock()
        obj.usuario = self.user2

        self.assertFalse(self.permission.has_object_permission(request, None, obj))
