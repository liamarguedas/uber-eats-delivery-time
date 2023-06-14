def ToRadians(degrees):
    return degrees * (np.pi / 180)

def distcalculate(latitude1, longitude1, latitude2, longitude2, R = 6371):
    
    latitude = ToRadians(latitude2 - latitude1)
    
    longitude = ToRadians(longitude2 - longitude1)
    
    a = np.sin(latitude / 2) ** 2 + np.cos(ToRadians(latitude1)) * np.cos(ToRadians(latitude2)) * np.sin(longitude / 2) ** 2
    
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    return R * c

def CordDistance(data: pd.DataFrame):

    data['DeliveryDistance'] = np.nan

    for i in range(len(data)):
        data.loc[i, 'DeliveryDistance'] = distcalculate(data.loc[i, 'Restaurant_latitude'], 
                                        data.loc[i, 'Restaurant_longitude'], 
                                        data.loc[i, 'Delivery_location_latitude'], 
                                        data.loc[i, 'Delivery_location_longitude'])

    return data