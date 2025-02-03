from django.db import models

class Modem(models.Model):

  mac_address = models.CharField(unique=True, max_length=17)
  created_ad = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.mac_address

#типы данных указывать лучше явно

class Sensor(models.Model):

  mac_address = models.CharField(max_length=17)
  vibration = models.IntegerField()
  temperature = models.IntegerField()
  modem_id = models.ForeignKey(Modem, on_delete=models.CASCADE, related_name='sensors')
  created_ad = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.mac_address

class Counter(models.Model):

  modem_id = models.ForeignKey(Modem, on_delete=models.CASCADE, related_name='counters')
  address = models.CharField(max_length=50)
  energy = models.FloatField()
  cos_fi_a = models.FloatField()
  cos_fi_b = models.FloatField()
  cos_fi_c = models.FloatField()
  cos_fi_common = models.FloatField()
  freq_a = models.FloatField()
  freq_b = models.FloatField()
  freq_c = models.FloatField()
  freq_common = models.FloatField()
  voltage_a = models.FloatField()
  voltage_b = models.FloatField()
  voltage_c = models.FloatField()
  voltage_common = models.FloatField()
  current_a = models.FloatField()
  current_b = models.FloatField()
  current_c = models.FloatField()
  current_common = models.FloatField()
  whole_power_a = models.IntegerField()
  whole_power_b = models.IntegerField()
  whole_power_c = models.IntegerField()
  active_power_a = models.IntegerField()
  active_power_b = models.IntegerField()
  active_power_c = models.IntegerField()
  reactive_power_a = models.IntegerField()
  reactive_power_b = models.IntegerField()
  reactive_power_c = models.IntegerField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.address
