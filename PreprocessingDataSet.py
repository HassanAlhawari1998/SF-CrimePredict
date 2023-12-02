
import pandas as pd

file_path = "C:\\Users\\HassanAlhawari\\Downloads\\sampleSubmission.csv"
dataset = pd.read_csv(file_path, sep=";")
selected_columns = dataset[["LARCENY.THEFT", "ASSAULT", "DRUG.NARCOTIC", "VEHICLE.THEFT", "BURGLARY"]]

print(selected_columns)

output_file_path = "C:\\Users\\HassanAlhawari\\Downloads\\sampleSubmission_selected.csv"
selected_columns.to_csv(output_file_path, index=False)