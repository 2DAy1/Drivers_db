from report_of_monaco_2018_racing_dan import report


def get_drivers(path=None):
    drivers = {}
    for driver in report.create_drivers(path):
        drivers[driver.code] = {
            "number":
                driver.number,
            "name":
                driver.name,
            "company":
                driver.company,
            "result":
                driver.result
        }
    return drivers

