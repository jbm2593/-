from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_url_v1_patterns = [
    path('boards', include('wisestudy_app.urls'))
]

schema_view = get_schema_view(
    openapi.Info(
        title="WiseStudy Open API",
        default_version='v1',
        description=
        """
        WiseStudy Open API 문서 페이지

        스터디 앱을 만들라고합니다

        팀원:SCH
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="WiseStudy"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
    # patterns=schema_url_v1_patterns,
)
