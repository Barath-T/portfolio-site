from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project, Skill


class ProjectListView(ListView):

	context_object_name = 'project_list'

	template_name = 'portfolio/Project_list.html'

	queryset = Project.objects.all()

	def get_context_data(self, **kwargs):
		context = super(ProjectListView, self).get_context_data(**kwargs)
		context['skill_list'] = Skill.objects.all()

		return context



class ProjectDetailView(DetailView):

	template_name = 'portfolio/project_detail.html'

	queryset = Project.objects.all()



