from django.contrib import admin
from freelanceapp.models import Project

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
			    ]

	list_display  = ('name', 'created', 'budget', 'slug')
	# inlines = [RewardInline]
	# inlines = [MilestoneInline]
	# inlines = [BankAccountInline]
	# list_display = ('name', 'goal', 'profile')
	# list_filter = ['approved', 'status', 'category', 'name', 'goal', 'profile']
	# search_fields = ['name','goal', 'duration', 'category']
	# date_hierarchy = 'start_date'
	




admin.site.register(Project, ProjectAdmin)