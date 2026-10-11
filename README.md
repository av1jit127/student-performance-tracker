# Student Performance Tracker 🎓

An interactive end-to-end Machine Learning web application designed to predict student academic performance (**Math Score**) using demographic indicators, socio-economic factors, and secondary test evaluations.

The application utilizes a scikit-learn preprocessing pipeline paired with an optimized **Linear Regression** model, deployed on **Streamlit Community Cloud**.

---

## 🌐 Live Application
Access the production application directly:  
🔗 **[student--performance--tracker.streamlit.app](https://student--performance--tracker.streamlit.app/)**

---

## 📌 Project Overview
Academic success is influenced by a combination of socio-economic backgrounds, study habits, and test preparedness. This project models student outcomes using statistical learning techniques to identify key contributors to achievement and deliver real-time score estimations.

### Key Highlights
* **Inference Pipeline:** Raw input data is preprocessed via `ColumnTransformer` (One-Hot Encoding for categorical features and Standard Scaling for numeric features) before inference.
* **Trained Estimator:** Employs a fitted `LinearRegression` model achieving ~88% R² score on evaluation splits.
* **Constraint Handling:** Predictions are strictly bounded within the valid academic scoring spectrum ([0, 100]).
* **Zero Cold-Start Lag:** Artifacts are cached using `@st.cache_resource` for low-latency response times.

---

## 📊 Dataset & Feature Breakdown

The dataset examines multiple socio-demographic indicators alongside standardized test scores:

| Feature Name | Type | Categories / Domain | Description |
| :--- | :--- | :--- | :--- |
| **`gender`** | Categorical | `female`, `male` | Biological gender of the student |
| **`race_ethnicity`** | Categorical | `group A` to `group E` | Anonymized ethnic cohort classification |
| **`parental_level_of_education`** | Categorical | 6 distinct levels | Highest education attained by parent(s) |
| **`lunch`** | Categorical | `standard`, `free/reduced` | Socio-economic proxy indicator |
| **`test_preparation_course`** | Categorical | `none`, `completed` | Test preparation course participation |
| **`reading_score`** | Numerical | [0, 100] | Evaluated student reading exam score |
| **`writing_score`** | Numerical | [0, 100] | Evaluated student writing exam score |
| **`math_score`** *(Target)* | Numerical | [0, 100] | Predicted student mathematics score |

---

## ⚙️ Model Architecture & Methodology

```text
[Raw User Input] 
       │
       ▼
[ColumnTransformer]
  ├── OneHotEncoder   ──► (gender, race_ethnicity, parental_level_of_education, lunch, test_prep)
  └── StandardScaler  ──► (reading_score, writing_score)
       │
       ▼
[Linear Regression Model]
       │
       ▼
[Boundary Enforcement: min(max(pred, 0), 100)]
       │
       ▼
[Predicted Math Score Display]
