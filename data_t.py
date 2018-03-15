import models


def populate_persons(s):
    ivanov = models.Person("Иванов")
    petrov = models.Person("Петров")
    sidorov = models.Person("Сидоров Денис")

    s.add_all([ivanov, petrov, sidorov])


def populate_facility_types(s):
    water = models.FacilityType("Вода", models.Units.cubic_meter)
    plot = models.FacilityType("Участок земли", models.Units.hundred)
    elecricity = models.FacilityType("Электричество", models.Units.kilowatt)

    s.add_all([water, plot, elecricity])


def populate_all(s):
    populate_facility_types(s)
    populate_persons(s)
