from django.test import TestCase

from .models import Post, Profile
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Vickie')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='loop.jpg', bio='On Deck You Nitwits',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)