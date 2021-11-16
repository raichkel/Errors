import uncertainties as un

def parse_errors(**values):
    '''
    Turns input values into uncertainties.ufloats so that they can be used for error propagation
    -------------
    Args:
    - **values: Dictionary of all symbols used in expression, their values and errors, eg.x = (10,2), y=(30,0.5)
    -------------
    Returns:
    - value_tuple: tuple containing all input values with their uncertainties, eg. (10.0+/-2.0, 30.0+/-0.5) '''
    symbols=[]
    for key,value in values.items():
        values[key]= un.ufloat(value[0],value[1])
        symbols.append(values[key])
    value_tuple=tuple(symbols)
    return value_tuple
