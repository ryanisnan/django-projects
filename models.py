from django.db import models
from django.db.models import permalink

import os.path

# Import django-tagging
from tagging.fields import TagField

# Method for fetching the dynamic upload path of images
def get_image_upload_path(instance, filename):
	return os.path.join('apps/projects', instance.slug, filename)
	
# Method for fetching the dynamic upload path of a project's images
def get_project_image_upload_path(instance, filename):
	return os.path.join('apps/projects', instance.project.slug, filename)

class ProjectManager(models.Manager):
	def latest(self):
		return self.get_query_set()[:1][0]

class Project(models.Model):	
	name = models.CharField(max_length=64, blank=False)
	slug = models.SlugField()
	priority = models.SmallIntegerField(default=0, help_text='Priority of this project compared to other projects.')
	brief_description = models.CharField(max_length=128, blank=False)
	description_text = models.TextField()
	description_html = models.TextField(blank=True)
	project_url = models.URLField(blank=True, help_text='If the project is on the web, enter the URL here.')
	preview_image = models.ImageField(blank=True, upload_to=get_image_upload_path)
	tags = TagField()
	
	objects = ProjectManager()
	
	class Meta:
		ordering = ('-priority',)
		
	def __unicode__(self):
		return self.name
	
	def save(self, force_insert=False, force_update=False):
		from markdown import markdown
		from smartypants import smartyPants
		self.description_html = markdown(self.description_text, output_format='html4')
		super(Project, self).save(force_insert, force_update)
	
	@permalink
	def get_absolute_url(self):
		from projects.views import project_detail
		return (project_detail, (self.slug,))

class ProjectImage(models.Model):
	project = models.ForeignKey('Project')
	image = models.ImageField(upload_to=get_project_image_upload_path)