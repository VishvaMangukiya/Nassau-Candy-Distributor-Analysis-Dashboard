# Nassau-Candy-Distributor-Analysis-Dashboard

# 📊 Product Profitability Dashboard (Streamlit)

## 🚀 Project Overview
This project is an interactive data analytics dashboard built using Streamlit, Pandas, and Plotly to analyze product-level profitability for a distribution business.

The dashboard provides real-time business insights into sales, cost, profit, and margins, helping stakeholders make data-driven decisions.

---

## 🎯 Objective
The main goal of this project is to:
- Analyze product profitability
- Identify high-performing and risky products
- Understand profit contribution across divisions
- Apply Pareto analysis (80/20 rule) for decision-making

---

## 📂 Dataset
The dataset used:
- Nassau Candy Distributor dataset
- Contains:
  - Product Name
  - Division
  - Sales
  - Cost

---

## 🛠️ Tech Stack
- Python  
- Streamlit → Web app framework  
- Pandas → Data cleaning & transformation  
- Plotly Express → Interactive visualizations  

---

## ⚙️ Key Features

### 🔹 1. Data Cleaning & Preparation
- Removed missing values  
- Filtered invalid sales (Sales > 0)  
- Created new metrics:
  - Profit = Sales - Cost  
  - Profit Margin (%)  

---

### 🔹 2. Interactive Filters
Users can dynamically filter data using:
- Division selection  
- Product search  
- Minimum profit margin slider  

---

### 🔹 3. KPI Dashboard
Displays key business metrics:
- 💰 Total Sales  
- 📈 Total Profit  
- 📊 Average Profit Margin  
- 📦 Total Products  

---

### 🔹 4. Visual Analytics

#### 📌 Top Products
- Shows top 10 products based on profit  

#### 📌 Division Performance
- Compares Sales vs Profit across divisions  

#### 📌 Margin Leaderboard
- Highlights most profitable products by margin  

#### 📌 Scatter Analysis
- Sales vs Profit  
- Cost vs Sales  

#### 📌 Margin Distribution
- Histogram of profit margins  

---

### 🔹 5. Pareto Analysis (80/20 Rule)
- Identifies top 20% products contributing to majority of profit  
- Calculates profit dependency  

---

### 🔹 6. Business Insights Sections

#### ⚠️ High Sales but Low Profit
- Identifies products generating revenue but low profit  

#### 🚨 Margin Risk Products
- Products with low profit margin (<10%)  

#### 📊 Profit Dependency Indicator
- Shows reliance on top-performing products  

---

### 🔹 7. Automated Insights
Generates smart insights like:
- Number of high-profit products  
- Low-margin product count  
- Profit concentration (Pareto insight)  

---

## 🎨 UI/UX Highlights
- Modern gradient-based design  
- Interactive KPI cards with hover effects  
- Clean sidebar filters  
- Responsive layout using Streamlit columns  

---

## 📈 Key Business Insights Delivered
This dashboard helps answer:
- Which products generate the most profit?  
- Which products are risky despite high sales?  
- How much profit depends on top products?  
- Which divisions perform best?  

---

## ▶️ How to Run the Project

pip install streamlit pandas plotly  
streamlit run app.py  

---

## 💡 Conclusion
This project demonstrates:
- Strong data analysis skills  
- Ability to build interactive dashboards  
- Understanding of business metrics & KPIs  
- Real-world application of data-driven decision making  

---

## 🔗 Future Improvements
- Add time-series analysis (sales trends)  
- Deploy on Streamlit Cloud  
- Add machine learning for profit prediction  
