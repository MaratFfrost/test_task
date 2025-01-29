import os
import json
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

"""ИНФОРМАЦИЯ ПО ТЕСТАМ
1) тест который принимает данные по примеру того энд поинта в тз
принимает его верно и корректно выдает информацию о модемах, сенсорах и датчиках.
2) пустой запрос
3) неверный мак адрес
4) неверный формат температуры (неверными считаются данные с
типами данных не int либо float)
5) неверный формат времени
6) неверные данные в параметрах каунтера
7) отсутсвие какого-нибудь параметра в каунтерах
8) отсутсвие какого-нибудь параметра в сенсорах
9) неккоректный адрес в сенсоре (не строка)
10) отсутвие какого-нибудь нужного параметра
"""

class PostRequestTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def load_json_data(self, filename):
        json_path = os.path.join(os.path.dirname(__file__), 'json_data', filename)
        self.assertTrue(os.path.exists(json_path), f"Файл {filename} не найден!")
        with open(json_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    def post_request_and_assert(self, filename, expected_status_code):
        data = self.load_json_data(filename)
        post_response = self.client.post(reverse('Add or update info'), data, format='json')
        self.assertEqual(post_response.status_code, expected_status_code)
        return post_response

    def test_1(self):
        post_response = self.post_request_and_assert('data1.json', 201)

        get_modem_response = self.client.get(reverse("all modems"))
        get_sensors_response = self.client.get(reverse("all sensors"))
        get_counters_response = self.client.get(reverse("all counters"))

        self.assertEqual(get_modem_response.status_code, 200)
        self.assertEqual(get_sensors_response.status_code, 200)
        self.assertEqual(get_counters_response.status_code, 200)

    def test_2(self):
        post_response = self.client.post(reverse("Add or update info"), {}, format="json")
        self.assertEqual(post_response.status_code, 400)

    def test_3_to_10(self):
        for i in range(3, 11):
          self.post_request_and_assert(f'data{i}.json', 400)
