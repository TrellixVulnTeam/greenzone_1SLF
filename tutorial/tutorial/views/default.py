from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models

""" The main function of a webframe work is mapping each URL pattern to a 
    code (a view callable) that is executed when the requested URL matches
    the corresponding route. This application uses the 'pyramid.view.view_config()'
    decorator to perform this mapping. """

@view_config(route_name='home', renderer='tutorial:templates/mytemplate.jinja2')
""" This is the important part. The @view_config decorator associates the function
    with a 'view configuration, consisting of:
    a route_name == home
    a renderer == a template from /templates of the package 
    When a pattern associated with the home view is matched during a request, 
    'my_view()' will be excuted. 'my_view()' returns a dict; renderer will use
    'template/mytemplate.jinja2 to create a response based on values of the dict"""

""" The purpose of __init__.py executing 'pyramid.config.Configurator.scan()'
    method 'config.scan()' was to find and process @view_config decorator
    in order to creae a view configuration within my app. @view_config is inert
    without being detected by 'config.scan()' """

""" the sample 'my_view()' created by cookiecutter uses 'try:' and 'except:'
    clause to detect if there is a problem accessing the project database
    and provide an alternate error response. This alt text can be found as the
    output of 'db_err_msg' at the bottom of this file. """

def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'myproj'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
