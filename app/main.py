from app.wsgi import application
import py_eureka_client.eureka_client as eureka_client
# App Engine by default looks for a main.py file at the root of the app
# directory with a WSGI-compatible object called app.
# This file imports the WSGI-compatible object of the Django app,
# application from mysite/wsgi.py and renames it app so it is
# discoverable by App Engine without additional configuration.
# Alternatively, you can add a custom entrypoint field in your app.yaml:
# entrypoint: gunicorn -b :$PORT mysite.wsgi

# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
# eureka_client.init(eureka_server="http://34.66.153.219:8761/",
#                    app_name="LOCATION_SERVICE")
your_rest_server_port = 443
eureka_client.init(eureka_server="http://34.66.153.219:8761/eureka/",
                    app_name="LOCATION-SERVICE",
                    instance_port=your_rest_server_port)
# eureka_client.init_registry_client(eureka_server="http://34.66.153.219:8761/eureka/",
#                                    app_name="LOCATION_SERVICE")
# eureka_client.stop()
app = application
