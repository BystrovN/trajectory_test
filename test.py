import unittest

from objects.coordinate import Coordinate
from vehicle_manager import VehicleManager, Vehicle


class TestCoordinate(unittest.TestCase):
    def test_distance_between_coordinates(self):
        coord1 = Coordinate(52.2297, 21.0122)
        coord2 = Coordinate(40.7128, -74.0060)
        distance = coord1 - coord2
        self.assertAlmostEqual(distance, 6854204, delta=1)


class TestVehicleManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = VehicleManager(url='https://test.tspb.su/test-task')

    def test_get_vehicles(self):
        vehicles = self.manager.get_vehicles()
        self.assertEqual(len(vehicles), 20)

    def test_filter_vehicles(self):
        filtered_vehicles = self.manager.filter_vehicles(params={'name': 'Toyota'})
        self.assertEqual(len(filtered_vehicles), 1)
        self.assertEqual(filtered_vehicles[0].name, 'Toyota')

    def test_get_vehicle(self):
        vehicle_id = 1
        vehicle = self.manager.get_vehicle(vehicle_id)
        self.assertEqual(vehicle.id, vehicle_id)

    def test_add_vehicle(self):
        vehicle_data = Vehicle(
            name='Test',
            model='Model',
            year=2022,
            color='Black',
            price=25000,
            latitude=55.753215,
            longitude=37.620393,
        )
        added_vehicle = self.manager.add_vehicle(vehicle_data)
        self.assertIsNotNone(added_vehicle.id)
        for attr_name in vars(vehicle_data):
            self.assertEqual(getattr(added_vehicle, attr_name), getattr(vehicle_data, attr_name))

    def test_update_vehicle(self):
        vehicle_data = Vehicle(
            id=1,
            name='UpdatedName',
            model='UpdatedModel',
            year=2023,
            color='Blue',
            price=30000,
            latitude=55.753215,
            longitude=37.620393,
        )
        updated_vehicle = self.manager.update_vehicle(vehicle_data)
        for attr_name in vars(vehicle_data):
            self.assertEqual(getattr(updated_vehicle, attr_name), getattr(vehicle_data, attr_name))

    def test_get_distance(self):
        id1 = 1
        id2 = 2
        distance = self.manager.get_distance(id1, id2)
        expected_distance = 638005
        self.assertAlmostEqual(distance, expected_distance, delta=1)


if __name__ == "__main__":
    unittest.main()
