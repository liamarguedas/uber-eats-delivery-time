def StrTransformation(data: pd.DataFrame):
	data['Weatherconditions'] = data['Weatherconditions'].apply(lambda value: value.split(' ')[-1]) 
	for feature in data.select_dtypes(include = 'O').columns:
    	data[feature] = data[feature].apply(lambda value: np.nan if pd.isnull(value) else value.replace(' ', ''))
    return data