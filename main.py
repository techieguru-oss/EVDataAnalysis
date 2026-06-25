from src.load_data import load_dataset
from src.clean_data import clean_dataset
from src.analyze_data import generate_summary
from src.visualize_data import *

DATASET = (
    "data/"
    "Electric_Vehicle_Population_Data.csv"
)

df = load_dataset(DATASET)

df = clean_dataset(df)

generate_summary(df)

df.to_csv(
    "data/EV_population_cleaned.csv",
    index=False
)

plot_electric_range(df)

plot_make_distribution(df)

plot_range_vs_msrp(df)

plot_heatmap(df)

plot_top_countries(df)

print(
    "\nAnalysis completed successfully."
)