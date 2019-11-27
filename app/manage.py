#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import py_eureka_client.eureka_client as eureka_client


def main():
    your_rest_server_port = 8000
    eureka_client.init(eureka_server="http://34.66.153.219:8761/eureka/",
                       app_name="LOCATION-SERVICE",
                       instance_port=your_rest_server_port,
                       instance_ip="35.225.198.249"
                       )
    # eureka_client.init_registry_client(eureka_server="http://34.66.153.219:8761/eureka/",
    #                                    app_name="LOCATION_SERVICE")
    # eureka_client.stop()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
