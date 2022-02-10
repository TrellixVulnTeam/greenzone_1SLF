def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    """ call 'pyramid.config.Configurator.add_static_view()' with 3 arguements

        static: the name
        static: the path
        cache_max_age: a keyword arguement

        This registers a static resource which will match any URL that starts with
        prefix '/static' (by virtue of the first argument to 'add_static_view')
        This will serve up static resources for me from within the static dir of the
        tutorial package, in this case via 'http://localhost:6543/static/ and below.
        With this declaration, any URL that starts with /static should go to the 
        static view. below the /static path will be used to compose a path to the 
        static file resource, such a CSS file. """
    
    config.add_route('home', '/')
    """ This module registers a route configuration via the 
        'pyramid.config.configurator.add_route()' method that will
        be used when the URL is '/'. Since this route has a *pattern* 
        equaling '/', it is the route that will be matched when URL '/' 
        is visited, e.g. 'http://localhost:6543/' """
