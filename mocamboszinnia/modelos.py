from django.db import models
from zinnia.models import EntryAbstractClass

class EntryMocambos(EntryAbstractClass):
    
    class Meta:
        abstract = True
        
      
    
# Vince_COMMENT: 
# Ver: http://stackoverflow.com/questions/8621937/inline-formset-for-creating-new-objects-with-one-to-many-relationship
# Ver: http://stackoverflow.com/questions/537593/multiple-images-per-model
