from django.conf.urls import url
from online_test.views import test_paper, test_start, test_result


urlpatterns = [
    url(r'^test/(?P<test_paper_slug>[-\w]+)/$', test_paper, name='test_paper'),
    url(r'^test/(?P<test_paper_slug>[-\w]+)/start/$', test_start,
        name='test_start'),
    url(r'^test/(?P<test_paper_slug>[-\w]+)/result/$', test_result,
        name='test_result'),
]