from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        labels = {
            'name': _('ゲームタイトル'),
        }
        help_texts = {
            'name': _('必須: 最大256文字'),
        }
        error_messages = {
            'name': {
                'max_length': _('タイトル長すぎるでやんす'),
            }
        }
