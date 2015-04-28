from mongoengine import *
from mongoengine.django.auth import User


class UserProfile(User):

    """Extend mongoengine User model"""

    USERNAME_FIELD = 'username'


class Teacher(UserProfile):
    """Extend User profile to create teacher"""

    qualification = StringField(max_length=50)
    subject = StringField(max_length=50)


class Student(UserProfile):
    """Extend User profile to create teacher"""

    birth_date = DateTimeField(required=True)
    student_class = StringField(required=True, max_length=50)
