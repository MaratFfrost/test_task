from django.urls import path
from .views.modem import Modems
from .views.sensors import Sensors
from .views.counters import Counters
from .views.post import DataProcessing

urlpatterns = [
  path('all_modems/', Modems.as_view(), name='all modems'),
  path("all_sensors/", Sensors.as_view(), name='all sensors'),
  path("all_counters/", Counters.as_view(), name="all counters"),
  path("add_or_update/", DataProcessing.as_view(), name="Add or update info")
]
