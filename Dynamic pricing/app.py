import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Dynamic Pricing", layout="wide")

# Elegant header
st.markdown("<h1 style='text-align: center; font-weight: 300;'>Dynamic Pricing Engine</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Real-time e-commerce price simulation based on market conditions</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar controls
st.sidebar.markdown("### ⚙️ Market Controls")
d = st.sidebar.slider("Demand Level", 0.3, 3.0, 1.0, 0.01)
s = st.sidebar.slider("Supply Constraint", 0.3, 3.0, 1.0, 0.01)
c = st.sidebar.number_input("Competitor Price ($)", 1.0, 1000.0, 95.0)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📦 Product Details")
    name = st.text_input("Product Name", "Wireless Earbuds")
    base = st.number_input("Base Price ($)", value=100.0)
    cat = st.selectbox("Category", ["Electronics", "Clothing", "Home", "Books", "Other"])

with col2:
    st.markdown("#### 📊 Market Summary")
    st.write(f"**Demand Level:** {d}")
    st.write(f"**Supply Constraint:** {s}")
    st.write(f"**Competitor Price:** ${c}")

# Pricing logic
def calc_price(b, d, s, c):
    adjusted = b * d / s
    final = (adjusted + c) / 2
    return round(final, 2), round(adjusted, 2)

# Run only if product name is valid
if name:
    final_price, adjusted_price = calc_price(base, d, s, c)

    st.markdown(f"<h2 style='text-align: center;'>📌 Final Price: <span style='color:#d6336c;'>${final_price}</span></h2>", unsafe_allow_html=True)
    st.markdown("---")

    # Interactive plotly chart
    fig = go.Figure(data=[
        go.Bar(name="Pricing", x=["Base Price", "Adjusted", "Final"],
               y=[base, adjusted_price, final_price],
               marker_color=["#636EFA", "#EF553B", "#00CC96"])
    ])
    fig.update_layout(
        title="💹 Dynamic Price Breakdown",
        yaxis_title="Price ($)",
        xaxis_title="Stage",
        plot_bgcolor='white',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("👆 Please enter a product name to calculate pricing.")

st.markdown("---")
st.caption("Built with ❤️ for Hackathon using Streamlit + Plotly")
