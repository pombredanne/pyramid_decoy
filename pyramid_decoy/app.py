# Copyright (c) 2014 by pyramid_decoy authors and contributors
# <see AUTHORS file>
#
# This module is part of pyramid_decoy and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT

from pyramid.config import Configurator


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""

    config = Configurator(settings=settings)
    return config.make_wsgi_app()
