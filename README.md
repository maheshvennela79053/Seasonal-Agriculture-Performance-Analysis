# Seasonal Agriculture Performance Analysis

## Project Overview

Seasonal Agriculture Performance Analysis is a data analytics project that analyzes agricultural performance across different seasons, crops, and states.

The project uses Python to study agricultural factors such as rainfall, temperature, humidity, sunlight, soil moisture, fertilizer usage, irrigation, water consumption, yield, production, profit, and disease/pest risk.

The main objective is to identify patterns and relationships in agricultural performance and provide useful insights for agricultural planning and decision-making.

---

## Problem Statement

Agricultural performance is influenced by seasonal variations in environmental conditions, farming practices, resource availability, and market conditions.

This project analyzes the given agricultural dataset to investigate differences in agricultural performance across seasons and identify meaningful patterns, trends, relationships, and variations within the available data.

---

## Objectives

- Explore and understand the agricultural dataset.
- Identify and handle missing values.
- Check duplicate records.
- Analyze agricultural performance across seasons.
- Compare crop performance.
- Compare agricultural performance across states.
- Study relationships between environmental factors and yield.
- Analyze irrigation methods and water usage.
- Analyze revenue, cost, and profit.
- Analyze disease and pest risk.
- Perform correlation analysis.
- Perform statistical analysis using ANOVA.
- Generate data-driven findings and recommendations.

---

## Dataset

The dataset contains **4,000 records and 28 columns** related to agricultural activities.

### Main Variables

- Farm_ID
- State
- District
- Crop
- Season
- Farm_Area_Hectares
- Rainfall_mm
- Avg_Temperature_C
- Humidity_pct
- Sunlight_Hours_Day
- Soil_pH
- Soil_Moisture_pct
- Nitrogen_kg_ha
- Phosphorus_kg_ha
- Potassium_kg_ha
- Irrigation_Method
- Water_Used_m3
- Fertilizer_kg_ha
- Pesticide_Litre_ha
- Seed_Quality_Score
- Yield_Tonnes_Ha
- Production_Tonnes
- Market_Price_INR_Tonne
- Total_Cost_INR
- Revenue_INR
- Profit_INR
- Water_Efficiency_t_per_1000m3
- Disease_Pest_Risk_pct

---

## Technologies Used

- **Python**
- **Pandas** – Data loading, cleaning, grouping and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical and graphical visualization
- **SciPy** – Statistical analysis and ANOVA
- **Python IDLE** – Development environment

---

## Data Cleaning

The following data-cleaning steps were performed:

- Checked the dataset structure and data types.
- Checked missing values.
- Filled missing numerical values using the median.
- Filled missing categorical values using the mode.
- Checked for duplicate rows.
- Prepared the dataset for further analysis.

---

## Analysis Performed

### 1. Seasonal Performance Analysis

Agricultural performance was compared across:

- Kharif
- Rabi
- Zaid

The analysis included:

- Average yield
- Total production
- Average water usage
- Average profit
- Disease/pest risk

A bar chart was created to compare average yield across seasons.

---

### 2. Crop Performance Analysis

Different crops were compared based on:

- Average yield
- Total production
- Average profit

A visualization was created to identify differences in average crop yield.

---

### 3. State Performance Analysis

Agricultural performance was compared across different states using:

- Average yield
- Total production
- Average profit

A bar chart was used to compare average yield across states.

---

### 4. Environmental and Resource Analysis

The project studies the relationship between yield and different environmental/resource factors:

- Rainfall
- Average temperature
- Humidity
- Sunlight hours
- Soil moisture
- Fertilizer usage
- Water usage

Scatter plots were created to visualize the relationship between these variables and agricultural yield.

---

### 5. Irrigation Analysis

Different irrigation methods were compared based on:

- Average yield
- Average water usage
- Average profit

A bar chart was created to compare yield across irrigation methods.

---

### 6. Economic Analysis

The project analyzes agricultural economic performance using:

- Revenue
- Total cost
- Profit
- Profit per hectare

Profit per hectare was calculated using:

`Profit per Hectare = Profit / Farm Area`

Season-wise economic performance was analyzed and visualized.

---

### 7. Disease and Pest Risk Analysis

Disease and pest risk was analyzed across different seasons.

The project also examines the relationship between disease/pest risk and agricultural yield using a scatter plot.

---

### 8. Correlation Analysis

A correlation matrix was created to understand relationships between numerical variables.

A correlation heatmap was also generated to visually represent the strength and direction of relationships between variables.

The correlation of different numerical variables with yield was specifically analyzed.

---

### 9. Statistical Analysis

One-way ANOVA was performed to test whether there is a statistically significant difference in agricultural yield between different seasons.

The ANOVA analysis uses:

- F-statistic
- P-value

A significance level of **0.05** is used to interpret the result.

---

## Key Findings

The analysis provides insights into:

- Differences in agricultural yield across seasons.
- Differences in crop performance.
- Regional variations in agricultural performance.
- Relationships between environmental conditions and yield.
- Differences between irrigation methods.
- Seasonal differences in revenue, cost and profit.
- Variation in disease and pest risk.
- Relationships between important numerical agricultural variables.
- Statistical differences in yield across seasons.

The exact findings and values are generated by the Python analysis program.

---

## Recommendations

Based on the analysis, the following recommendations can be considered:

- Consider seasonal differences when planning agricultural activities.
- Select crops based on both yield and profitability.
- Optimize irrigation and water usage.
- Monitor environmental conditions such as rainfall and soil moisture.
- Pay attention to seasons with higher disease/pest risk.
- Use regional agricultural performance data for planning.
- Consider both productivity and economic performance when making agricultural decisions.

---

## Future Scope

The project can be further improved by:

- Developing machine learning models for yield prediction.
- Using real-time weather data.
- Building an interactive agricultural dashboard.
- Including data from more years and regions.
- Adding crop recommendation systems.
- Integrating real-time market price information.
- Developing irrigation and fertilizer recommendation systems.

---

## Project Files

The repository contains:

- `seasonal_agriculture_analysis.py` – Python source code
- `seasonal_agriculture_performance_dataset.csv` – Original dataset
- `cleaned_seasonal_agriculture_dataset.csv` – Cleaned dataset
- `README.md` – Project documentation

---

## Conclusion

This project demonstrates the use of Python-based data analytics to understand seasonal agricultural performance.

The analysis covers seasonal, crop-wise, state-wise, environmental, irrigation, economic, and disease/pest-related factors. Correlation analysis and ANOVA are also used to identify relationships and statistically evaluate seasonal differences in yield.

The insights obtained from the analysis can support better agricultural planning, resource utilization, crop selection, and economic decision-making.

---

## Author

**Name:** Vennela Mahesh

**AICTE STU ID:** STU6a0e0ee8467301779306216

**College:** Lovely Professional University
