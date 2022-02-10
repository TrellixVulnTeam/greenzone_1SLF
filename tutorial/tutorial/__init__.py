from pyramid.config import Configurator
""" When I invoke the pserve development.ini command, 
    the main function above is executed. 
    It accepts some settings and returns a WSGI application. 
    __init__.py is returning this main function"""

def main(global_config, **settings):
""" This function returns a Pyramid WSGI application."""
    
    with Configurator(settings=settings) as config: # contruct a Configurator object using a context manager
    """ settings is passed to the Configurator as a keyword argument with the dict values
        passed as the **settings arguement. this will be a dict of settings parsed from the 
        .ini file, which contains deployment related values, such as pyramid.reload_templates, 
        sqlalchemy.url, so on. """
    
        config.include('pyramid_jinja2') # include jinja2 templating bindings
        config.include('.routes')        # include routes module using a dotted Python path
        config.include('.models')        # include models using a dotted Python path
        """ Pyramids 'pyramid.config.Configurator.include()' method is the primary mechanism for
            extending the configurator and breaking my code into feature-focused modules. """

        config.scan()
        """ main calls scan method of the configurator or 'pyramid.config.Configurator.scan()'
            which will recursively scan my tutorial package, looking for @view_config and other
            special decorators. when scan finds @view_config decorator, a view configuration 
            with be registered, allowing one of my app URLs to be mapped to code. """
        
    return config.make_wsgi_app()
    """ main finishes configuring 'pyramid.config.Configurator.make_wsgi_app()' method 
        returns a WSGI application. """
