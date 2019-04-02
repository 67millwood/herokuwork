from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	# output = ', '.join([q.question_text for q in latest_question_list])
	# return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	#try:
	question = get_object_or_404(Question, pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("🦂 Nada uno Question-eh 😬")
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	# return HttpResponse("🐋 You're voting on question %s." %question_id)
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def home(request):
	return HttpResponse("🐋 Welcome to the bus.")

