import autocomplete_light

autocomplete_light.autodiscover()

from models import *

class ClustrsSearchAutocomplete(autocomplete_light.AutocompleteModelBase):
    model = Clustr
    search_fields = ['name']
    attrs={'placeholder': 'search all clustrs'}

autocomplete_light.shortcuts.register(Clustr, ClustrsSearchAutocomplete)




