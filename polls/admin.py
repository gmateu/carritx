from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
                ('Pregunta', {'fields':['question']}),
                ('Data',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    inlines = [ChoiceInline]
    
    
admin.site.register(Poll,PollAdmin)

