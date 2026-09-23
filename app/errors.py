class NotVaccinatedError(Exception):
    pass


class VaccineError(Exception):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(VaccineError):
    pass
