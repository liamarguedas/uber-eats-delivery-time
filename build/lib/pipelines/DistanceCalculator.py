import numpy

def ToRadians(degrees):
    return degrees * (numpy.pi / 180)

def distcalculate(latitude1, longitude1, latitude2, longitude2, R = 6371):
    
    latitude = ToRadians(latitude2 - latitude1)
    
    longitude = ToRadians(longitude2 - longitude1)
    
    a = numpy.sin(latitude / 2) ** 2 + numpy.cos(ToRadians(latitude1)) * numpy.cos(ToRadians(latitude2)) * numpy.sin(longitude / 2) ** 2
    
    c = 2 * numpy.arctan2(numpy.sqrt(a), numpy.sqrt(1 - a))
    
    return R * c