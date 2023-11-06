from django import template
from django.utils.safestring import mark_safe
from html.parser import HTMLParser

register = template.Library()

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = []

    def handle_data(self, d):
        self.text.append(d)

    def get_text(self):
        return ''.join(self.text)

@register.filter
def truncate_text(text, length):
    # Using HTMLStripper to extract text without HTML tags
    html_stripper = HTMLStripper()
    html_stripper.feed(text)
    text_without_tags = html_stripper.get_text()

    if len(text_without_tags) > length:
        truncated_text = text_without_tags[:length]
        return mark_safe(f'{truncated_text}...')
    return text
