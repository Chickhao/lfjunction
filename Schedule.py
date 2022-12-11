class Schedule:
    count_id = 0

    def __init__(self, tutor_name, subject, level, date, time_slot):
        Schedule.count_id += 1
        self.__schedule_id = Schedule.count_id
        self.__tutor_name = tutor_name
        self.__subject = subject
        self.__level = level
        self.__date = date
        self.__time_slot = time_slot

    def get_schedule_id(self):
        return self.__schedule_id

    def get_tutor_name(self):
        return self.__tutor_name

    def get_subject(self):
        return self.__subject

    def get_level(self):
        return self.__level

    def get_date(self):
        return self.__date

    def get_time_slot(self):
        return self.__time_slot

    def set_schedule_id(self, schedule_id):
        self.__schedule_id = schedule_id

    def set_tutor_name(self, tutor_name):
        self.__tutor_name = tutor_name

    def set_subject(self, subject):
        self.__subject = subject

    def set_level(self, level):
        self.__level = level

    def set_date(self, date):
        self.__date = date

    def set_time_slot(self, time_slot):
        self.__time_slot = time_slot

