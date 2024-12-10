# E-commerce Sales Analysis Dashboard

## Overview
Interactive Power BI dashboard analyzing sales data across different markets, focusing on customer behavior and product performance. Built using Brazilian E-commerce dataset from Olist.

## Key Features
- **Multi-market Analysis**: Performance tracking across 5 countries (DE, FR, IT, UK, USA)
- **Category Performance**: Detailed analysis of 5 product categories
- **Customer Behavior**: Purchase patterns and customer segmentation
- **Interactive Elements**: Dynamic filtering and drill-down capabilities

## Dashboard Pages

### 1. Overview
Key performance metrics and high-level insights
![Overview Dashboard](./docs/screenshots/overview.png)

### 2. Sales Analysis by Country
Detailed breakdown of sales performance by market
![Sales Analysis](./docs/screenshots/sales_analysis.png)

### 3. Purchase Patterns
Customer behavior analysis and category combinations
![Purchase Patterns](./docs/screenshots/purchase_patterns.png)

### 4. Key Findings
Comprehensive insights and analysis
![Key Findings](./docs/screenshots/key_findings.png)

## Key Insights
- UK leads market share (22.68%) with €1.48M in sales
- Home + Clothing dominate product categories (47% of revenue)
- 5.02 average orders per customer
- 8.98% Month-over-Month growth
- Weekend sales show 15% higher volume

## Technical Setup

### Prerequisites
- Power BI Desktop
- Python 3.x
- Required Python packages: pandas, numpy

### Installation
1. Clone the repository
```bash
git clone [repository-url]
```

2. Run data preparation script
```bash
python src/data_preparation.py
```

3. Open dashboard in Power BI Desktop
```
src/ecommerce_dashboard.pbix
```

## Data Source
[Brazilian E-commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Project Structure
```
PowerBI-Ecommerce-Analysis/
├── src/
│   ├── data_preparation.py
│   └── ecommerce_dashboard.pbix
├── data/
│   ├── raw/
│   │   ├── sales_data.csv
│   │   ├── customer_data.csv
│   │   └── product_data.csv
│   └── processed/
│       └── prepared_ecommerce_data.csv
├── docs/
│   ├── screenshots/
│   │   ├── overview.png
│   │   ├── sales_analysis.png
│   │   ├── purchase_patterns.png
│   │   └── key_findings.png
│   └── metadata.md
└── README.md
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```

