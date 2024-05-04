import requests

from objects.vehicle import Vehicle


class VehicleApiClient:
    DEFAULT_TIMEOUT = 20

    @classmethod
    def request(self, method, url, json=None, timeout=DEFAULT_TIMEOUT):
        try:
            response = requests.request(method=method, url=url, json=json, timeout=timeout)
            response.raise_for_status()
            return response.json() if response.text else None
        except requests.exceptions.Timeout as err:
            print(f'[request] timeout error {err}')


class VehicleManager:
    def __init__(self, url, api_client=VehicleApiClient):
        self.url = url
        self.api_client = api_client

    def get_vehicles(self):
        """Данные по всем авто в базе."""
        data = self.api_client.request('get', f'{self.url}/vehicles')
        return [self._create_vehicle(vehicle_data) for vehicle_data in data]

    def filter_vehicles(self, params):
        """Фильтрация авто по параметрам."""
        all_vehicles = self.get_vehicles()
        filtered_vehicles = []
        for vehicle in all_vehicles:
            match = True
            for key, value in params.items():
                if getattr(vehicle, key, None) != value:
                    match = False
                    break
            if match:
                filtered_vehicles.append(vehicle)

        return filtered_vehicles

    def get_vehicle(self, vehicle_id):
        """Данные по единичному авто."""
        data = self.api_client.request('get', f'{self.url}/vehicles/{vehicle_id}')
        return self._create_vehicle(data)

    def add_vehicle(self, vehicle):
        """Добавление нового авто."""
        vehicle_data = vars(vehicle)
        if vehicle_data.get('id') is None:
            del vehicle_data['id']
        data = self.api_client.request('post', f'{self.url}/vehicles', vehicle_data)
        return self._create_vehicle(data)

    def update_vehicle(self, vehicle):
        """Обновление данных авто."""
        data = self.api_client.request('put', f'{self.url}/vehicles/{vehicle.id}', vars(vehicle))
        return self._create_vehicle(data)

    def delete_vehicle(self, id):
        """Удаление данных по авто."""
        return self.api_client.request('delete', f'{self.url}/vehicles/{id}')

    def get_distance(self, id1, id2):
        """Расстояние между двумя авто."""
        vehicle1 = self.get_vehicle(id1)
        vehicle2 = self.get_vehicle(id2)
        return vehicle1.coordinate() - vehicle2.coordinate()

    def get_nearest_vehicle(self, id):
        """Найти ближайшее авто."""
        target_vehicle_coordinate = self.get_vehicle(id).coordinate()
        vehicles = self.get_vehicles()
        vehicles.sort(key=lambda vehicle: abs(target_vehicle_coordinate - vehicle.coordinate()))
        return vehicles[1] if len(vehicles) > 1 else None

    def _create_vehicle(self, data):
        """Создания экземпляра авто."""
        return Vehicle(**data)
