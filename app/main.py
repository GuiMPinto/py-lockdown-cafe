from errors import (OutdatedVaccineError, NotVaccinatedError,
                    NotWearingMaskError)
from cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    masks_to_buy = 0

    try:
        for friend in friends:
            cafe.visit_cafe(friend)

    except NotVaccinatedError:
        return "NotVaccinatedError"        

    except OutdatedVaccineError:
        return "All friends should be vaccinated"

    except NotWearingMaskError:
        masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return "Friends can go to {cafe.name}"
