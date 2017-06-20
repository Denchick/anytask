# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from schools.models import School


@login_required
def school_page(request, school_link):
    school = get_object_or_404(School, link=school_link)
    courses = school.courses.all().filter(is_active=True).order_by('name')

    context = {
        'school': school,
        'courses': courses,
    }

    return render_to_response('school_page.html', context, context_instance=RequestContext(request))


@login_required
def archive_page(request, school_link):
    school = get_object_or_404(School, link=school_link)
    courses = school.courses.all().filter(is_active=False).order_by('name')

    context = {
        'school': school,
        'courses': courses,
    }

    return render_to_response('archive_page.html', context, context_instance=RequestContext(request))
