import numpy as np
import pandas as pd
from scipy.stats import pearsonr

def bootstrap_difference(y_true, y_pred_A, y_pred_B, metric='pearson', B=1000, seed=10, redistribution=False):
    """
    Compute the bootstrapped 95% confidence interval of the difference
    between model A and model B on a given metric.
    
    Parameters:
        y_true     : np.array of ground truth scores
        y_pred_A   : np.array of predictions from model A
        y_pred_B   : np.array of predictions from model B
        metric     : 'pearson' or 'mae'
        B          : number of bootstrap samples
        seed       : random seed for reproducibility
        
    Returns:
        (lower_bound, upper_bound), mean_diff, all_diffs
    """
    if seed:
        np.random.seed(seed)

    y_true = np.asarray(y_true)
    y_pred_A = np.asarray(y_pred_A)
    y_pred_B = np.asarray(y_pred_B)
    n = len(y_true)
    diffs = []
    s_a, s_b = 0, 0

    for _ in range(B):
        indices = np.random.choice(n, n, replace=True)

        yt = y_true[indices]
        a  = y_pred_A[indices]
        b  = y_pred_B[indices]

        if redistribution:
            mean_true = np.mean(yt)
            std_true = np.std(yt)

            mean_pred_a = np.mean(a)
            std_pred_a = np.std(a)

            mean_pred_b = np.mean(b)
            std_pred_b = np.std(b)

            a_2, b_2 = [], []

            for t in a:
                k = (((t - mean_pred_a) / std_pred_a) * std_true) + mean_true
                #kk = (k/ 2.0)**2 - (3.0 / 8.0)
                a_2.append(k)

            for p in b:
                k = (((p - mean_pred_b) / std_pred_b) * std_true) + mean_true
                #kk = (k/ 2.0)**2 - (3.0 / 8.0)
                b_2.append(k)

            a_2 = np.clip(a_2, np.min(yt), np.max(yt))
            b_2 = np.clip(b_2, np.min(yt), np.max(yt))

            a = a_2
            b = b_2

        if metric == 'pearson':
            stat_A = pearsonr(yt, a)[0]
            s_a += stat_A
            stat_B = pearsonr(yt, b)[0]
            s_b += stat_B
        elif metric == 'mae':
            stat_A = np.mean(np.abs(yt - a))
            stat_B = np.mean(np.abs(yt - b))
        else:
            raise ValueError("Metric must be 'pearson' or 'mae'")

        diffs.append(stat_A - stat_B)

    diffs = np.array(diffs)
    lower = np.percentile(diffs, 2.5)
    upper = np.percentile(diffs, 97.5)
    mean_diff = np.mean(diffs)

    return (lower, upper), mean_diff, diffs


csv_file = "/home/pkaliosis/zero-shot/tr_pcl_ans.csv"
scores_file_A = "/home/pkaliosis/zero-shot/scores/correct_scores_meta-llama70-1_direct_fs_alt.csv"
scores_file_B = "/home/pkaliosis/zero-shot/scores/correct_scores_meta-llama70-1_direct_fs_alt_all.csv"
#scores_file_B = "/home/pkaliosis/zero-shot/roberta_tr.csv"

# === Load main data ===
df = pd.read_csv(csv_file)
df["video_id"] = df["video_id"].astype(str)

# === Load Model A predictions ===
df_A = pd.read_csv(scores_file_A)
df_A["video_id"] = df_A["video_id"].astype(str).str.split("_").str[0]
df_A = df_A.rename(columns={"PTSD_Score": "pred_A"})

# === Load Model B predictions ===
df_B = pd.read_csv(scores_file_B)
df_B["video_id"] = df_B["video_id"].astype(str).str.split("_").str[0]
df_B = df_B.rename(columns={"PTSD_Score": "pred_B"})

# === Merge everything ===
df_all = df.merge(df_A[["video_id", "pred_A"]], on="video_id")
df_all = df_all.merge(df_B[["video_id", "pred_B"]], on="video_id")

# Clean
df_all = df_all.dropna(subset=["PCL_SCORE", "pred_A", "pred_B"])
df_all = df_all[(df_all["pred_A"] != -34) & (df_all["pred_B"] != -34)]

# Convert types
df_all["PCL_SCORE"] = df_all["PCL_SCORE"].astype(float)
df_all["pred_A"] = df_all["pred_A"].astype(float)
df_all["pred_B"] = df_all["pred_B"].astype(float)

print(df_all.head())

# === Run bootstrap comparison ===
ci_pearson, mean_diff_pearson, _ = bootstrap_difference(
    df_all["PCL_SCORE"], df_all["pred_A"], df_all["pred_B"], metric="pearson", redistribution=True
)

ci_mae, mean_diff_mae, _ = bootstrap_difference(
    df_all["PCL_SCORE"], df_all["pred_A"], df_all["pred_B"], metric="mae", redistribution=True
)

# === Print results ===
print("Bootstrap Results:")
print(f"\nPearson r difference: {mean_diff_pearson:.4f}")
print(f"95% CI: [{ci_pearson[0]:.4f}, {ci_pearson[1]:.4f}]")
print("→ Significant" if ci_pearson[0] > 0 or ci_pearson[1] < 0 else "→ Not significant")

if ci_pearson[0] > 0 or ci_pearson[1] < 0:
    if ci_pearson[0] > 0:
        print("For Pearson: wo cues outperforms w cues SIGNIFICANTLY")
    elif ci_pearson[1] < 0:
        print("For Pearson: w cues outperforms wo cues SIGNIFICANTLY")

print(f"\nMAE difference: {mean_diff_mae:.4f}")
print(f"95% CI: [{ci_mae[0]:.4f}, {ci_mae[1]:.4f}]")
print("→ Significant" if ci_mae[0] > 0 or ci_mae[1] < 0 else "→ Not significant")
if ci_mae[0] > 0 or ci_mae[1] < 0:
    if ci_mae[1] < 0:
        print("For MAE: wo cues outperforms w cues SIGNIFICANTLY")
    elif ci_mae[0] > 0:
        print("For MAE: w cues outperforms wo cues SIGNIFICANTLY")