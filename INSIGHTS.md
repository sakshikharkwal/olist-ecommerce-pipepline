# Insights from Cleaned Olist Data

## Orders Analysis

* **Average Delivery Time**: 11.49 (Calculated from purchase to customer delivery).
* **Proportion of Late Deliveries**: 6.57% of orders delivered after the estimated date.
* **Delivery Delay Distribution**: Histogram of delays.
![Delivery Delay Distribution](visuals/13_delivery_delay_distribution.png)
* **Order Status Analysis**: Distribution of delivered, shipped, canceled, unavailable, etc.
![Order Status Analysis](visuals/14_order_status_analysis.png)
* **Cancellation Rate**: 0.63% of orders canceled.
* **Delivery Performance**: Average actual vs. estimated delivery times.
Average actual delivery time: 11.49 days, Average estimated delivery time: 23.40 days
* **Delivery Performance Categories**: % Delivered Early vs. On Time vs. Late.
![Delivery Performance Categories](visuals/15_delivery_performance.png)
* **Median vs. Mean Delivery Delay**: Mean Delivery Delay: -12.09 days, Median Delivery Delay: -12.00 days.

## Payments Analysis

* **Payment Type Distribution**: Distribution of various payment types like Credit card, boleto, etc.
![Payment Type Distribution](visuals/16_payment_type_distribution.png)
* **Installments vs. Payment Value**: Average payment value across installment counts.
![Installments vs. Payment Value](visuals/17_installments_vs_payment.png)

## Reviews Analysis

* **Review Sentiments**: Positive: 77.068048, Negative: 14.688987, Neutral: 8.242965
* **Review Score Distribution**: % of reviews that are 1, 2, 3, 4, 5.
![Review Score Distribution](visuals/18_review_scores_distribution.png)

## Cross Analysis (Payments × Reviews)

* **Reviews Timing Distribution**: Distribution of time lag between purchase and review creation.
![Reviews Timing Distribution](visuals/19_review_delays_distribution.png)
* **Installments vs. Reviews**: Whether customers paying in more installments leave lower scores.
![Installments vs. Reviews](visuals/20_installments_vs_review_score.png)