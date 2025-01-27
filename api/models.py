from django.db import models

class Modem(models.Model):
  mac_address = models.CharField(unique=True, max_length=17)
  created_ad = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.mac_address

class Sensor(models.Model):
  mac_address = models.CharField(unique=True, max_length=17)
  vibration = models.JSONField()
  temperature = models.JSONField()
  modem_id = models.ForeignKey(Modem, on_delete=models.CASCADE, related_name='sensors')
  created_ad = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.mac_address

class Counter(models.Model):

  address = models.CharField(max_length=50)
  energy = models.JSONField()
  cos_fi_a = models.JSONField()
  cos_fi_b = models.JSONField()
  cos_fi_c = models.JSONField()
  cos_fi_common = models.JSONField()
  freq_a = models.JSONField()
  freq_b = models.JSONField()
  freq_c = models.JSONField()
  freq_common = models.JSONField()
  voltage_a = models.JSONField()
  voltage_b = models.JSONField()
  voltage_c = models.JSONField()
  voltage_common = models.JSONField()
  current_a = models.JSONField()
  current_b = models.JSONField()
  current_c = models.JSONField()
  current_common = models.JSONField()
  whole_power_a = models.JSONField()
  whole_power_b = models.JSONField()
  whole_power_c = models.JSONField()
  active_power_a = models.JSONField()
  active_power_b = models.JSONField()
  active_power_c = models.JSONField()
  reactive_power_a = models.JSONField()
  reactive_power_b = models.JSONField()
  reactive_power_c = models.JSONField()
  timestamp = models.JSONField()
  modem_id = models.ForeignKey(Modem, on_delete=models.CASCADE, related_name='counters')
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.address
