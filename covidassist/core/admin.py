from django.contrib import admin
from .models import Question, Answer, Datasourse
from import_export.admin import ImportExportModelAdmin


admin.site.register(Question)
admin.site.register(Answer)


@admin.register(Datasourse)
class DatasourseAdmin(ImportExportModelAdmin):
    pass
