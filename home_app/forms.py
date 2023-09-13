from django.forms import *
from .models import *


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                # 'class': 'form-control',
                'placeholder': field_name
            })
