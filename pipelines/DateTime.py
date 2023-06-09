def DateTime(data: pd.DataFrame):
	data['Time_Orderd'] = data['Order_Date'] + ' ' + data['Time_Orderd']
	data['Time_Order_picked'] = data['Order_Date'] + ' ' + data['Time_Order_picked']
	data['Time_Orderd'] = pd.to_datetime(data['Time_Orderd'], format = '%d-%m-%Y %H:%M:%S')
	data['Time_Order_picked'] = pd.to_datetime(data['Time_Order_picked'], format = '%d-%m-%Y %H:%M:%S')
	data['Time_To_Pick'] = (data['Time_Order_picked'] - data['Time_Orderd']).astype('timedelta64[m]')
	data['Order_Year'] = data['Time_Orderd'].apply(lambda value: value.year)
	data['Order_Month'] = data['Time_Orderd'].apply(lambda value: value.month).map({1:'January', 2:'February',
	3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October',11:'November', 12:'December'})
	data['Order_Day'] = data['Time_Orderd'].apply(lambda value: value.dayofweek).map({0:'Monday', 1:'Tuesday', 2:'Wednesday',
	3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'})
	return data