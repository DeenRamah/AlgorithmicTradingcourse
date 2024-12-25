//Resambling Data to different Time Frames
weekly_data =data['Close'].resample('W').mean()
print(weekly_data.head())
