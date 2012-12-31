from django.contrib import admin
from projects.models import Project, ProjectImage

class ProjectImageAdmin(admin.TabularInline):
	model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
	inlines = [
		ProjectImageAdmin,
	]
	exclude = ('description_html',)
	list_display = ('name', 'brief_description', 'priority')
	prepopulated_fields = { 'slug' : ('name',) }
	search_fields = ('name', 'description_text')
	
admin.site.register(Project, ProjectAdmin)