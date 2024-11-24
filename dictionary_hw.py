car_4x2 = {
    "price": 1263400,
    "has_rear_led_turn_signals": False,
    "design_elements_zen": [
        "dark_executive_salon",
        "illumination_of_salon",
        "laers",
        "metalic_paint",
        "tinted",
    "heating",
    ],
    "panoramic_sunroof": {}
}

car_4x4 = {
    "price": 1470800,
    "has_rear_led_turn_signals": True,
    "design_elements_intense": [
        "dark_executive_salon",
        "illumination_of_salon",
        "laers",
        "metalic_paint",
        "tinted",
    "heating",
    ],
    "panoramic_sunroof": {
        "price_glass_roof": 29486
    }
}

print(car_4x4["panoramic_sunroof"])

for element in car_4x2["design_elements_zen"]:
    print("Element of design -", element)
