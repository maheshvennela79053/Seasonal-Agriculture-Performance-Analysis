# ============================================================
# SEASONAL AGRICULTURE PERFORMANCE ANALYSIS
# Python IDLE Project
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway


# ============================================================
# 1. LOAD DATASET
# ============================================================

file_path = r"C:\Users\hp\Downloads\Telegram Desktop\seasonal_agriculture_performance_dataset.csv"

df = pd.read_csv(file_path)

print("\n" + "=" * 60)
print("SEASONAL AGRICULTURE PERFORMANCE ANALYSIS")
print("=" * 60)

print("\nDataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ============================================================
# 2. BASIC DATA INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("BASIC DATA INFORMATION")
print("=" * 60)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


# ============================================================
# 3. DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

# Numerical columns
numeric_columns = df.select_dtypes(include=np.number).columns

# Fill missing numerical values with median
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns
categorical_columns = df.select_dtypes(include="object").columns

# Fill missing categorical values with mode
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Missing values after cleaning:",
      df.isnull().sum().sum())


# ============================================================
# 4. DATASET OVERVIEW
# ============================================================

print("\n" + "=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nNumber of States:", df["State"].nunique())
print("Number of Districts:", df["District"].nunique())
print("Number of Crops:", df["Crop"].nunique())
print("Number of Seasons:", df["Season"].nunique())

print("\nSeason Distribution:")
print(df["Season"].value_counts())

print("\nCrop Distribution:")
print(df["Crop"].value_counts())


# ============================================================
# 5. SEASONAL ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("SEASONAL PERFORMANCE ANALYSIS")
print("=" * 60)

season = df.groupby("Season").agg({
    "Yield_Tonnes_Ha": "mean",
    "Production_Tonnes": "sum",
    "Water_Used_m3": "mean",
    "Profit_INR": "mean",
    "Disease_Pest_Risk_pct": "mean"
}).round(2)

print("\nSeasonal Performance:")
print(season)


# Yield by season
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="Season",
    y="Yield_Tonnes_Ha",
    estimator="mean"
)
plt.title("Average Yield by Season")
plt.xlabel("Season")
plt.ylabel("Yield (Tonnes/Ha)")
plt.tight_layout()
plt.show()


# Profit by season
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="Season",
    y="Profit_INR",
    estimator="mean"
)
plt.title("Average Profit by Season")
plt.xlabel("Season")
plt.ylabel("Average Profit (INR)")
plt.tight_layout()
plt.show()


# ============================================================
# 6. CROP ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CROP PERFORMANCE ANALYSIS")
print("=" * 60)

crop = df.groupby("Crop").agg({
    "Yield_Tonnes_Ha": "mean",
    "Production_Tonnes": "sum",
    "Profit_INR": "mean"
}).sort_values(
    "Yield_Tonnes_Ha",
    ascending=False
).round(2)

print("\nCrop Performance:")
print(crop)


plt.figure(figsize=(10, 5))
sns.barplot(
    data=df,
    x="Crop",
    y="Yield_Tonnes_Ha",
    estimator="mean"
)
plt.title("Average Yield by Crop")
plt.xlabel("Crop")
plt.ylabel("Yield (Tonnes/Ha)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 7. STATE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("STATE PERFORMANCE ANALYSIS")
print("=" * 60)

state = df.groupby("State").agg({
    "Yield_Tonnes_Ha": "mean",
    "Production_Tonnes": "sum",
    "Profit_INR": "mean"
}).sort_values(
    "Yield_Tonnes_Ha",
    ascending=False
).round(2)

print("\nState Performance:")
print(state)


plt.figure(figsize=(10, 5))
state["Yield_Tonnes_Ha"].plot(kind="bar")
plt.title("Average Yield by State")
plt.xlabel("State")
plt.ylabel("Yield (Tonnes/Ha)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 8. ENVIRONMENTAL AND RESOURCE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("ENVIRONMENTAL AND RESOURCE ANALYSIS")
print("=" * 60)

environmental_variables = [
    "Rainfall_mm",
    "Avg_Temperature_C",
    "Humidity_pct",
    "Sunlight_Hours_Day",
    "Soil_Moisture_pct",
    "Fertilizer_kg_ha",
    "Water_Used_m3"
]

for variable in environmental_variables:

    plt.figure(figsize=(7, 5))

    sns.scatterplot(
        data=df,
        x=variable,
        y="Yield_Tonnes_Ha"
    )

    plt.title(variable + " vs Yield")
    plt.xlabel(variable)
    plt.ylabel("Yield (Tonnes/Ha)")
    plt.tight_layout()
    plt.show()


# ============================================================
# 9. IRRIGATION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("IRRIGATION ANALYSIS")
print("=" * 60)

irrigation = df.groupby("Irrigation_Method").agg({
    "Yield_Tonnes_Ha": "mean",
    "Water_Used_m3": "mean",
    "Profit_INR": "mean"
}).round(2)

print("\nIrrigation Performance:")
print(irrigation)


plt.figure(figsize=(9, 5))

sns.barplot(
    data=df,
    x="Irrigation_Method",
    y="Yield_Tonnes_Ha",
    estimator="mean"
)

plt.title("Yield by Irrigation Method")
plt.xlabel("Irrigation Method")
plt.ylabel("Yield (Tonnes/Ha)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 10. ECONOMIC ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("ECONOMIC PERFORMANCE")
print("=" * 60)

# Profit per hectare
df["Profit_Per_Hectare"] = (
    df["Profit_INR"] / df["Farm_Area_Hectares"]
)

economic = df.groupby("Season").agg({
    "Revenue_INR": "mean",
    "Total_Cost_INR": "mean",
    "Profit_INR": "mean",
    "Profit_Per_Hectare": "mean"
}).round(2)

print("\nEconomic Performance by Season:")
print(economic)


plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Season",
    y="Profit_Per_Hectare",
    estimator="mean"
)

plt.title("Average Profit per Hectare by Season")
plt.xlabel("Season")
plt.ylabel("Profit per Hectare (INR)")
plt.tight_layout()
plt.show()


# ============================================================
# 11. DISEASE AND PEST RISK
# ============================================================

print("\n" + "=" * 60)
print("DISEASE / PEST RISK ANALYSIS")
print("=" * 60)

risk = df.groupby("Season")[
    "Disease_Pest_Risk_pct"
].mean().round(2)

print("\nDisease/Pest Risk by Season:")
print(risk)


plt.figure(figsize=(8, 5))

risk.plot(kind="bar")

plt.title("Average Disease/Pest Risk by Season")
plt.xlabel("Season")
plt.ylabel("Risk (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Risk vs Yield
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Disease_Pest_Risk_pct",
    y="Yield_Tonnes_Ha",
    hue="Season"
)

plt.title("Disease/Pest Risk vs Yield")
plt.xlabel("Disease/Pest Risk (%)")
plt.ylabel("Yield (Tonnes/Ha)")
plt.tight_layout()
plt.show()


# ============================================================
# 12. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CORRELATION ANALYSIS")
print("=" * 60)

numeric_df = df.select_dtypes(include=np.number)

correlation = numeric_df.corr()

print("\nCorrelation with Yield:")

yield_correlation = (
    correlation["Yield_Tonnes_Ha"]
    .sort_values(ascending=False)
)

print(yield_correlation)


# Heatmap
plt.figure(figsize=(14, 10))

sns.heatmap(
    correlation,
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()


# ============================================================
# 13. ANOVA TEST
# ============================================================

print("\n" + "=" * 60)
print("STATISTICAL ANALYSIS - ANOVA")
print("=" * 60)

seasons = df["Season"].unique()

groups = [
    df[df["Season"] == season_name]["Yield_Tonnes_Ha"]
    for season_name in seasons
]

f_stat, p_value = f_oneway(*groups)

print("\nANOVA Test for Seasonal Yield")
print("F-statistic:", round(f_stat, 3))
print("P-value:", round(p_value, 5))

if p_value < 0.05:
    print("Result: Season has a statistically significant effect on yield.")
else:
    print("Result: Season does not have a statistically significant effect on yield.")


# ============================================================
# 14. FINAL FINDINGS
# ============================================================

print("\n" + "=" * 60)
print("FINAL FINDINGS")
print("=" * 60)

best_season = season["Yield_Tonnes_Ha"].idxmax()
best_crop = crop["Yield_Tonnes_Ha"].idxmax()
best_state = state["Yield_Tonnes_Ha"].idxmax()
best_profit_season = economic["Profit_INR"].idxmax()
lowest_risk_season = risk.idxmin()

print("\n1. Best season based on average yield:",
      best_season)

print("2. Best crop based on average yield:",
      best_crop)

print("3. Highest yielding state:",
      best_state)

print("4. Most profitable season:",
      best_profit_season)

print("5. Season with lowest disease/pest risk:",
      lowest_risk_season)


print("\nKey Recommendations:")
print("- Consider seasonal differences when planning crop production.")
print("- Select crops based on yield and profitability.")
print("- Optimize irrigation and water usage.")
print("- Monitor environmental conditions such as rainfall and soil moisture.")
print("- Give additional attention to seasons with higher disease/pest risk.")
print("- Use both productivity and economic performance for agricultural planning.")


# ============================================================
# 15. SAVE CLEANED DATASET
# ============================================================

output_file = "cleaned_seasonal_agriculture_dataset.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved as:", output_file)

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 60)
