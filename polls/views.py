from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # 获取问题对象
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。 这个例子中， request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。 request.POST 的值永远是字符串。
    except(KeyError,Choice.DoesNotExist):
        # 如果在 request.POST['choice'] 数据中没有提供 choice ， POST 将引发一个 KeyError 。上面的代码检查 KeyError ，如果没有给出 choice 将重新显示 Question 表单和一个错误信息。
        return render(request,'polls/detail.html',{'question':question,'error_message':"You didn`t select a choice.",})
        #   return render(request,'polls/detail.html',{
        #     'question': question,
        #     'error_message': "You didn't select a choice.",
        # })
        
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,) ) )

