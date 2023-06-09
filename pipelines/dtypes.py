def SetDtypes(data: pd.DataFrame):
	data['Delivery_person_Age'] = data['Delivery_person_Age'].astype(float)
	data['Delivery_person_Ratings'] = data['Delivery_person_Ratings'].astype(float)
	data['multiple_deliveries'] = data['multiple_deliveries'].astype(float)
	data['Vehicle_condition'] = data['Vehicle_condition'].astype(float)
	return data