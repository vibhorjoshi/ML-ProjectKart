## Supply Chain Demand Forecasting

### GOAL
The main goal of this project is to build a robust demand forecasting model using a hybrid LSTM-Transformer architecture. The purpose is to predict future sales quantities, helping optimize inventory levels, reduce stockouts, and enhance customer satisfaction.

### DATASET
- **Dataset Name:** : Amazon Sales Report
- **Source:** : Kaggle
- **Link:** : [Dataset](https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data/data)

### DESCRIPTION
This project focuses on predicting future product demand by leveraging historical sales data. The LSTM-Transformer model combines the sequential learning capabilities of LSTM with the self-attention mechanism of Transformers, allowing for accurate long-term predictions. The output is a time series forecast of future sales quantities.

### WHAT I HAD DONE
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

### MODELS USED
- **LSTM (Long Short-Term Memory):** Captures short and long-term dependencies in sequential data.
- **Transformer:** Employs self-attention to model relationships between data points, enhancing long-range forecasting.

**Why these models?**
- LSTM is great for handling sequential time series data.
- Transformer complements it by capturing complex dependencies and reducing error propagation.

### LIBRARIES NEEDED
- **Pandas** for data manipulation.
- **NumPy** for numerical operations.
- **Matplotlib** for data visualization.
- **Sklearn (MinMaxScaler)** for data normalization.
- **Torch (PyTorch):**
  - **nn** for defining neural networks.
  - **optim** for optimization algorithms.
  - **DataLoader** for batch processing.

### ACCURACIES
- **LSTM-Transformer Model:** The evaluation metric used was MSE Loss, progressively reduced over epochs.
- [Add MSE or RMSE values once finalized.]

### CONCLUSION
The LSTM-Transformer model effectively predicts future sales demand by combining the strengths of LSTM's sequential learning and Transformer's attention mechanism. The model shows promising results in forecasting, and further tuning can enhance accuracy. These forecasts can be utilized to optimize supply chain processes and maintain healthy stock levels.

---

**T Aditya** 
Github: [mikeyzgoat](https://github.com/mikeyzgoat)

