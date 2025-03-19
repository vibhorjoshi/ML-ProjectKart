# Supply Chain Demand Forecasting

## GOAL
The main goal of this project is to build a robust demand forecasting model using a hybrid LSTM-Transformer architecture. The purpose is to predict future sales quantities, helping optimize inventory levels, reduce stockouts, and enhance customer satisfaction.

## DATASET
- **Dataset Name:** Amazon Sales Report
- **Source:** Kaggle
- **Link:** [Dataset](https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data/data)

## DESCRIPTION
This project focuses on predicting future product demand by leveraging historical sales data. The LSTM-Transformer model combines the sequential learning capabilities of LSTM with the self-attention mechanism of Transformers, allowing for accurate long-term predictions. The output is a time series forecast of future sales quantities.

## MODELS USED

### 1. SARIMAX (Seasonal ARIMA with Exogenous Regressors)
SARIMAX is a statistical model that captures seasonality and trends in time series data. It is effective for data with strong seasonal patterns but struggles with complex non-linear relationships.

### 2. XGBoost (Extreme Gradient Boosting)
XGBoost is a powerful tree-based ensemble learning method that is widely used for structured data. It provides fast and accurate predictions but lacks the ability to model long-term temporal dependencies effectively.

### 3. LSTM-Transformer (Long Short-Term Memory with Transformer Mechanism)
LSTM-Transformer combines the strengths of LSTMs (which handle sequential dependencies) and Transformers (which capture long-range dependencies). This hybrid model is particularly useful for time series forecasting as it adapts well to changing trends and complex relationships in demand patterns.

## WHY LSTM-TRANSFORMER IS BETTER
- **Captures Long-Term Dependencies:** Unlike SARIMAX and XGBoost, LSTM-Transformer can learn long-term patterns in time series data.
- **Handles Non-Linearity:** LSTM-Transformer excels at capturing complex relationships between past and future demand.
- **Robust to Seasonality Changes:** While SARIMAX relies on predefined seasonality, LSTM-Transformer dynamically learns patterns, making it more adaptive.
- **Scalable to Large Datasets:** Traditional methods struggle with high-dimensional data, whereas deep learning models like LSTM-Transformer perform well on large datasets.

## WHAT I HAD DONE
1. **Data Preprocessing:**
   - Loaded and cleaned sales data, keeping only 'Shipped' orders.
   - Aggregated quantities sold by date.
   - Normalized data using MinMaxScaler.
2. **Dataset Preparation:**
   - Created time series sequences with a sequence length of 30 days.
   - Used PyTorch DataLoader to efficiently handle batches.
3. **Model Building:**
   - Developed a combined LSTM-Transformer model:
     - LSTM to capture temporal dependencies.
     - Transformer to capture long-range relationships.
4. **Training:**
   - Used MSE Loss function and Adam optimizer.
   - Implemented learning rate scheduling to adjust learning rate dynamically.
5. **Prediction:**
   - Generated rolling forecasts for the next 30 days.
   - Applied simple moving average (SMA) for smoother predictions.
6. **Visualization:**
   - Plotted historical data and future predictions for visual inspection.

## INSTALLATION & USAGE
```sh
pip install -r requirements.txt
python supply_chain_demand_forecasting.py
```

## RESULTS
The model comparison showed that LSTM-Transformer outperformed SARIMAX and XGBoost in forecasting accuracy, particularly for longer forecasting windows.

## ACCURACIES
- **LSTM-Transformer Model:** The evaluation metric used was MSE Loss, progressively reduced over epochs.
- [Add MSE or RMSE values once finalized.]

## CONCLUSION
The LSTM-Transformer model effectively predicts future sales demand by combining the strengths of LSTM's sequential learning and Transformer's attention mechanism. The model shows promising results in forecasting, and further tuning can enhance accuracy. These forecasts can be utilized to optimize supply chain processes and maintain healthy stock levels.

## LICENSE
This project is open-source and available under the MIT License.

---

**T Aditya**  
Github: [mikeyzgoat](https://github.com/mikeyzgoat)