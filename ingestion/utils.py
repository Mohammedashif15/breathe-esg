def detect_scope(source_type):

    if source_type == 'SAP':
        return 'SCOPE1'

    elif source_type == 'UTILITY':
        return 'SCOPE2'

    return 'SCOPE3'


def normalize_unit(
    quantity,
    unit
):

    unit = unit.lower()

    if unit == 'mwh':
        return quantity * 1000, 'kwh'

    elif unit == 'kwh':
        return quantity, 'kwh'

    elif unit == 'litre':
        return quantity, 'litre'

    elif unit == 'km':
        return quantity, 'km'

    return quantity, unit


def detect_suspicious(
    quantity
):

    return quantity > 10000