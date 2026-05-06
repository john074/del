import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файла
file_path = "kernel_error_stats.csv"
df = pd.read_csv(file_path)

# График количества ошибок
plt.figure()
plt.bar(df["ErrorType"], df["Count"])
plt.xticks(rotation=30)
plt.title("Kernel Error Distribution")
plt.xlabel("Error Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# График распределения ошибок
plt.figure()
plt.pie(df["Count"], labels=df["ErrorType"], autopct='%1.1f%%')
plt.title("Error Share Distribution")
plt.show()

# Прогноз увеличения числа ошибок при линейном росте нагрузки
growth_rate = 0.1
forecast_steps = 5

forecast_results = {}
for _, row in df.iterrows():
    current = row["Count"]
    forecasts = []
    for _ in range(forecast_steps):
        current = int(current * (1 + growth_rate))
        forecasts.append(current)
    forecast_results[row["ErrorType"]] = forecasts

print(forecast_results)
