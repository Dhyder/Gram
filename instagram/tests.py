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

class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='Vickie', user=User(username='Calypso'))
        self.profile_test.save()

        self.image_test = Post(image='loop1.png', name='test', caption='default test', user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)