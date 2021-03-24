class SaveManager:
    def __init__(self):
        pass

    def save_to_file(self):
        pass

    def load_from_file(self):
        pass

    def create_new_save(self):
        pass

    def get_save_data(self):
        return ""

    @staticmethod
    def get_template_values():
        return '''
        {
        "mapId": "STARTING_MAP",
        "timestamp": get_time(),
        "someList": {
            "l1": [1, 2, 3],
            "l2": 1
        }
        '''
