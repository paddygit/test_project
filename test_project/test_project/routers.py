# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from online_test import views as online_test_views
from result import views as result_views

router = routers.DefaultRouter()

# Users Router
router.register(r'users', online_test_views.UserViewSet)

# Online Test Router
router.register(r'tests', online_test_views.TestViewSet)
router.register(r'question', online_test_views.QuestionViewSet)
router.register(r'multiplechoice', online_test_views.MultipleChoiceViewSet)

# Result Router
router.register(r'result', result_views.UserAnswersViewSet)
