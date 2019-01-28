import json
import pprint

from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    context = {
        'additional_script': '',
        'css_class': 'class1'
    }
    if request.method == 'POST':
        context['css_class'] = request.POST.get('css_class', 'class1')
        context['additional_script'] = request.POST.get('additional_script', '')
    return render(request, template_name='picker.html', context=context)


def report_csp_violation(request):
    pprint.pprint(
        json.loads(request.body.decode('utf-8'))
    )
    return HttpResponse(status=200)
