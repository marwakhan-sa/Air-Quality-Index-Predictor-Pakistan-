🌿 Pakistan Air Quality Index Predictor
A machine learning web application that predicts the air quality category of locations across Pakistan based on pollutant levels built as part of an AI/ML Bootcamp project.

🌍 Problem Statement
Air pollution is a serious health crisis in Pakistan. Cities like Lahore, Karachi, and Peshawar regularly face dangerous pollution levels. This tool gives everyday people a simple way to check how dangerous their air quality is based on real pollutant data.

🎯 What It Does
Enter pollutant levels (CO, Ozone, NO2, PM2.5) and the app instantly predicts the air quality category from Good to Hazardous along with a health recommendation.
CategoryMeaning🌿 GoodAir is safe for everyone🌤 ModerateAcceptable for most people⚠️ Unhealthy for Sensitive GroupsChildren & elderly should take care😷 UnhealthyEveryone may experience health effects🚨 Very UnhealthyAvoid outdoor activity☠️ HazardousEmergency conditions — stay indoors

📊 Dataset

Source: Global Air Pollution Dataset — Kaggle
Filtered to: 307 Pakistani cities
Features used: CO AQI, Ozone AQI, NO2 AQI, PM2.5 AQI
Target: AQI Category (6 classes)


🛠️ Tech Stack
ToolPurposePythonProgramming languagePandas & NumPyData cleaning & manipulationScikit-learnModel training & evaluationMatplotlib & SeabornData visualizationJoblibSaving & loading the modelStreamlitWeb application UIKaggleDataset & notebook environmentVS CodeLocal development

🧹 Data Cleaning Steps

Removed 427 rows with missing Country values
Removed 1 row with missing City value
Stripped extra whitespace from text columns
Dropped unnecessary AQI category text columns
Label encoded the target column into 6 numeric classes
Filtered dataset to Pakistan only (307 cities)


📈 EDA Highlights

Unhealthy is the most common AQI category across Pakistani cities
PM2.5 has a 0.95 correlation with AQI Value, strongest predictor
Visualizations include: category distribution, AQI histogram, PM2.5 scatter plot, and correlation heatmap


🤖 Model

Algorithm: Random Forest Classifier
Trees: 100 estimators
Train/Test Split: 80% / 20%
Accuracy: 100%


The high accuracy is expected, AQI Category is mathematically derived from pollutant values, and PM2.5 alone has a 0.95 correlation with AQI.


🚀 How to Run Locally
1. Clone the repository
bashgit clone https://github.com/yourusername/pakistan-aqi-predictor.git
cd pakistan-aqi-predictor
2. Install dependencies
bashpip3 install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
3. Run the app
bashstreamlit run app.py
4. Open in browser
http://localhost:8501

📁 Project Structure
pakistan-aqi-predictor/
│
├── data/
│   └── air_pollution.csv         # Filtered Pakistan dataset
├── model/
│   ├── aqi_model.pkl             # Trained Random Forest model
│   └── label_encoder.pkl         # Label encoder for AQI categories
├── notebook/
│   └── eda_cleaning.ipynb        # Data cleaning & EDA notebook
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

📸 App Preview

A green nature-themed UI with interactive sliders for pollutant input and a color-coded result showing the predicted AQI category and health advice.




