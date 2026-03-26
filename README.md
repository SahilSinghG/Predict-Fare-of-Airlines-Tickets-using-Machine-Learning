# ✈️ Airline Fare Prediction Using Machine Learning

## 📌 Project Overview

Airline ticket prices fluctuate significantly due to various factors such as airline company, travel route, number of stops, departure time, and the number of days left before departure. Predicting these prices can help travelers make informed decisions and assist airline companies in dynamic pricing strategies.

The goal of this project is to build a machine learning model that predicts airline ticket prices based on historical flight data. The model learns patterns from the dataset and estimates the likely price of a flight based on user-provided input.

This project demonstrates the complete machine learning lifecycle, including:

Data preprocessing
Exploratory Data Analysis (EDA)
Feature engineering
Model training
Model evaluation
Deployment using Streamlit

The final result is an interactive web application where users can input flight details and receive an estimated ticket price.

## 📂 Project Structure

<img width="768" height="536" alt="image" src="https://github.com/user-attachments/assets/c06d7f30-ffe0-4349-a016-bf5aeb77775e" />

## 📊 Dataset Description

The dataset used in this project contains historical flight booking data. Each row represents a flight with multiple attributes affecting ticket prices.

Dataset Features
Feature	Description
airline	Airline company operating the flight
source_city	City where the flight departs
departure_time	Time category of flight departure
stops	Number of stops during the journey
arrival_time	Time category of arrival
destination_city	Destination city
class	Travel class (Economy / Business)
duration	Total flight duration
days_left	Number of days left before departure
price	Ticket price (target variable)

## 🎯 Problem Statement

Airline companies use dynamic pricing models, meaning ticket prices change depending on several factors such as:

Travel demand
Booking time
Airline company
Route popularity
Class of travel

<img width="806" height="747" alt="image" src="https://github.com/user-attachments/assets/e01551ff-9324-4848-8f0c-4ad1bdd0e9d2" />


The objective of this project is to build a regression model that predicts the flight ticket price based on available features.

## 🧠 Machine Learning Approach

This project follows a standard machine learning workflow.

1️⃣ Data Loading

The dataset was first loaded into a Pandas DataFrame for analysis and preprocessing.

df = pd.read_csv("Clean_Dataset.csv")

<img width="862" height="468" alt="image" src="https://github.com/user-attachments/assets/17647973-f630-4c24-a274-9389b8f5945e" />

2️⃣ Data Cleaning

During preprocessing:

Removed unnecessary columns
Checked for missing values
Ensured data types were correct

The flight column was removed because it only represents a flight identifier and does not contribute meaningful predictive information.

<img width="580" height="363" alt="image" src="https://github.com/user-attachments/assets/ba2fc9ee-cf01-4adf-86b8-ee3d6f44fbc8" />


3️⃣ Exploratory Data Analysis (EDA)

Exploratory analysis was performed to understand relationships between features and ticket prices.

Key visualizations included:

Airline vs Price distribution

<img width="906" height="538" alt="image" src="https://github.com/user-attachments/assets/0cab89ac-c967-4e97-99a5-bec4de639632" />

Stops vs Price

<img width="823" height="427" alt="image" src="https://github.com/user-attachments/assets/f028f624-0fd2-4411-8b2d-1cdfd6081ed9" />

Price distribution histogram

<img width="893" height="512" alt="image" src="https://github.com/user-attachments/assets/0fbbd395-250a-4e0e-b2df-8de1d33fcaff" />

Correlation heatmap

<img width="865" height="581" alt="image" src="https://github.com/user-attachments/assets/be6461e3-38f5-48c7-a6da-4ab260f17a50" />

These visualizations helped identify the most influential features affecting ticket prices.

4️⃣ Feature Encoding

Machine learning models require numerical inputs. Since several features were categorical (such as airline, city, and travel class), Label Encoding was used to convert them into numerical form.

Example:

Airline	Encoded Value
AirAsia	0
Air India	1
GO FIRST	2
Indigo	3
SpiceJet	4
Vistara	5

This step ensures the machine learning algorithm can process categorical information.

5️⃣ Train-Test Split

The dataset was split into:

Training Data (80%) – used to train the model
Testing Data (20%) – used to evaluate performance
train_test_split(X, y, test_size=0.2)

This ensures the model can generalize to unseen data.

## 🤖 Model Selection

Several regression algorithms were considered, including:

Linear Regression
Decision Tree
Random Forest

<img width="611" height="563" alt="image" src="https://github.com/user-attachments/assets/e0135eb7-0d32-46db-97d4-a4d95979a7a2" />

After comparing performance, Random Forest Regressor was selected because it handles nonlinear relationships effectively and provides strong predictive accuracy.

Why Random Forest?

<img width="770" height="641" alt="image" src="https://github.com/user-attachments/assets/8ac0eea2-bb48-4af6-a597-fcdbaf960ab7" />

Random Forest works by:

Creating multiple decision trees
Training each tree on different subsets of data
Combining predictions from all trees

This approach reduces overfitting and improves prediction accuracy.

## 📈 Model Performance

Model evaluation metrics used:

R² Score

Measures how well the model explains the variance in ticket prices.

R² Score ≈ 0.98

This means 98% of the price variability is explained by the model.

RMSE (Root Mean Squared Error)
RMSE ≈ 2781

RMSE represents the average prediction error.

For example, if the real ticket price is:

₹5900

The model might predict within approximately:

₹5900 ± ₹2781

This level of error is expected in airline pricing because real prices depend on dynamic factors such as demand and promotions.

## 🌐 Deployment

To make the model accessible to users, it was deployed using Streamlit, a Python framework for building data applications.

The Streamlit web app allows users to input flight details such as:

Airline
Source city
Destination city
Number of stops
Travel class
Duration
Days before departure

The model then predicts the estimated ticket price.

<img width="557" height="653" alt="image" src="https://github.com/user-attachments/assets/1d7735db-ee2c-407c-9d3c-29e1bf6af09e" />


## 🚀 How to Run the Project

Clone the repository
git clone https://github.com/SahilSinghG/Predict-Fare-of-Airlines-Tickets-using-Machine-Learning.git

Install dependencies
pip install -r requirements.txt

Run the Streamlit application
streamlit run app.py

The web interface will open in your browser.

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit

## 📌 Key Learnings

Through this project I gained hands-on experience with:

Data preprocessing techniques
Feature encoding
Exploratory data analysis
Regression modeling
Model evaluation
Building interactive ML applications
Deploying machine learning models

## 📊 Future Improvements

Possible enhancements include:

Using advanced algorithms such as XGBoost or Gradient Boosting
Hyperparameter tuning for improved performance
Adding additional features such as weekday/weekend indicators
Deploying the model using FastAPI or Docker

👨‍💻 Author

Sahil Singh

Data Science & Machine Learning Enthusiast

GitHub:
https://github.com/SahilSinghG
