from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'march': 'This is march',
    'april': 'This is april',
    'may': 'This is may',
    'june': 'This is june',
    'july': 'This is july',
    'august': 'This is august',
    'september': 'This is september',
    'october': 'This is october',
    'november': 'This is november',
    'december': 'This is december',
}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month_challenge', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('No such month')

    redirect_month = months[month - 1]
    redirect_path = reverse('month_challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string('challenges/challenge.html')
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported</h1>')
