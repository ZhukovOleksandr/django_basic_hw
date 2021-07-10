from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index page")


def articles(request):
    return HttpResponse("Articles page")


def archive(request, article_number=''):
    if not article_number:
        return HttpResponse("Archive page")
    else:
        return HttpResponse(f"This is archived article with number {article_number}")


def user(request, user_number=''):
    if user_number:
        return HttpResponse(f'This page of user {user_number}')
    else:
        return HttpResponse('Common users page')


def article(request, article_number, slug_text=''):
    if slug_text:
        return HttpResponse(f'This is a article with number {article_number} and slug - {slug_text}')
    else:
        return HttpResponse(f'This is a article with number {article_number} and no slug')


def some_id(request, my_slug, my_id=''):
    if my_id:
        return HttpResponse(f'{my_slug} and {my_id} ')
    else:
        return HttpResponse(f'{my_slug} and has no id')


def number_validator(request, numb):
    operator_code = ['050', '066', '096', '073', '067']

    if numb[:3] in operator_code:
        return HttpResponse(f'number {numb[:-1]} is valid')
    else:
        raise ValueError('Incorrect number')


def some_view(request, value):
    return HttpResponse(f'Great! {value}')