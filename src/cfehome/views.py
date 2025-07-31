from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit
this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "HomePage"
    my_context = {
        "page_title" : my_title,
        "total_visit_count" : qs.count(),
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100.0)/(qs.count()),
    }
    PageVisit.objects.create(path = request.path)

    html_template = "home.html"
    return render(request, html_template , my_context)




def home_old_page_view(request, *args, **kwargs):
    my_title = "Hey i am title from the old home page"
    my_context = {
        "page_title" : my_title
    }
    html_file_path = this_dir/ "home.html"
    # html_ = html_file_path.read_text()
    html_ = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{page_title} is something</h1>
</body>
</html>
'''.format(**my_context)
    return HttpResponse(html_)
