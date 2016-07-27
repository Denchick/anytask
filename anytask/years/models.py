from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Year(models.Model):
    start_year = models.IntegerField(db_index=True, null=False, blank=False, unique=True)

    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return u"{0}-{1}".format(self.start_year, self.start_year + 1)

    def get_absolute_url(self):
        return reverse('courses.views.courses_list', args=[str(self.start_year)])
