import datetime

from errors import OutdatedVaccineError, NotVaccinatedError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        
        current_date = datetime.date.today()
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < current_date:
            raise OutdatedVaccineError("Vaccine is expired")

        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        if visitor["vaccine"] == False:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return "Welcome {self.name}"