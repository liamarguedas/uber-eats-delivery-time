def ImputeDistanceOutliers(data: pd.DataFrame, quantile99 = 20.851726357533593):
	for index in data[data['DeliveryDistance'] > quantile99].index:

		distance = data[data['Time_taken(min)'] == data.iloc[index]['Time_taken(min)']].groupby('Time_taken(min)').mean()['DeliveryDistance'].values[0]
    
    	data.at[index, 'DeliveryDistance'] = distance

    return data