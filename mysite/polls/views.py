from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last 5 published questions."""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# templates = loader.get_template('polls/index.html')
	# context = {
	#     'latest_question_list': latest_question_list,
	# }
	# return HttpResponse(template.render(context, request))
	# 使用render代替，可不使用loader和HttpResponse
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist.")
	# return render(request, 'polls/detail.html', {'question':question})
	# 使用get_object_or_404代替get() and Http404
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
		# request.POST['key']获取post提交的数据id，当不存在post数据时会抛出KeyError
	except (KeyError, Choice.DoesNotExist):
		return render(question, 'polls/detail.html', {
			    'question':question,
			    'error_message':"You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# 当成功post数据后需返回HttpResponseRedirect
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
		# reverse()转换url返回如‘/polls/question.id/results/’的url

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})
