Student Performance Tracker 🎓An interactive end-to-end Machine Learning web application designed to predict student academic performance (Math Score) using demographic indicators, socio-economic factors, and secondary test evaluations.The application utilizes a scikit-learn preprocessing pipeline paired with an optimized Linear Regression model, deployed on Streamlit Community Cloud.🌐 Live ApplicationAccess the production application directly:🔗 student--performance--tracker.streamlit.app📌 Project OverviewAcademic success is influenced by a combination of socio-economic backgrounds, study habits, and test preparedness. This project models student outcomes using statistical learning techniques to identify key contributors to achievement and deliver real-time score estimations.Key HighlightsInference Pipeline: Raw input data is preprocessed via ColumnTransformer (One-Hot Encoding for categorical features and Standard Scaling for numeric features) before inference.Trained Estimator: Employs a fitted LinearRegression model achieving ~88% $R^2$ score on evaluation splits.Constraint Handling: Predictions are strictly bounded within the valid academic scoring spectrum ($[0, 100]$).Zero Cold-Start Lag: Artifacts are cached using @st.cache_resource for low-latency response times.📊 Dataset & Feature BreakdownThe dataset examines multiple socio-demographic indicators alongside standardized test scores:Feature NameTypeCategories / DomainDescriptiongenderCategoricalfemale, maleBiological gender of the studentrace_ethnicityCategoricalgroup A to group EAnonymized ethnic cohort classificationparental_level_of_educationCategorical6 distinct levelsHighest education attained by parent(s)lunchCategoricalstandard, free/reducedSocio-economic proxy indicatortest_preparation_courseCategoricalnone, completedTest preparation course participationreading_scoreNumerical$[0, 100]$Evaluated student reading exam scorewriting_scoreNumerical$[0, 100]$Evaluated student writing exam scoremath_score (Target)Numerical$[0, 100]$Predicted student mathematics score⚙️ Model Architecture & Methodology[Raw User Input] 
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
Exploratory Data Analysis (EDA): Analyzed score distributions, variance, skewness, and inter-feature correlations.Data Transformation:Categorical features mapped to dense indicator vectors using OneHotEncoder(drop='first').Continuous variables centered and scaled to unit variance using StandardScaler.Model Selection: Benchmarked against Ridge, Lasso, Random Forest, AdaBoost, CatBoost, and XGBoost regressors; standard Linear Regression provided high stability and interpretability with an $R^2$ score exceeding $0.88$.Serialization: Decoupled transformation and inference logic into two separate serialized files (preprocessor.pkl and model.pkl) for modularity.🗂️ Repository StructurePlaintextstudent-performance-tracker/
├── app.py                # Streamlit front-end UI and scoring logic
├── model.pkl             # Trained Linear Regression model artifact
├── preprocessor.pkl      # Fitted ColumnTransformer preprocessing artifact
├── requirements.txt      # Production runtime dependencies
├── .python-version       # Environment configuration pinning Python runtime
└── README.md             # Project documentation and specifications
🚀 Deployment & Cloud Environment ConfigurationThe application is deployed on Streamlit Community Cloud. To avoid binary serialization incompatibilities when unpickling scikit-learn objects, specific environment pins are established:Runtime Version: Python 3.11 (enforced via .python-version)Scikit-Learn Version: 1.6.1 (enforced via requirements.txt to match the exact pickle serialization schema)Dependency Resolver: Explicit pinned packages prevent unpickling issues like _RemainderColsList attribute errors.🛠️ Tech StackLanguage: PythonData Processing & Analytics: Pandas, NumPyMachine Learning Framework: Scikit-LearnApplication Framework: StreamlitDeployment Platform: Streamlit Community CloudVersion Control: Git, GitHub
