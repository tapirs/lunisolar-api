# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Moonshot
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
  """This Class defines the test cases for the moonshot model."""

  def setUp(self):
    """Define the test client and other test variables"""

    self.moonshot_name = "test event"
    user = User.objects.create_user("nerd")
    self.moonshot = Moonshot(name=self.moonshot_name, owner=user)

  def test_model_can_create_a_moonshot(self):
    """Test the moonshot model can create and event."""

    old_count = Moonshot.objects.count()
    self.moonshot.save()
    new_count = Moonshot.objects.count()
    self.assertNotEqual(old_count, new_count)	

class ViewTestCase(TestCase):
  """Test suite for the api views"""

  def setUp(self):
    """Define the test client and other test variables"""
    user = User.objects.create_user("nerd")

    self.client = APIClient()
    self.client.force_authenticate(user=user)

    self.moonshot_data = {'name': 'view test event', 'owner': user.get_username()}
    self.response = self.client.post(
      reverse('create'),
      self.moonshot_data,
      format="json")

  def test_api_can_create_a_moonshot(self):
    """Test the api can create a moonshot"""
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def test_authorization_is_enforced(self):
    """Test that the api has user authorization"""

    new_client = APIClient()
    response = new_client.get('/lunisolar/moonshot/', kwargs={'pk': 3}, format="json")
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_api_can_get_a_moonshot(self):
    """Test the api can get a moonshot"""
    moonshot = Moonshot.objects.get(id=1)
    response = self.client.get(
      reverse('details',
      kwargs={'pk': moonshot.id}),
      format="json")

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, moonshot)

  def test_api_can_update_a_moonshot(self):
    """Test the api can update a moonshot"""
    moonshot = Moonshot.objects.get()
    change_moonshot = {'name': 'updated event'}
    response = self.client.put(
      reverse('details', kwargs={'pk': moonshot.id}),
      change_moonshot, format="json")

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_api_can_delete_a_moonshot(self):
    """Test the api can delete a moonshot"""
    moonshot = Moonshot.objects.get()
    response = self.client.delete(
      reverse('details', kwargs={'pk': moonshot.id}),
      format="json",
      follow=True)

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
