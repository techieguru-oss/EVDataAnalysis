# Electric Vehicle Data Analysis

## Project Overview

This project performs data cleaning, exploratory data analysis (EDA), and visualization on the Electric Vehicle Population Dataset.

The objective is to analyze EV adoption trends, identify leading manufacturers, study electric range distributions, and explore relationships between vehicle specifications.

---

## Features

* Data loading using Pandas
* Missing value handling
* Duplicate record removal
* Statistical analysis
* Manufacturer-wise EV distribution
* Electric range analysis
* Correlation analysis
* Automated visualization generation
* Modular Python project structure

---

## Project Structure

```text
EVDataAnalysis/
│
├── data/
│   ├── Electric_Vehicle_Population_Data.csv
│   └── EV_population_cleaned.csv
│
├── outputs/
│   ├── electric_range_histogram.png
│   ├── vehicle_make_distribution.png
│   ├── range_vs_msrp.png
│   ├── correlation_heatmap.png
│   └── top_counties.png
│
├── src/
│   ├── __init__.py
│   ├── load_data.py
│   ├── clean_data.py
│   ├── analyze_data.py
│   └── visualize_data.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Dataset

Electric Vehicle Population Dataset containing information about:

* Vehicle Make
* Vehicle Model
* Electric Range
* Base MSRP
* County
* Legislative District
* Vehicle Type

---

## Data Cleaning Steps

1. Filled missing values in Electric Range using median.
2. Filled missing values in Base MSRP using median.
3. Replaced missing Legislative District values with "Unknown".
4. Removed duplicate records.
5. Saved cleaned dataset.

---

## Exploratory Data Analysis

### Summary Statistics

* Total records
* Total columns
* Average electric range
* Median electric range
* Top vehicle manufacturers
* Top counties by EV adoption

### Visualizations

#### Electric Range Distribution

Shows the distribution of vehicle electric ranges.

#### Vehicle Manufacturer Distribution

Displays the most common EV manufacturers.

#### Electric Range vs Base MSRP

Analyzes the relationship between range and vehicle price.

#### Correlation Heatmap

Shows correlations among numerical variables.

#### Top Countries by EV Adoption

Highlights counties with the highest EV registrations.

---
## Sample Visualizations

### Project Structure

![Project Structure](outputs/Project_Structure.png)

### Terminal Output

![Terminal Output](outputs/terminal_output.png)

### Electric Range Distribution

![Electric Range Distribution](outputs/electric_range_histogram.png)

### Vehicle Manufacturer Distribution

![Vehicle Manufacturer Distribution](outputs/vehicle_make_distribution.png)

### Electric Range vs Base MSRP

![Electric Range vs Base MSRP](outputs/range_vs_msrp.png)

### Correlation Heatmap

![Correlation Heatmap](outputs/correlation_heatmap.png)

### Top Counties by EV Adoption

![Top Counties](outputs/top_countries.png)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/techieguru-oss/EVDataAnalysis.git
```

Move into the project directory:

```bash
cd EVDataAnalysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute:

```bash
python main.py
```

Generated visualizations will be stored inside the outputs folder.

---

## Sample Output

```text
===== DATASET SUMMARY =====

Rows: 261698
Columns: 17

Average Electric Range: 42.61
Median Electric Range: 0.00

Top 10 Vehicle Manufacturers:
TESLA
CHEVROLET
NISSAN
...
```

---

## Author

Akansha Singh

Computer Science Student