from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from projects.models import Project, ProjectImage

def projects_index(request):
	projects = Project.objects.all()
	latest_project = Project.objects.latest()
	context = {
		'projects' : projects,
		'latest_project' : latest_project,
	}
	return render_to_response('projects/projects_index.html', context, RequestContext(request))

def project_detail(request, slug):
	project = get_object_or_404(Project.objects.filter(slug=slug))
	project_images = ProjectImage.objects.filter(project=project)
	context = {
		'project' : project,
		'project_images' : project_images,
	}
	return render_to_response('projects/project_detail.html', context, RequestContext(request))