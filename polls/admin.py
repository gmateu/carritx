from polls.models import Poll,Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
                ('Pregunta', {'fields':['question']}),
                ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
                ]
    inLines = [ChoiceInline]
admin.site.register(Poll,PollAdmin)

