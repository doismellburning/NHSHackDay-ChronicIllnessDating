import datetime
from haystack import indexes
from nhshd.models import Patient

class nhshd(indexes.SearchIndex, indexes.Indexable):
    text            = indexes.CharField(document=True, use_template=True)
    name            = indexes.CharField(model_attr='name')
    
    def get_model(self):
        return Patient

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()