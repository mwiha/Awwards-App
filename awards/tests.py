from django.test import TestCase
from .models import Profile,Project,Voted 
from django.contrib.auth.models import User
# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.new_user = User(username='ray',email='myemail@gmail.com', password='123', first_name = 'Raymond',
        last_name='Ndegwa')
    def test_user_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

class TestProfile(TestCase):
    def setUp(self):
        self.new_user = User(username='ray',email='myemail@gmail.com', password='123', first_name = 'Raymond',
        last_name='Ndegwa')
        self.new_profile = Profile(profile_pic='avatar.png', bio="RRRR",user=self.new_user)

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_get_user_profile(self):
        self.new_profile.save()
        profile = Profile.get_user_profile(self.new_user)
        self.assertTrue(profile == self.new_profile)

class TestProject(TestCase):
    def setUp(self):
        self.new_user = User(username='ray',email='myemail@gmail.com', password='123', first_name = 'Raymond',
        last_name='Ndegwa')
        self.new_profile = Profile(profile_pic='avatar.png', bio="RRRR",user=self.new_user)
        self.new_project = Project(name='Pitches',description="Just an App", project_pic="pitches.png", 
        profile=self.new_profile)
    def test_project_instance(self):
        
        self.assertTrue(isinstance(self.new_project,Project))