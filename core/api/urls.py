from django.conf.urls import include, url
from tastypie.api import Api
from .student import StudentResource


v1_api = Api(api_name='v1')
v1_api.register(StudentResource())
#v1_api.register(EntryResource())
#student_resource = StudentResource()


urlpatterns = patterns('',
    (r'^', include(v1_api.urls)),
)
