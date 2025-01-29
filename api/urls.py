from django.urls import path
from .views.modem import Modems
from .views.sensors import Sensors
from .views.counters import Counters
from .views.post import DataProcessing

urlpatterns = [
  path('all_modems/', Modems.as_view(), name='End point for reaching info about modems'),
  path("all_sensors/", Sensors.as_view(), name='End point for reaching info about sensors'),
  path("all_counters/", Counters.as_view(), name="End point for reaching info about counters"),
  path("add_or_update/", DataProcessing.as_view(), name="Add or update info")
]
