from django.contrib import admin
from freelanceapp.models import Project, SkillSet

class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
					('Project Title', {'fields': ['name']}), 
					('Project Creator', {'fields': ['profile']}),
					('Currency', {'fields': ['budget_currency']}),
					('Project Goal', {'fields': ['budget']}),
					# ('Start date', {'fields': ['start_date']}),
					# ('End date', {'fields': ['end_date']}),
					('Description', {'fields': ['short_description']}),
					('Time frame', {'fields': ['time_frame']}),
					('Duration unit', {'fields': ['time_frame_unit']}),
					('Slug', {'fields': ['slug']}),
					('Skills', {'fields': ['skills']}),
			    ]

	list_display  = ('name', 'created', 'budget', 'slug')
	
class SkillSetAdmin(admin.ModelAdmin):
	fieldsets =[('Skill', {'fields': ['value']}),]
	list_display  = ('value', 'created')



admin.site.register(Project, ProjectAdmin)
admin.site.register(SkillSet, SkillSetAdmin)