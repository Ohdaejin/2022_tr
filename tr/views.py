from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm

def index(request):
    """
    tr 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'tr/question_list.html', context)

def detail(request, question_id):
    """
    tr 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render (request, 'tr/question_detail.html', context)

def answer_create(request, question_id):
    """
    tr 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('tr:detail', question_id=question.id)

def question_create(request):
    """
    tr 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('tr:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'tr/question_form.html', context)