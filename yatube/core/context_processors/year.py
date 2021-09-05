import datetime as dt


def year(request):
    year = dt.datetime.today().year
    context = {
        'year': year
    }
    return context
