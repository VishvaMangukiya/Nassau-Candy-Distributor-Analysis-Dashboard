import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Profitability Dashboard", layout="wide")

# -------------------------------
# GLOBAL STYLING
# -------------------------------
st.markdown("""
<style>

/* App Background */
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #bbdefb, #90caf9);
} 

/* Header */
.header {
    background: linear-gradient(135deg, #111e3c, #1e3a8a);
    padding: 1.5rem 2rem;
    border-radius: 16px;
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #1e293b);
    padding: 20px 15px;
}

/* Sidebar Labels */
section[data-testid="stSidebar"] label {
    color: #ffffff !important;
    font-size: 14px;
    font-weight: 600;
}

/* ===== KPI GRADIENT CARDS ===== */
.kpi-card {
    padding: 20px;
    border-radius: 18px;
    color: white;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    transition: 0.3s ease;
}

.kpi-card:hover {
    transform: translateY(-5px) scale(1.02);
}

.kpi-title {
    font-size: 14px;
    opacity: 0.9;
}

.kpi-value {
    font-size: 28px;
    font-weight: bold;
    margin-top: 5px;
}

/* Gradients */
.sales {
    background: linear-gradient(135deg, #3b82f6, #60a5fa);
}

.profit {
    background: linear-gradient(135deg, #10b981, #34d399);
}

.margin {
    background: linear-gradient(135deg, #f59e0b, #fbbf24);
}

.products {
    background: linear-gradient(135deg, #8b5cf6, #a78bfa);
}

/* Titles */
h1, h2, h3 {
    color: #0d47a1;
}

            .dependency-card {
    background: linear-gradient(135deg, #1e3a8a, #3b82f6);
    padding: 25px;
    border-radius: 18px;
    color: white;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    transition: 0.3s ease;
}

.dependency-card:hover {
    transform: scale(1.03);
}

.dep-title {
    font-size: 16px;
    opacity: 0.9;
}

.dep-value {
    font-size: 36px;
    font-weight: bold;
    margin-top: 10px;
}

.dep-sub {
    font-size: 14px;
    opacity: 0.85;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<div class="header">
    <h1 style="margin:0; font-size:3rem;">Product Profitability Dashboard 📈</h1>
    <p style="margin:0; opacity:0.9; font-size:1.2rem;">
        Nassau Candy Distributor • Real-time Insights
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("Nassau Candy Distributor.csv")

# -------------------------------
# CLEANING
# -------------------------------
df = df.dropna()
df = df[df['Sales'] > 0]

# -------------------------------
# CALCULATIONS
# -------------------------------
df['Profit'] = df['Sales'] - df['Cost']
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100



df_original = df.copy()


# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.markdown("""
<div style="
    background: rgba(37, 99, 235, 0.2);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 10px;
    border-radius: 12px;
    text-align: center;
    font-size: 30px;
    font-weight: 600;
    color: white;
    margin-bottom: 20px;
">
    🎯 Filter Panel
</div>
""", unsafe_allow_html=True)

# if 'Order Date' in df.columns:
#     df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

#     date_range = st.sidebar.date_input(
#         "📅 Select Date Range",
#         [df['Order Date'].min(), df['Order Date'].max()]
#     )

#     df = df[(df['Order Date'] >= pd.to_datetime(date_range[0])) &
#             (df['Order Date'] <= pd.to_datetime(date_range[1]))]
    
division = st.sidebar.selectbox(
    "🏢 Select Division",
    ["All"] + sorted(df['Division'].unique())
)

if division != "All":
    df = df[df['Division'] == division]

st.sidebar.markdown("<hr style='border:0.5px solid rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

product = st.sidebar.selectbox(
    "🔍 Search Product",
    [""] + sorted(df['Product Name'].unique())
)

if product != "":
    df = df[df['Product Name'] == product]

st.sidebar.markdown("<hr style='border:0.5px solid rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

min_margin = st.sidebar.slider(
    "📊 Minimum Profit Margin (%)",
    0, 100, 10
)

df = df[df['Profit Margin'] >= min_margin]

# -------------------------------
# KPI SECTION (UPDATED)
# -------------------------------
st.markdown("## Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"""
<div class="kpi-card sales">
    <div class="kpi-title">💰 Total Sales</div>
    <div class="kpi-value">{df['Sales'].sum():,.0f}</div>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="kpi-card profit">
    <div class="kpi-title">📈 Total Profit</div>
    <div class="kpi-value">{df['Profit'].sum():,.0f}</div>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="kpi-card margin">
    <div class="kpi-title">📊 Avg Margin %</div>
    <div class="kpi-value">{df['Profit Margin'].mean():.2f}</div>
</div>
""", unsafe_allow_html=True)

col4.markdown(f"""
<div class="kpi-card products">
    <div class="kpi-title">📦 Total Products</div>
    <div class="kpi-value">{df['Product Name'].nunique()}</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# REST OF YOUR CODE (UNCHANGED)
# -------------------------------
st.markdown("---")

col1, col2 = st.columns(2)

top_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
division_data = df.groupby('Division')[['Sales', 'Profit']].sum()

with col1:
    st.subheader("Top Products")
    st.bar_chart(top_products)

with col2:
    st.subheader("Division Performance")
    st.bar_chart(division_data)

st.markdown("---")

st.subheader("🏆 Product Margin Leaderboard")

margin_leaderboard = df.groupby('Product Name')['Profit Margin'].mean().sort_values(ascending=False).head(10)

st.bar_chart(margin_leaderboard)

col3, col4 = st.columns(2)

fig = px.scatter(df, x="Sales", y="Profit", color="Division", size="Profit", hover_data=["Product Name"])
fig2 = px.histogram(df, x="Profit Margin", nbins=20)

with col3:
    st.subheader("Cost vs Profit")
    st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader("Margin Distribution")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("Pareto Analysis")

pareto = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False)
pareto_cum = pareto.cumsum() / pareto.sum()

st.line_chart(pareto_cum)

st.markdown("---")
st.subheader("📊 Profit Dependency Indicator")

top_20 = int(0.2 * len(pareto))
dependency = pareto.head(top_20).sum() / pareto.sum() * 100

st.markdown(f"""
<div class="dependency-card">
    <div class="dep-title">Top 20% Products Contribution</div>
    <div class="dep-value">{dependency:.2f}%</div>
    <div class="dep-sub">of Total Profit</div>
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 4️⃣ HIGH SALES LOW PROFIT (IMPORTANT)
# -------------------------------


st.markdown("---")
st.subheader("⚠️ High Sales but Low Profit Products")

high_sales_low_profit = df_original[
    (df_original['Sales'] > df_original['Sales'].quantile(0.75)) &
    (df_original['Profit'] < df_original['Profit'].quantile(0.25))
]

st.dataframe(
    high_sales_low_profit[['Product Name', 'Sales', 'Profit', 'Profit Margin']]
    .sort_values(by='Profit Margin')
)

st.markdown("---")
st.subheader("💰 Cost vs Sales Analysis")

fig_cost = px.scatter(
    df,
    x="Sales",
    y="Cost",
    color="Division",
    size="Profit",
    hover_data=["Product Name"]
)

st.plotly_chart(fig_cost, use_container_width=True)


# -------------------------------
# 5️⃣ MARGIN RISK PRODUCTS
# -------------------------------
st.markdown("---")
st.subheader("🚨 Margin Risk Products")

risk_products = df_original[df_original['Profit Margin'] < 10]
st.dataframe(
    risk_products[['Product Name', 'Division', 'Sales', 'Profit', 'Profit Margin']]
    .sort_values(by='Profit Margin')
)

st.subheader("Key Insights")

high_profit = df[df['Profit'] > df['Profit'].mean()]
low_margin = df[df['Profit Margin'] < df['Profit Margin'].mean()]

top_20 = int(0.2 * len(pareto))
top_profit_share = pareto.head(top_20).sum() / pareto.sum() * 100

def insight_box(text, bg_color, border_color):
    st.markdown(f"""
    <div style="
        background-color: {bg_color};
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid {border_color};
        margin-bottom: 10px;
        font-size: 16px;
    ">
        {text}
    </div>
    """, unsafe_allow_html=True)

insight_box(f"✅ {len(high_profit)} products generate above-average profit.", "#e6f4ea", "#22c55e")
insight_box(f"⚠️ {len(low_margin)} products have below-average profit margins.", "#fff4e5", "#f59e0b")
insight_box(f"🔥 Top 20% contribute {top_profit_share:.2f}% of total profit.", "#eef2ff", "#6366f1")
