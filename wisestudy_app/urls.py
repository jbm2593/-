from django.urls import path, include

from wisestudy_app.category import views as category_views #카테고리
# from wisestudy_app.user import views as user_views #유저
# from wisestudy_app.user_category import views as user_category_views #유저 카테고리
# from wisestudy_app.study import views as study_views #스터디
# from wisestudy_app.study_member import views as study_member_views #스터디원
# from wisestudy_app.activity_picture import views as activity_picture_views #활동사진
# from wisestudy_app.schedule import views as schedule_views #일정
#
# from wisestudy_app.accounts import views as accounts_views #카카오 소셜로그인
# from wisestudy_app.accounts.views import KakaoLogin as kakao_login

# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token


# app_name='accounts'

#카테고리
# category_patterns = [
#     path('', category_views),
    # path('/<int:id>', category_views.getCategory)
# ]


# #유저
# user_patterns = [
#     path('', user_views.getAllOrCreateUser),
#     path('/<int:id>', user_views.getUser)
# ]
#
# #유저 카테고리
# user_category_patterns = [
#     path('', user_category_views.getAllOrCreateUserCategory),
#     path('/<int:id>', user_category_views.getUserCategory)
# ]
#
# #스터디
# study_patterns = [
#     path('', study_views.getAllOrCreateStudy),
#     path('/<int:id>', study_views.getStudy)
# ]
#
# #스터디원
# study_member_patterns = [
#     path('', study_member_views.getAllOrCreateStudyMember),
#     path('/<int:id>', study_member_views.getStudyMember)
# ]
#
# #활동사진
# activity_picture_patterns = [
#     path('', activity_picture_views.getAllOrCreateActivityPicture),
#     path('/<int:id>', activity_picture_views.getActivityPicture)
# ]
#
# #일정
# schedule_patterns = [
#     path('', schedule_views.getAllOrCreateSchedule),
#     path('/<int:id>', schedule_views.getSchedule)
# ]


urlpatterns = [
    # path('', accounts_views.index, name="index"),
    # path('oauth', accounts_views.oauth, name='oauth'),
    # path('kakao_login', accounts_views.kakao_login, name='kakao_login'),
    # path('kakao_logout', accounts_views.kakao_logout, name='kakao_logout'),
    # path('rest-auth/kakao', kakao_login.as_view(), name='kakao_login2'),
    #
    # path('/category', include(category_patterns)),
    # path('/user', include(user_patterns)),
    # path('/user_category', include(user_category_patterns)),
    # path('/study', include(study_patterns)),
    # path('/study_member', include(study_member_patterns)),
    # path('/activity_picture', include(activity_picture_patterns)),
    # path('/schedule', include(schedule_patterns)),

    # path('api-jwt-auth/', obtain_jwt_token),
    # path('api-jwt-auth/refresh/', refresh_jwt_token),
    # path('api-jwt-auth/verify/', verify_jwt_token),
    # # path('/accounts/rest-auth/kakao/', verify_jwt_token),
    #
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    #
    # path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
]


