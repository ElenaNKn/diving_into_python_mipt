import os
import csv

list_car_type = ['car', 'truck', 'spec_machine']  # list of possible car types
photo_file_exten = ['.jpg', '.jpeg', '.png', '.gif']  # list of possible file extensions

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext (self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = list_car_type[0]
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.car_type = list_car_type[1]
        super().__init__(brand, photo_file_name, carrying)
        # try to split string with body parameters and convert them to float
        try:
            if body_whl == '':
                raise ValueError
            l, w,h = map (float, body_whl.split('x'))
        except ValueError:
            self.body_length, self.body_width, self.body_height  = 0.0, 0.0, 0.0
        else:
            self.body_length, self.body_width, self.body_height  = l, w, h

    def get_body_volume (self):
        return self.body_height * self.body_length * self.body_width

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = list_car_type[2]
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

# function reads from *.csv and appends list with class objects
def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # pass the heading string of file
        for row in reader:
            new_machine = line_reader(row)
            if new_machine and new_machine.get_photo_file_ext() in photo_file_exten:
                car_list.append(new_machine)
    return car_list

# function validates parameters and creates class objects
def line_reader(row):
    if len(row) < 7:
        return None
    # validation parameters for CarBase class object
    try:
        car_type = row[0]
        brand = row[1]
        photo_file_name = row[3]
        if car_type == '' or brand == '' or photo_file_name == '':
            raise ValueError
        carrying = row[5]
        float(carrying)
    except Exception:
        return None
    # validation parameters and creation Car class object
    if car_type == list_car_type[0]:
        try:
            passenger_seats_count = row[2]
            int(passenger_seats_count)
        except ValueError or TypeError:
            return None
        new_object = Car(brand,photo_file_name,carrying,passenger_seats_count)
    # validation parameters and creation Truck class object
    elif car_type == list_car_type[1]:
        body_whl = row[4]
        new_object = Truck(brand,photo_file_name,carrying,body_whl)
    # validation parameters and creation SpecMachine class object
    elif car_type == list_car_type[2]:
        try:
            extra = row[6]
            if extra == '':
                raise ValueError
        except ValueError:
            return None
        new_object = SpecMachine(brand,photo_file_name,carrying,extra)
    else:
        new_object = None
    return new_object

if __name__ == '__main__':
    pass