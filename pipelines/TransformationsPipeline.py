from sklearn.base import BaseEstimator, TransformerMixin
from DistanceCalculator import distcalculate
import pandas
import numpy

class MapMissingValues(BaseEstimator, TransformerMixin):
    def __init__(self, data):
        
        if not isinstance(data, pandas.DataFrame):
            
            raise ValueError('data should be type pandas.DataFrame') 
        
        self.data = data
        
    def fit(self, X, y = None):
        
        return self
    
    def transform(self, X, copy = False):
        
        if copy:
            X = X.copy()
        
        for column in self.data.columns:
            
            X[column] = X[column].apply(lambda value: numpy.nan if value == 'NaN ' else value)
        
        return X
    
class DateTime(BaseEstimator, TransformerMixin):
    def __init__(self, data):
        
        if not isinstance(data, pandas.DataFrame):
            
            raise ValueError('data should be type pandas.DataFrame')
        
        self.data = data
        
    def fit(self, X, y = None):
        
        return self
    
    def transform(self, X, copy = False):
        
        if copy:
            X = X.copy()
        
        X['Time_Orderd'] = X['Order_Date'] + ' ' + X['Time_Orderd']
        X['Time_Order_picked'] = X['Order_Date'] + ' ' + X['Time_Order_picked']
        X['Time_Orderd'] = pandas.to_datetime(X['Time_Orderd'], format = '%d-%m-%Y %H:%M:%S')
        X['Time_Order_picked'] = pandas.to_datetime(X['Time_Order_picked'], format = '%d-%m-%Y %H:%M:%S')
        X['Time_To_Pick'] = (X['Time_Order_picked'] - X['Time_Orderd']).astype('timedelta64[m]')
        X['Time_To_Pick'] = X['Time_To_Pick'].apply(lambda value: value if value not in [-1425.0, -1430.0, -1435.0] else 15.0 if value == -1425.0 else 10.0 if value == -1430.0 else 5.0)
        X['Order_Year'] = X['Time_Orderd'].apply(lambda value: value.year)
        X['Order_Month'] = X['Time_Orderd'].apply(lambda value: value.month).map({1:'January', 2:'February',
	 	3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October',11:'November', 12:'December'})
        X['Order_Day'] = X['Time_Orderd'].apply(lambda value: value.dayofweek).map({0:'Monday', 1:'Tuesday', 2:'Wednesday',
	 	3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'})
        X['OrderTime'] = pandas.to_datetime(X['Time_Order_picked']).apply(lambda value: value.hour)
        X['TypeOfMeal'] = X['OrderTime'].apply(lambda value: "Breakfast" if value in [8, 9, 10, 11] else "Launch" if value in [12, 13, 14, 15, 16] else "Dinner")
        
        return X
        
class SetDtypes(BaseEstimator, TransformerMixin):
    def __init__(self, data):
        
        if not isinstance(data, pandas.DataFrame):
            
            raise ValueError('data should be type pandas.DataFrame')
        
        self.data = data
        
    def fit(self, X, y = None):
        
        return self
    
    def transform(self, X, copy = False):
        
        if copy:
            X = X.copy()
        X['Delivery_person_Age'] = X['Delivery_person_Age'].astype(float)
        X['Delivery_person_Ratings'] = X['Delivery_person_Ratings'].astype(float)
        X['multiple_deliveries'] = X['multiple_deliveries'].astype(float)
        X['Vehicle_condition'] = X['Vehicle_condition'].astype(float)
        
        return X
    
class TransformStr(BaseEstimator, TransformerMixin):
    def __init__(self, data):
        
        if not isinstance(data, pandas.DataFrame):
            
            raise ValueError('data should be type pandas.DataFrame')
        
        self.data = data
        
    def fit(self, X, y = None):
        
        return self
    
    def transform(self, X, copy = False):
        
        if copy:
            X = X.copy()
        
        X['Weatherconditions'] = X['Weatherconditions'].apply(lambda value: value.split(' ')[-1])
        
        for feature in X.select_dtypes(include = 'O').columns:
            X[feature] = X[feature].apply(lambda value: numpy.nan if pandas.isnull(value) else value.replace(' ', ''))
        
        return X
    
class ImputeMissingValues(BaseEstimator, TransformerMixin):
    def __init__(self, data):
        
        if not isinstance(data, pandas.DataFrame):
            
            raise ValueError('data should be type pandas.DataFrame')
        
        self.data = data
        
    def fit(self, X, y = None):
        
        return self
    
    def transform(self, X, copy = False):
        
        if copy:
            X = X.copy()
        X['TotalNaN'] = X.isna().sum(axis = 1)
        X = X[X['TotalNaN'] < 5]
        X.loc[X['City'].isna(), 'City'] = 'Metropolitian'
        X.loc[X['multiple_deliveries'].isna(), 'multiple_deliveries'] = 1.0
        X.loc[X['Delivery_person_Ratings'].isna(), 'Delivery_person_Ratings'] = 4.7
        X.loc[X['Festival'].isna(), 'Festival'] = 'No'
        X.loc[X['Delivery_person_Age'].isna(), 'Delivery_person_Age'] = 29.0
        X = X.drop('TotalNaN', axis = 1)
        
        X = X.reset_index(drop = True)
        
        return X
    
class GetDistances(BaseEstimator, TransformerMixin):
    def __init__(self, data):
        
        if not isinstance(data, pandas.DataFrame):
            
            raise ValueError('data should be type pandas.DataFrame')
        
        self.data = data
        
    def fit(self, X, y = None):
        
        return self
    
    def transform(self, X, copy = False , quantile99 = 20.851726357533593):
        
        if copy:
            X = X.copy()
        
        X['DeliveryDistance'] = numpy.zeros_like(X.shape[0])

        for i in range(len(X)):
            X.loc[i, 'DeliveryDistance'] = distcalculate(X.loc[i, 'Restaurant_latitude'], 
                                        X.loc[i, 'Restaurant_longitude'], 
                                        X.loc[i, 'Delivery_location_latitude'], 
                                        X.loc[i, 'Delivery_location_longitude'])
            
        for index in X[X['DeliveryDistance'] > quantile99].index:
            
            distance = X[X['Time_taken(min)'] == X.iloc[index]['Time_taken(min)']].groupby('Time_taken(min)').mean()['DeliveryDistance'].values[0]
            
            X.at[index, 'DeliveryDistance'] = distance
            
        return X
    
class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self, data):
        
        if not isinstance(data, pandas.DataFrame):
            
            raise ValueError('data should be type pandas.DataFrame')
        
        self.data = data
        
    def fit(self, X, y = None):
        
        return self
    
    def transform(self, X, copy = False ):
        
        if copy:
            X = X.copy()
            
        X['City'] = X['City'].apply(lambda value: 'Urban' if value == 'Semi-Urban' else value)
        X = X[['Delivery_person_Age', 'Delivery_person_Ratings', 'Weatherconditions',
       'Road_traffic_density', 'Vehicle_condition', 'Type_of_order',
       'Type_of_vehicle', 'multiple_deliveries', 'City', 'Order_Day',
       'DeliveryDistance', 'OrderTime', 'TypeOfMeal']]
        X = pandas.get_dummies(X, drop_first = True)
        
        return X