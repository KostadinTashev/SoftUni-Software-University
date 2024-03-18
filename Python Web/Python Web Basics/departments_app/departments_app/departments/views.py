from random import choice

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect


# Without render
def show_departments(request: HttpRequest, *args, **kwargs):
    context = {
        'page_title': 'Departments',
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name'),
    }
    return render(request, 'departments/all.html', context)


def show_department_details(request: HttpRequest, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def redirect_to_fist_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    # to = 'https://softuni.bg'
    # to = f'/departments/?order_by={order_by}'
    return redirect('show departments details', department_id=13,
                    )


def show_not_found(request):
    status_code = 404
    # print('With response')
    # return HttpResponseNotFound('This not found')
    # return HttpResponse('Error', status=status_code)
    # raise Http404('Not found!')
