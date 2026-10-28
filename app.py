"""Dashboard that RUNS the team's own files (Question 1.py ... Question 4.py).
No maths is re-written here: each tab just runs a file and shows what it prints and plots."""
import contextlib
import io
import os
import re
import runpy

import matplotlib
matplotlib.use("Agg")                     # lets plots work without a pop-up window
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)                            # so files can find student_performance.csv

st.set_page_config(page_title="CMM Dashboard", layout="wide")
st.title("Computational Mathematical Modeling - Week 04 Dashboard")
# -------------------------------
# Group Members
# -------------------------------
st.subheader("Group Members")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### Kuladu")
    st.write("Question 1")

with col2:
    st.markdown("### Sadeepa")
    st.write("Question 2")

with col3:
    st.markdown("### Rasini")
    st.write("Question 3")

with col4:
    st.markdown("### Mihindi")
    st.write("Question 4")

st.divider()


def find_script(number):
    """Find 'Question 1.py', 'question1.py', 'Question_1.py' ... in this folder."""
    for name in sorted(os.listdir(HERE)):
        compact = re.sub(r"[\s_\-]", "", name.lower())
        if compact.startswith(f"question{number}") and name.endswith(".py"):
            return name
    return None


def run_script(path):
    """Run a file, capture what it prints and every figure it draws."""
    plt.close("all")
    buffer = io.StringIO()
    error = None
    with contextlib.redirect_stdout(buffer):
        try:
            runpy.run_path(path, run_name="__main__")
        except BaseException as err:      # show the error instead of crashing the dashboard
            error = err
    figures = [plt.figure(n) for n in plt.get_fignums()]
    return buffer.getvalue(), figures, error


def show_tab(number, title):
    st.header(title)
    path = find_script(number)
    if path is None:
        st.error(f"Could not find a file called 'Question {number}.py' in the repo.")
        return
    st.caption(f"Using file: {path}")

    key = f"result_{number}"
    if st.button(f"Run Question {number}", key=f"button_{number}"):
        with st.spinner("Running..."):
            st.session_state[key] = run_script(path)

    if key in st.session_state:
        text, figures, error = st.session_state[key]
        if error is not None:
            st.error(f"{type(error).__name__}: {error}")
        if text:
            st.subheader("Output")
            st.code(text)
        for fig in figures:
            st.pyplot(fig)

    with st.expander("Show the code"):
        with open(path, encoding="utf-8") as handle:
            st.code(handle.read(), language="python")


tab1, tab2, tab3, tab4 = st.tabs(
    ["Question 1", "Question 2", "Question 3", "Question 4"])

with tab1:
    show_tab(1, "Q1 Statistics")
with tab2:
    show_tab(2, "Q2 Linear Algebra")
with tab3:
    show_tab(3, "Q3 Calculus")
with tab4:
    show_tab(4, "Q4 Student Data")
    if os.path.exists("student_performance.csv"):
        with st.expander("Preview the dataset"):
            st.dataframe(pd.read_csv("student_performance.csv"))
