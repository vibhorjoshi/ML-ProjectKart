# Medical Insurance Cost Prediction Model

This repository contains the Jupyter Notebook and related documentation for the **Medical Insurance Cost Prediction** project. The objective is to predict medical insurance costs based on various factors such as age, sex, BMI, number of children, smoking status, and region.

## Contents

- **MedicalInsuranceCostPrediction.ipynb**: The main Jupyter Notebook implementing the prediction model, structured as follows:
  - **Importing necessary libraries**: Includes essential libraries like NumPy, Pandas, Matplotlib, Seaborn, Plotly, Scikit-learn, XGBoost, and Imbalanced-learn.
  - **Loading the dataset**: Reads the dataset (`Insurance.csv`) into a Pandas DataFrame.
  - **Data cleaning and preprocessing**: Handles missing values and converts categorical variables into numerical format using Label Encoding.
  - **Exploratory Data Analysis (EDA)**: Utilizes visualization techniques to understand feature distributions and relationships.
  - **Feature Engineering**: Encodes categorical variables (`sex`, `smoker`, `region`) into numerical values.
  - **Model training using multiple algorithms**: Splits data into training and testing sets and evaluates different machine learning models.
  - **Model evaluation**: Computes RMSE (Root Mean Squared Error) to assess model performance.

## Algorithms Used

The project explores multiple machine learning algorithms for predicting insurance costs:
- **XGBoost Regressor**: Main model used for prediction due to its efficiency and accuracy.
- **Random Forest Regressor**: Used as an alternative ensemble learning approach.
- **Linear Regression**: Baseline model for comparison.
- **Decision Tree Regressor**: Tested for interpretability.

## Usage

Follow these steps to use the model:

1. **Install required dependencies**:
   ```sh
   pip install numpy pandas matplotlib seaborn plotly scikit-learn xgboost imbalanced-learn
   ```

2. **Open the Jupyter Notebook**:
   - Launch `MedicalInsuranceCostPrediction.ipynb` in Jupyter Notebook.

3. **Run the notebook**:
   - Execute the cells sequentially to load data, preprocess it, train the model, and generate predictions.

## Dependencies

- Python 3.x
- Jupyter Notebook
- Libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `plotly`, `scikit-learn`, `xgboost`, `imbalanced-learn`

## Author

- **Harshit Seth**
- Email: harshitseth@hotmail.com
- GitHub: [HarshitSeth77](https://github.com/HarshitSeth77)
- LinkedIn: [Harshit Seth](https://www.linkedin.com/in/harshitseth77/)

## Conclusion

This project demonstrates a machine learning approach to predicting medical insurance costs. The steps outlined in the notebook guide users through data preprocessing, exploratory data analysis, model training, and evaluation. The final model provides accurate cost predictions based on user input, aiding individuals and organizations in estimating insurance expenses effectively.

