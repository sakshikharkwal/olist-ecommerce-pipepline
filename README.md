# Olist E-commerce Data Pipeline

This project processes, cleans, and analyzes the Olist Brazilian E-commerce dataset.  
It demonstrates a full data pipeline: raw → processed → insights, with modular utilities and reproducible steps.

---

## Project Structure

```

.
├── data
│   ├── raw/          # Original untouched datasets
│   ├── processed/    # Cleaned & transformed datasets (gitignored)
│   └── interim/      # Temporary files (gitignored)
├── notebooks/        # Jupyter notebooks for exploration
├── utils/            # Custom utility scripts (cleaning, transforms, etc.)
├── visuals/          # Generated charts and plots
├── INSIGHTS.md       # Key insights & visuals summary
├── README.md         # Project documentation
├── requirements.txt  # Project dependencies
├── .gitignore        # Ignore unnecessary files
└── LICENSE           # License file

````

---

## Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/olist-ecommerce-pipeline.git
cd olist-ecommerce-pipeline
pip install -r requirements.txt
````

---

## Data Pipeline

1. **Raw Data** → Stored in `data/raw`
2. **Cleaning & Preprocessing**

   * Handling missing values
   * Normalization & scaling (for ML)
   * Log transformations for skewed features
   * Export to `data/processed`
3. **Analysis & Visualizations**

   * Orders, payments, and reviews insights
   * Plots stored in `visuals/`
   * Summary written in `INSIGHTS.md`

---

## Insights Overview

Detailed results are in [INSIGHTS.md](INSIGHTS.md).
Highlights include:

* Average delivery time & delay analysis
* % of early vs. on-time vs. late deliveries
* Order status distribution & cancellation rate
* Payment method usage & installments vs. value
* Review score distribution & review timing
* Cross-analysis: payments vs. reviews

---

## Visuals

Example:

```
![Delivery Performance](visuals/06_delivery_performance.png)
```

---

## Tools Used

* Python (pandas, numpy, matplotlib, seaborn, scikit-learn)
* Jupyter Notebook
* Git & GitHub for version control

---

## License

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.