from vehicle_manager import VehicleManager, Vehicle

print('Создание экземпляра класса VehicleManager')
manager = VehicleManager(url='https://test.tspb.su/test-task')

print('Получение списка всех автомобилей')
print(manager.get_vehicles())

print('Получение списка автомобилей, у которых поле name равно "Toyota"')
print(manager.filter_vehicles(params={'name': 'Toyota'}))

print('Получение автомобиля с id=1')
print(manager.get_vehicle(vehicle_id=1))

print('Добавление нового автомобиля в базу данных')
print(
    manager.add_vehicle(
        vehicle=Vehicle(
            name='Toyota',
            model='Camry',
            year=2021,
            color='red',
            price=21000,
            latitude=55.753215,
            longitude=37.620393,
        )
    )
)

print('Изменение информации об автомобиле с id=1')
print(
    manager.update_vehicle(
        vehicle=Vehicle(
            id=1,
            name='Toyota',
            model='Camry',
            year=2021,
            color='red',
            price=21000,
            latitude=55.753215,
            longitude=37.620393,
        )
    )
)

print('Удаление автомобиля с id=1')
print(manager.delete_vehicle(id=1))

print('Расчет расстояния между автомобилями с id=1 и id=2')
print(manager.get_distance(id1=1, id2=2))

print('Нахождение ближайшего автомобиля к автомобилю с id=1')
print(manager.get_nearest_vehicle(id=1))
