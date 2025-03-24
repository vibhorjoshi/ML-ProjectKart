# Medical Insurance Cost Prediction Model

This folder contains the Jupyter Notebook and related documentation for the Medical Insurance Cost Prediction project. The primary goal of this project is to predict the medical insurance costs based on various factors such as age, sex, BMI, number of children, smoking status, and region.

## Contents

- **insurance.ipynb**: This Jupyter Notebook implements the medical insurance cost prediction model. It includes the following sections:
  - Importing necessary libraries: This section imports all the required libraries for data manipulation, visualization, and model building.
  - Loading the dataset: This section loads the dataset from a CSV file into a pandas DataFrame.
  - Data cleaning and preprocessing: This section handles missing values, data type conversions, and other preprocessing steps to prepare the data for analysis.
  - Exploratory Data Analysis (EDA): This section performs various data visualization techniques to understand the distribution and relationships within the data.
  - Converting categorical variables into numerical format: This section converts categorical variables into numerical format using techniques like label encoding.
  - Model training using Random Forest Regressor: This section splits the data into training and testing sets and trains a Random Forest Regressor model.
  - Making predictions based on user input: This section allows users to input their parameters and get the predicted insurance cost.


## Usage

To use the model, follow these steps:

1. Ensure you have the required dependencies installed. You can install them using pip:
   ```
   pip install numpy pandas matplotlib seaborn plotly scikit-learn xgboost imbalanced-learn
   ```

2. Open the `insurance.ipynb` file in Jupyter Notebook.

3. Run the cells sequentially to execute the model. You can input your parameters when prompted to get the predicted insurance cost.

## Dependencies

- Python 3.x
- Jupyter Notebook
- Libraries: numpy, pandas, matplotlib, seaborn, plotly, scikit-learn, xgboost, imbalanced-learn

## Author

- Harshit Seth
- Email: harshitseth@hotmail.com
- GitHub: [HarshitSeth77](https://github.com/HarshitSeth77)
- LinkedIn: [Harshit Seth](https://www.linkedin.com/in/harshitseth77/)

## Conclusion

This project provides a comprehensive approach to predicting medical insurance costs using machine learning techniques. By following the steps outlined in the Jupyter Notebook, users can understand the data preprocessing, exploratory data analysis, and model training processes. The model can be used to make accurate predictions based on user input, helping individuals and organizations estimate insurance costs effectively.