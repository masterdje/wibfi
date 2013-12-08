# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386448749.254984
_enable_loop = True
_template_filename = u'themes/custom/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace(u'phelper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'phelper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        phelper = _mako_get_namespace(context, 'phelper')
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 35
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        phelper = _mako_get_namespace(context, 'phelper')
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        for post in posts:
            # SOURCE LINE 8
            __M_writer(u'        <div class="postbox">\n\t\t\t<div class="media">\n\t\t\t\t<a class="pull-left" href="')
            # SOURCE LINE 10
            __M_writer(unicode(post.permalink()))
            __M_writer(u'">\n\t\t\t\t\t')
            # SOURCE LINE 11
            __M_writer(unicode(phelper.html_theme(post)))
            __M_writer(u'\n\t\t\t\t</a>\n\t\t\t\t<div class="media-body">\n\t\t\t \n\t\t\t\t\t<div class="panel panel-primary">\n\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t<h3 class="panel-title"><a href="')
            # SOURCE LINE 17
            __M_writer(unicode(post.permalink()))
            __M_writer(u'">')
            __M_writer(unicode(post.title()))
            __M_writer(u'</a>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="panel-body">')
            # SOURCE LINE 19
            __M_writer(unicode(phelper.html_tags(post)))
            __M_writer(u'\n\t\t\t\t\t\t\t<small><time class="published" datetime="')
            # SOURCE LINE 20
            __M_writer(unicode(post.date.isoformat()))
            __M_writer(u'">')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'</time></small>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\t\t\n\t\t\t\t</div>\n\t\t\t</div>\t\t\n        ')
            # SOURCE LINE 25
            __M_writer(unicode(post.text(teaser_only=index_teasers)))
            __M_writer(u'\n')
            # SOURCE LINE 26
            if not post.meta('nocomments'):
                # SOURCE LINE 27
                __M_writer(u'            ')
                __M_writer(unicode(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer(u'\n')
            # SOURCE LINE 29
            __M_writer(u'        </div>\n')
        # SOURCE LINE 31
        __M_writer(u'    ')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n    ')
        # SOURCE LINE 32
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n\t')
        # SOURCE LINE 33
        __M_writer(unicode(helper.mathjax_script(posts)))
        __M_writer(u'\n\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


