from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    data = []
    with open(settings.DATA_FILE, encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for line in csv_reader:
            data.append(dict(line))
    context = {'inflation_list': data}

    return render(request, template_name,
                  context)