from __future__ import unicode_literals
from django.template.loader import get_template
from ..template import Library
from ..utils import get_copy_dict


register = Library()


@register.to_end_tag
def editable(parsed, context, token, *args, **kwargs):

    request = context['request']
    user = request.user
    skip_cache = user.has_perm('templatecms.Copy')
    copy_dict = get_copy_dict(skip_cache=skip_cache)
    fields = token.split_contents()[1:]
    has_permission = user.has_perm('templatecms.Copy')
    lookup_key = fields[0]

    if not has_permission:
        return parsed

    fields = token.split_contents()[1:]

    try:
        editable_type = fields[1]
    except IndexError:
        editable_type = "copy"

    t = get_template("templatecms/includes/editable_form.html")
    context["editable_type"] = editable_type
    context["parsed"] = parsed
    context["lookup_key"] = lookup_key
    context["copy_value"] = copy_dict.get(lookup_key, "")
    return t.render(context)

    return parsed


@register.to_end_tag
def initial_value(parsed, context, token):

    skip_cache = context['user'].has_perm('templatecms.Copy')
    copy_dict = get_copy_dict(skip_cache=skip_cache)

    # get lookup key
    fields = token.split_contents()[1:]
    lookup_key = fields[0]

    # get dictionary value
    output_value = copy_dict.get(lookup_key, parsed)

    return output_value
