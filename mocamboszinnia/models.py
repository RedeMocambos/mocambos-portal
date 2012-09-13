from django.db import models
from zinnia.models import EntryAbstractClass, Entry

class EntryMocambosImage(models.Model):
    image = models.ImageField(upload_to='zinnia_images')
#    entry = models.ForeignKey(Entry, related_name='%(class)s_images')
    entry = models.ForeignKey(Entry)
