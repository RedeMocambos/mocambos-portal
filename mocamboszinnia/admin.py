from django.contrib import admin
from zinnia.models import Entry
from zinnia.admin.entry import EntryAdmin
from mocamboszinnia.models import EntryMocambosImage
from django.utils.translation import ugettext_lazy as _
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()


class EntryMocambosImageInline(admin.TabularInline):
    model = EntryMocambosImage
    extra = 3

class EntryMocambosAdmin(EntryAdmin):
    inlines = [ EntryMocambosImageInline, ]
    # In our case we put the gallery field
    # into the 'Content' fieldset
    fieldsets = ((_('Content'), {'fields': (
                    'title', 'content', 'image', 'status')}), ) + \
                    EntryAdmin.fieldsets[1:]
                    

admin.site.unregister(Entry)
admin.site.register(Entry, EntryMocambosAdmin)
