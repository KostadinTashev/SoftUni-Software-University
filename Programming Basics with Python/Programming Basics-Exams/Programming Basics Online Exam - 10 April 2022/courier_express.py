shipment_kilogram = float(input())
type_service = input()
distance_in_kilometers = int(input())
total_price = 0
transport_price = 0

if type_service == "standard":
    if shipment_kilogram < 1:
        total_price = distance_in_kilometers * 0.03
    elif 1 <= shipment_kilogram < 10:
        total_price = distance_in_kilometers * 0.05
    elif 10 <= shipment_kilogram < 40:
        total_price = distance_in_kilometers * 0.10
    elif 40 <= shipment_kilogram < 90:
        total_price = distance_in_kilometers * 0.15
    elif 90 <= shipment_kilogram < 150:
        total_price = distance_in_kilometers * 0.20
elif type_service == "express":
    if shipment_kilogram < 1:
        transport_price = distance_in_kilometers * 0.03
        markup_kg = 0.8 * 0.03
        markup_km = shipment_kilogram * markup_kg
        total_markup = distance_in_kilometers * markup_km
        total_price = transport_price + total_markup
    elif 1 <= shipment_kilogram < 10:
        transport_price = distance_in_kilometers * 0.05
        markup_kg = 0.4 * 0.05
        markup_km = shipment_kilogram * markup_kg
        total_markup = distance_in_kilometers * markup_km
        total_price = transport_price + total_markup
    elif 10 <= shipment_kilogram < 40:
        transport_price = distance_in_kilometers * 0.10
        markup_kg = 0.05 * 0.10
        markup_km = shipment_kilogram * markup_kg
        total_markup = distance_in_kilometers * markup_km
        total_price = transport_price + total_markup
    elif 40 <= shipment_kilogram < 90:
        transport_price = distance_in_kilometers * 0.15
        markup_kg = 0.02 * 0.15
        markup_km = shipment_kilogram * markup_kg
        total_markup = distance_in_kilometers * markup_km
        total_price = transport_price + total_markup
    elif 90 <= shipment_kilogram < 150:
        transport_price = distance_in_kilometers * 0.20
        markup_kg = 0.01 * 0.20
        markup_km = shipment_kilogram * markup_kg
        total_markup = distance_in_kilometers * markup_km
        total_price = transport_price + total_markup

print(f"The delivery of your shipment with weight of {shipment_kilogram:.3f} kg. would cost {total_price:.2f} lv.")

