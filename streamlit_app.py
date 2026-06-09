import streamlit as st
import time

st.set_page_config(page_title="行政管理数据看板", page_icon="📊", layout="wide")

# 用时间戳做缓存破坏，每次刷新都加载最新版
_cache_buster = str(int(time.time()))
GITHUB_PAGES_URL = f"https://admin-dashboard1.github.io/-https-xingzhengshuju.com/行政数据看板.html?t={_cache_buster}"

st.title("📊 行政管理数据看板")
st.caption("完整版 · 实时数据")

# Embed the full dashboard via IFrame pointing to GitHub Pages
st.components.v1.iframe(GITHUB_PAGES_URL, height=950, scrolling=True)

st.divider()
st.caption("数据来源：GitHub Pages · 飞书 → 预计算 JSON → HTML 嵌入")
