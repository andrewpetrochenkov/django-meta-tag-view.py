__all__ = ['MetaTagMixin']

from django.utils.safestring import mark_safe


def gethtml(name, content):
    return """<meta name="%s" content="%s">""" % (name, content)


class MetaTagMixin:
    meta_tags = {}

    def get_meta_tags(self):
        return self.meta_tags

    def get_meta_tags_html(self):
        tags = []
        for name, content in self.get_meta_tags().items():
            if content:
                tags.append(gethtml(name, content))
        return mark_safe("\n".join(tags))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta_tags'] = self.get_meta_tags_html()
        return context
