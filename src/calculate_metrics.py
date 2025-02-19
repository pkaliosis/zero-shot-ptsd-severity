import pandas as pd
import pickle
import numpy as np
from scipy.stats import pearsonr
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load CSV file
csv_file = "/home/pkaliosis1/deepseek-ptsd/gpt4-depression-schema/data/tr_pcl_ans.csv"  # Replace with your actual CSV filename
df = pd.read_csv(csv_file)

# Convert video_id in CSV to string
df["video_id"] = df["video_id"].astype(str)


# Load pickle file
pickle_file = "/home/pkaliosis1/deepseek-ptsd/gpt4-depression-schema/out/expts/responses/qwen_w_reasoning_wo_defs_wo_questions_scores.pkl" #e with your actual pickle filename
with open(pickle_file, "rb") as f:
    predicted_dict = pickle.load(f)

keys = list(predicted_dict.keys())
keys = [str(k.split("_")[0]) for k in keys]

processed_dict = {key.split("_")[0]: value for key, value in predicted_dict.items()}

# Extract true and predicted values for PCL_SCORE
df = df[df["video_id"].isin(keys)]  # Keep only relevant rows
df["predicted_PCL_SCORE"] = df["video_id"].map(processed_dict)

# Drop rows where prediction is missing (optional)
df = df.dropna(subset=["PCL_SCORE", "predicted_PCL_SCORE"])

# Convert columns to float to avoid errors
df["PCL_SCORE"] = df["PCL_SCORE"].astype(float)
df["predicted_PCL_SCORE"] = df["predicted_PCL_SCORE"].astype(float)

print(df)

# Extract true and predicted scores
true_values = df["PCL_SCORE"].values
predicted_values = df["predicted_PCL_SCORE"].values

print("mean true:", np.mean(true_values))
print("median true:", np.median(true_values))
print("mean pred:", np.mean(predicted_values))
print("median pred:", np.median(predicted_values))


print("len true values:", len(true_values))
print("len pred values:", len(predicted_values))

# Compute metrics
pearson_r, _ = pearsonr(true_values, predicted_values)
mae = mean_absolute_error(true_values, predicted_values)
rmse = np.sqrt(mean_squared_error(true_values, predicted_values))

# Print results
print(f"Pearson's r: {pearson_r:.4f}")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")