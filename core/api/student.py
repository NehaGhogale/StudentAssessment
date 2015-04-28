# api/student.py
from tastypie import authorization
from tastypie_mongoengine import resources
from user.models import Student

class StudentResource(resources.MongoEngineResource):
    class Meta:
        queryset = Student.objects.all()
        allowed_methods = ('get', 'post', 'put', 'delete')
        authorization = authorization.Authorization()
