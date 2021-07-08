class Driver():
    _all = []
    _count = 0
    
    def __init__(self, name, car_make, car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model
        Driver.add_driver(self)
        Driver.up_count()
        
    @property
    def name(self):
        return self._name
    
    @property
    def car_make(self):
        return self._car_make
    
    @property
    def car_model(self):
        return self._car_model
    
    @classmethod
    def add_driver(cls, driver):
        cls._all.append(driver)
        
    @classmethod
    def up_count(cls):
        cls._count += 1
        
    @classmethod
    def fleet_size(cls):
        return cls._count
    
    @classmethod
    def driver_names(cls):
        return [driver.name for driver in cls._all]
    
    @classmethod
    def fleet_models(cls):
        return [driver.car_model for driver in cls._all]
    
    @classmethod
    def fleet_makes(cls):
        return [driver.car_make for driver in cls._all]
    
    @classmethod
    def fleet_makes_count(cls):
        makes_lst = cls.fleet_makes()
        make_dict = {}
        for make in set(makes_lst):
            make_dict[make] = makes_lst.count(make)
        return make_dict
    
    @classmethod
    def fleet_models_count(cls):
        models_lst = cls.fleet_models()
        models_dict = {}
        for model in set(models_lst):
            models_dict[model] = models_lst.count(model)
        return models_dict
    
    @classmethod
    def percent_of_fleet(cls, make):
        make_dict = cls.fleet_makes_count()
        percent = round((make_dict[make]/cls.fleet_size()) * 100, 3)
        return str(percent) + "%"
    
    
    