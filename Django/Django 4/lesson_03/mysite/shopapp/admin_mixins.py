from django.db.models import QuerySet
from django.db.models.options import Options
from django.http import HttpRequest, HttpResponse
import csv


# класс и метод для скачивания файла CSV
class ExportAsCSVMixin:
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        meta: Options = self.model._meta  # берем мета модели, в мета доступны поля
        field_names = [field.name for field in meta.fields]  # список из строк как называются поля на этой модели

        response = HttpResponse(content_type='text/csv')  # подготавливаем объект в который будут выводится данные
        response['Content-Disposition'] = f'attachment; filename={meta}-export.csv'  #  для того чтобы можно было скачать файл

        csv_writer = csv.writer(response)  # записываем результат в ответ

        csv_writer.writerow(field_names)  # записали строчку с заголовками

        for obj in queryset: # записали строчки с данными
            csv_writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_csv.short_description = 'Export as CSV'  # описание метода
