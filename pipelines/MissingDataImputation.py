def ImputeValues(data: pd.DataFrame):
	data['TotalNaN'] = data.isna().sum(axis = 1)
	data = data[data['TotalNaN'] < 5]
	data.loc[data['City'].isna(), 'City'] = 'Metropolitian'
	data.loc[data['multiple_deliveries'].isna(), 'multiple_deliveries'] = 1.0
	data.loc[data['Delivery_person_Ratings'].isna(), 'Delivery_person_Ratings'] = 4.7
	data.loc[data['Festival'].isna(), 'Festival'] = 'No'
	data.loc[data['Delivery_person_Age'].isna(), 'Delivery_person_Age'] = 29.0
	data = data.drop('TotalNaN', axis = 1)
	return data