from djangomako import shortcuts
from student import settings


def render_to_response(template_name, context):
    context['static'] = settings.STATIC_URL
    return shortcuts.render_to_response(template_name, context)
