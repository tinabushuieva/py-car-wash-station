from typing import Union


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: int) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: float) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.wash_single_car(car)
                price, difference = self.calculate_washing_price(car)
                income += price
                car.clean_mark += difference
            else:
                pass
        return income

    def calculate_washing_price(self, car: object) -> Union:
        difference = self.clean_power - car.clean_mark
        price = round(((car.comfort_class
                        * difference * self.average_rating)
                       / self.distance_from_city_center), 1)
        return price, difference

    def wash_single_car(self, car: object) -> str:
        print(f"{car.brand} was washed")

    def rate_service(self, rate: float) -> float:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                     * (self.count_of_ratings - 1) + rate)
                                    / self.count_of_ratings, 1)
        return self.average_rating
