def DateTime(data: pd.DataFrame):
	data['Time_Orderd'] = data['Order_Date'] + ' ' + data['Time_Orderd']
	data['Time_Order_picked'] = data['Order_Date'] + ' ' + data['Time_Order_picked']
	data['Time_Orderd'] = pd.to_datetime(data['Time_Orderd'], format = '%d-%m-%Y %H:%M:%S')
	data['Time_Order_picked'] = pd.to_datetime(data['Time_Order_picked'], format = '%d-%m-%Y %H:%M:%S')
	return data