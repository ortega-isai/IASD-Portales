import csv
from django.http import HttpResponse
from django.contrib import admin

from .models import Oracion


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])

        return response


class OracionAdmin(admin.ModelAdmin, ExportCsvMixin):
    fields = ['fecha_hora', 'nombre', 'motivo']
    search_fields = ['fecha_hora', 'nombre']
    actions = ["export_as_csv"]


admin.site.register(Oracion, OracionAdmin)
