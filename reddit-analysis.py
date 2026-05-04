import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv("./data/reddit-responses.csv")
    df.columns = [
          "timestamp",
          "learn_first",
          "domain",
          "drop_off_reason",
          "math_opinion",
          "uses_docs",
          "video_length",
          "language_pref",
          "student_group"
    ]
    df
    return (df,)


@app.cell
def _(df):
    print(df.shape)
    return


@app.cell
def _(df):
    df.dtypes
    return


@app.cell
def _(df):
    df_clean = df.drop(columns=["timestamp"])
    df_clean
    return (df_clean,)


@app.cell
def _(df_clean):
    for col in df_clean.columns:
        print(f"{col} : {list(df_clean[col].unique())}\n")
    
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
