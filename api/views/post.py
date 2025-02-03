import datetime
import re
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Counter, Modem, Sensor

class DataProcessing(APIView):

    @staticmethod
    def is_valid_mac(mac: str) -> bool:
        if mac is None:
            return False
        mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
        return bool(mac_regex.match(mac))

    @staticmethod
    def is_valid_counter(counter: dict) -> bool:
        if type(counter.get("address")) is not str:
            raise ValueError("Адрес должен быть строкой или адреса нет")

        keys = [
            "energy", "cos_fi_a", "cos_fi_b", "cos_fi_c", "cos_fi_common",
            "freq_a", "freq_b", "freq_c", "freq_common",
            "voltage_a", "voltage_b", "voltage_c", "voltage_common",
            "current_a", "current_b", "current_c", "current_common",
            "whole_power_a", "whole_power_b", "whole_power_c",
            "active_power_a", "active_power_b", "active_power_c",
            "reactive_power_a", "reactive_power_b", "reactive_power_c"
        ]

        for key in keys:
            if key not in counter or not isinstance(counter[key], list):
                return False
            if not all(isinstance(element, (int, float)) for element in counter[key]):
                return False

        return True

    @staticmethod
    def is_all_times_valid(times: list) -> bool:
        def is_valid_time_format(time_str):
            try:
                datetime.datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')
                return True
            except ValueError:
                return False

        return all(is_valid_time_format(time) for time in times)

    @staticmethod
    def is_valid_sensors(sens_info: dict) -> bool:
        necessary_params = ("vibrations", "name", "temperature")
        max_index = len(sens_info) // 3
        seen_indices = set()

        if len(sens_info) % 3 != 0:
            raise ValueError("Некорректные данные датчиков")

        for key, value in sens_info.items():
            if not any(key.startswith(prefix) for prefix in necessary_params):
                return False

            try:
                index = int(re.search(r'\d+$', key).group())
                if index < 1 or index > max_index:
                    return False
                if (key[:-len(str(index))], index) in seen_indices:
                    return False
                seen_indices.add((key[:-len(str(index))], index))
            except ValueError:
                return False

            if key.startswith("name"):
                if not isinstance(value, str):
                    return False
            else:
                if not isinstance(value, (list, tuple)):
                    return False
                if not all(isinstance(item, (int, float)) for item in value):
                    return False

        return True

    def post(self, request):
        try:
            data = request.data

            keys_to_keep = ("name", "vibrations", "temperature")
            filt_data = {k: v for k, v in data.items() if k.startswith(keys_to_keep)}

            if not self.is_valid_mac(data.get("mac")):
                raise ValueError("Некорректный MAC-адрес")

            if "counters" not in data or not isinstance(data["counters"], list):
                raise ValueError("Некорректные данные счетчиков")
            for counter in data["counters"]:
                if not self.is_valid_counter(counter):
                    raise ValueError("Некорректные данные счетчиков")

            if not self.is_all_times_valid(data.get("time", [])):
                raise ValueError("Некорректные данные времени")

            if not self.is_valid_sensors(filt_data):
                raise ValueError("Некорректная информация по датчикам")

            # более актуальное время последний элемент
            created_at = data.get("time")[-1]

            if not created_at:
                raise ValueError("Нет времени")

            created_at = datetime.datetime.strptime(created_at, '%Y/%m/%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

            modem, created = Modem.objects.get_or_create(
                mac_address=data.get("mac"),
                defaults={'created_ad': created_at}
            )

            # нужно записывать только одно значение соответствующее времени
            for counter in data["counters"]:
                if counter.get("energy"):
                    counter_data = {
                        'modem_id': modem,
                        'address': counter.get("address")[-1],
                        'energy': counter.get("energy")[-1],
                        'cos_fi_a': counter.get("cos_fi_a")[-1],
                        'cos_fi_b': counter.get("cos_fi_b")[-1],
                        'cos_fi_c': counter.get("cos_fi_c")[-1],
                        'cos_fi_common': counter.get("cos_fi_common")[-1],
                        'freq_a': counter.get("freq_a")[-1],
                        'freq_b': counter.get("freq_b")[-1],
                        'freq_c': counter.get("freq_c")[-1],
                        'freq_common': counter.get("freq_common")[-1],
                        'voltage_a': counter.get("voltage_a")[-1],
                        'voltage_b': counter.get("voltage_b")[-1],
                        'voltage_c': counter.get("voltage_c")[-1],
                        'voltage_common': counter.get("voltage_common")[-1],
                        'current_a': counter.get("current_a")[-1],
                        'current_b': counter.get("current_b")[-1],
                        'current_c': counter.get("current_c")[-1],
                        'current_common': counter.get("current_common")[-1],
                        'whole_power_a': counter.get("whole_power_a")[-1],
                        'whole_power_b': counter.get("whole_power_b")[-1],
                        'whole_power_c': counter.get("whole_power_c")[-1],
                        'active_power_a': counter.get("active_power_a")[-1],
                        'active_power_b': counter.get("active_power_b")[-1],
                        'active_power_c': counter.get("active_power_c")[-1],
                        'reactive_power_a': counter.get("reactive_power_a")[-1],
                        'reactive_power_b': counter.get("reactive_power_b")[-1],
                        'reactive_power_c': counter.get("reactive_power_c")[-1],
                        'created_at': created_at
                    }
                    Counter.objects.update_or_create(
                        modem_id=modem,
                        address=counter_data['address'],
                        defaults=counter_data
                    )

            for i in range(1, max(len(filt_data) // 3, 2) + 1):
                if data.get(f"name" + str(i)):
                    sensor_data = {
                        'mac_address': data.get(f"name" + str(i)),
                        'vibration': data.get(f"vibrations" + str(i))[-1],
                        'temperature': data.get(f"temperature" + str(i))[-1],
                        'modem_id': modem,
                        'created_ad': created_at
                    }
                    Sensor.objects.update_or_create(
                        mac_address=sensor_data['mac_address'],
                        modem_id=modem,
                        defaults=sensor_data
                    )

            return Response({"message": "Data processed or updated successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
