from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from questions.models import Question , Answer
from questions.forms import AnswerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST

# Create your views here.
class QuestionListView(ListView):
    model = Question
    paginate_by = 10
    context_object_name = 'objects'


def QuestionDetailView(request, pk):
    if request.method == 'POST':
        question = get_object_or_404(Question, id = pk) 
        answer = None
        form = AnswerForm(data=request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.name = request.user.username
            answer.save()        

    question = get_object_or_404(Question, id = pk)
    answers = question.answer.all()
    form = AnswerForm()

    context = {
        'form': form,
        'answer': answers,
        'object': question
    }

    return render(request, 'questions/question_detail.html', context)

class QuestionCreateView(LoginRequiredMixin ,CreateView):
    model = Question

    fields = ['question']

    def form_valid(self, form):
        form.instance.asker = self.request.user
        return super().form_valid(form)