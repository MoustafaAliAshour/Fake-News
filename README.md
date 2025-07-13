# 📰 Fake News Detection Web App

This is a simple and clean **Fake News Detection** app built using **Python**, **scikit-learn**, and **Streamlit**. The app allows users to input any news article content in English and classify it as **Real** or **Fake** using one of several trained machine learning models.

---

## 📌 Features

- 🔍 Detects Fake or Real news from article text
- 🤖 Choose between four ML models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
- 🧼 Automatic text preprocessing
- 🌐 Web-based interface built with Streamlit

---

## 📁 Project Structure

Fake-News-Detection/

├── Deployment.py

├── fake-news-detection.ipynb

├── news.csv

├── manual_testing.csv

├── models/

│ ├── vectorizer.pkl

│ ├── LR_model.joblib

│ ├── DT_model.joblib

│ ├── RFC_model.joblib

│ └── GBC_model.joblib

---

## Deployment [Streamlit](https://fake-news-9mup3iedw3fcywu53xij7w.streamlit.app/)
---

## 📊 Dataset

The dataset used for training is available here:  
🔗 [Download `news.csv`](https://drive.google.com/file/d/1xb4E-ougFyREgbD3cyGJEPenALIHmY2b/view?usp=drive_link)

It contains labeled news articles with the following fields:
- `title`
- `text`
- `label` (`0` = Fake, `1` = Real)

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/Fake-News-Detection.git
cd Fake-News-Detection
2. Install Requirements

pip install streamlit scikit-learn joblib pandas
3. Download the Dataset
Manually download the dataset and place news.csv in the project directory:
news.csv Download Link

4. Run the App

streamlit run Deployment.py
🧠 Model Training
Model training is handled in fake-news-detection.ipynb, which includes:

Preprocessing using TF-IDF

Model training with Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting

Saving trained models and vectorizer using joblib

import joblib, os
os.makedirs("models", exist_ok=True)
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(log_model, "models/LR_model.joblib")
joblib.dump(dt_model, "models/DT_model.joblib")
joblib.dump(rf_model, "models/RFC_model.joblib")
joblib.dump(gbc_model, "models/GBC_model.joblib")
📃 License
This project is licensed under the MIT License.

✍️ Author
Mostafa Ashour
• [LinkedIn](https://www.linkedin.com/in/moustafa-ashour0/)
• [GitHub](https://github.com/MoustafaAliAshour)

---

## ✅ LinkedIn Post (Updated - English Only)

🚀 **Just Launched: Fake News Detection App!** 📰

I’m excited to share my new project — a **Fake News Detection Web App** built with **Python**, **scikit-learn**, and **Streamlit**!

🔍 The app takes any news article in **English** and classifies it as **Real or Fake** using machine learning. It supports multiple models:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

💡 Key Features:
- Clean English-only interface
- Automatic text preprocessing with TF-IDF
- Trained using `news.csv` dataset
- Fully web-based with no installation needed beyond Python and Streamlit

🧠 Dataset used for training:  
🔗 [Download news.csv](https://drive.google.com/file/d/1xb4E-ougFyREgbD3cyGJEPenALIHmY2b/view?usp=drive_link)

👉 Check it out on GitHub:  
🔗 https://github.com/MoustafaAliAshour/Fake-News

If you're curious about NLP, machine learning, or building apps with Streamlit, feel free to explore or fork the repo!

#Python #MachineLearning #FakeNews #Streamlit #NLP #OpenSource #PortfolioProject #AI
