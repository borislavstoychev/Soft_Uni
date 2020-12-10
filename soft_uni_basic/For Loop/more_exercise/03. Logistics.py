n = int(input())

price_to_transport = 0
bus_tons, truck_tons, train_tons = (0, 0, 0)
tonnage = 0

for i in range(1, n + 1):
    tonnage = int(input())
    if tonnage <= 3:
        bus_tons += tonnage
    if 4 <= tonnage <= 11:
        truck_tons += tonnage

    if tonnage >= 12:
        train_tons += tonnage

price_to_transport = (bus_tons * 200) + (truck_tons * 175) + (train_tons * 120)
tons = bus_tons + truck_tons + train_tons

print(f'{price_to_transport / tons:.2f}')
print(f'{(bus_tons / tons) * 100:.2f}%')
print(f'{(truck_tons / tons) * 100:.2f}%')
print(f'{(train_tons / tons) * 100:.2f}%')

