from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def main_page(request):

    return render(request, 'main_page.html')

def index(request):
    """
    tr 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'tr/question_list.html', context)

def detail(request, question_id):
    """
    tr 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render (request, 'tr/question_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    tr 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('tr:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'tr/question_detail.html', context)


@login_required(login_url='common:login')
def question_create(request):
    """
    tr 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('tr:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'tr/question_form.html', context)