from pyramid.view import notfound_view_config


@notfound_view_config(renderer='tutorial:templates/404.jinja2')
""" @notfound_view_config decorator registers a 'Not Found View'
    using 'pyramid.config.Configurator.add_notfound_view()'.
    
    renderer argument names an 'asset specification' of
    tutorial:templates/404.jinja2 """

def notfound_view(request):
    request.response.status = 404
    return {}
    """ set a 'view callable' named notfound_view. Sets an HTTP
        response status code '404'. The function returns an empty
        dict to the template:templates/404.jinja2, which accepts
        no parameters. """
