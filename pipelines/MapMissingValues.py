def MapMissingValues(data: pd.DataFrame):
	for column in data.columns:
    	data[column] = data[column].apply(lambda value: np.nan if value == 'NaN ' else value)
    return data