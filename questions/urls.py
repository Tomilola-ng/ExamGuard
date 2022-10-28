from django.urls import path
from questions.views import QuestionCreateView, QuestionDetailView, QuestionListView


urlpatterns = [
    path('', QuestionListView.as_view() ,name='question_list'),
    path('ask/', QuestionCreateView.as_view() ,name='question_create'),
    path('<int:pk>/', QuestionDetailView ,name='question_detail'),
]
