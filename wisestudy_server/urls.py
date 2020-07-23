from django.contrib import admin
from django.urls import path, include

# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token
# from wisestudy_app.accounts import views as accounts_views #카카오 소셜로그인

from rest_framework import routers
from wisestudy_app.category.views import CategoryViewSet
from django.conf.urls import url

from wisestudy_server.yasg import schema_view

router = routers.DefaultRouter(trailing_slash=False)
router.register('categories', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # path('api/v1', include('wisestudy_app.urls'))
    # path('admin', admin.site.urls),
    # path('', include('wisestudy_app.urls')),
    # path('api/v1', include('wisestudy_app.urls')),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    #
    # path('accounts', include('wisestudy_app.urls', namespace='accounts')),
    #
    # path('api-jwt-auth', obtain_jwt_token),
    # path('api-jwt-auth/refresh', refresh_jwt_token),
    # path('api-jwt-auth/verify', verify_jwt_token),
    #
    # path('rest-auth', include('rest_auth.urls')),
    # path('rest-auth/registration', include('rest_auth.registration.urls')),

    # API 문서 자동화 UI
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]