from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F

from .models import Choice, Question
from .forms import *

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

class DetailView(generic.UpdateView):
    model = Question
    template_name = 'polls/detail.html'
    form_class = QuestionForm
    success_url = 'results/'     
           
    def form_valid(self, form):
        sch = form.cleaned_data['ch'].id
        Choice.objects.filter(pk=sch).update(votes=F('votes') + 1)
        return HttpResponseRedirect(reverse('polls:results', args=(self.object.id,)))
                
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



