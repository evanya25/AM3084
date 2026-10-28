"""Dashboard. It only CALLS the functions in q1..q4 - no maths is re-written here."""
import pandas as pd
import streamlit as st
import sympy as sp

import q1_statistics as q1
import q2_linear_algebra as q2
import q3_calculus as q3
import q4_data_analysis as q4

st.set_page_config(page_title="CMM Dashboard", layout="wide")
st.title("Computational Mathematical Modeling - Week 04 Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Q1 Statistics", "Q2 Linear Algebra", "Q3 Calculus", "Q4 Student Data"])

# ---------------------------------------------------------------- Q1
with tab1:
    st.header("Study hours statistics")
    source = st.radio("Dataset", ["Original", "Corrected (first 8 -> 12)", "My own numbers"],
                      horizontal=True)
    if source == "Original":
        data = q1.ORIGINAL
    elif source.startswith("Corrected"):
        data = q1.corrected_data()
    else:
        text = st.text_input("Numbers separated by commas", "5, 2, 8, 4, 7")
        try:
            data = [float(x) for x in text.split(",") if x.strip()]
        except ValueError:
            st.error("Please enter numbers separated by commas.")
            data = []
    if data:
        st.write("Data:", data)
        stats = q1.describe(data)
        cols = st.columns(len(stats))
        for col, (name, value) in zip(cols, stats.items()):
            col.metric(name, f"{value:.4f}")
        bins = st.slider("Number of histogram bins", 3, 12, 6)
        st.pyplot(q1.make_histogram(data, bins))

# ---------------------------------------------------------------- Q2
with tab2:
    st.header("System A X = B")
    st.write("Edit the numbers if you want to try a different system.")
    left, right = st.columns([3, 1])
    A_df = left.data_editor(pd.DataFrame(q2.A_DEFAULT, columns=["x", "y", "z"]),
                            key="A_editor")
    B_df = right.data_editor(pd.DataFrame(q2.B_DEFAULT, columns=["B"]), key="B_editor")
    A, B = A_df.to_numpy(dtype=float), B_df["B"].to_numpy(dtype=float)
    try:
        info = q2.analyse_matrix(A)
        st.subheader("(a) Matrix properties")
        st.write("Determinant:", info["det"])
        if info["inverse"] is None:
            st.warning("det(A) = 0, so A has no inverse.")
        else:
            st.write("Inverse of A:")
            st.dataframe(pd.DataFrame(info["inverse"]))
        st.write("Eigenvalues:", info["eigenvalues"])
        st.write("Eigenvectors (each COLUMN belongs to the eigenvalue in the same position):")
        st.dataframe(pd.DataFrame(info["eigenvectors"]))
        X, R, norm = q2.solve_system(A, B)
        st.subheader("(b) Solution and (c) residual")
        st.write("X = [x, y, z] =", X)
        st.write("Residual vector R = AX - B =", R)
        st.write("Euclidean norm of R:", norm)
    except Exception as err:
        st.error(f"Could not solve this system: {err}")

# ---------------------------------------------------------------- Q3
with tab3:
    st.header("f(t) = t^3 - 6t^2 + 9t + 2")
    res = q3.analyse_function()
    st.write("Factorised form:")
    st.latex(sp.latex(res["factored"]))
    st.write("Roots of f(t) = 0:", res["roots_f_equals_0"])
    st.write("Solutions of f(t) = 2:", res["solutions_f_equals_2"])
    st.write("f'(t):")
    st.latex(sp.latex(res["first_derivative"]))
    st.write("f''(t):")
    st.latex(sp.latex(res["second_derivative"]))
    st.write("Indefinite integral (add + C):")
    st.latex(sp.latex(res["indefinite_integral"]))
    c1, c2 = st.columns(2)
    a = c1.number_input("Lower limit a", value=0.0)
    b = c2.number_input("Upper limit b", value=2.0)
    st.write(f"Definite integral from {a} to {b}:", q3.definite_integral(a, b))
    st.pyplot(q3.plot_function())

# ---------------------------------------------------------------- Q4
with tab4:
    st.header("Student performance data")
    df = None
    try:
        df = q4.load_data("student_performance.csv")
    except FileNotFoundError:
        up = st.file_uploader("student_performance.csv was not found - upload it", type="csv")
        if up is not None:
            df = q4.load_data(up)
    if df is not None:
        info = q4.overview(df)
        st.write("Dimensions (rows, columns):", info["shape"])
        st.write("Data types:")
        st.dataframe(info["dtypes"].rename("type"))
        st.write("First rows:")
        st.dataframe(info["head"])
        st.write("Summary statistics:")
        st.dataframe(info["describe"])

        s = q4.exam_stats(df)
        m1, m2, m3 = st.columns(3)
        m1.metric("Mean exam mark", f"{s['mean']:.2f}")
        m2.metric("Median exam mark", f"{s['median']:.2f}")
        m3.metric("Std deviation", f"{s['std']:.2f}")
        st.write("Student with the highest exam mark:")
        st.dataframe(s["top_student"].to_frame().T)
        st.write("Pearson correlation (Study Hours vs Exam):", q4.correlation(df))

        cat = q4.categorise(df)
        st.write("Exam categories:")
        st.dataframe(cat["Category"].value_counts())
        st.download_button("Download cleaned data (CSV)",
                           cat.to_csv(index=False), "cleaned_data.csv", "text/csv")

        figs = q4.make_plots(df)
        choice = st.selectbox("Choose a plot", list(figs.keys()))
        st.pyplot(figs[choice])
