import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
import seaborn as sns

st.set_page_config(
    page_title="Streamlit + Pygwalker Webアプリ",
    layout="wide"
)

STR_UPLOAD_CSV = "CSVファイルをアップロード"
STR_SAMPLE_DATASET = "サンプルデータセットを使う"

df = None
with st.sidebar:
    select_data_type = st.radio(
        "使うデータのタイプを選択",
        [STR_UPLOAD_CSV, STR_SAMPLE_DATASET]
    )
    if select_data_type == STR_UPLOAD_CSV:
        input = st.file_uploader("Choose a CSV file")
        if input is not None:
            title_str = input.name
            df = pd.read_csv(input)
    else:
        select_data_set = st.radio(
            "datasetを選択してください",
            ["iris", "mpg", "titanic", "penguins"]
        )
        title_str = select_data_set
        if select_data_set == "iris":
            df = sns.load_dataset("iris")
        elif select_data_set == "mpg":
            df = sns.load_dataset("mpg")
        elif select_data_set == "titanic":
            df = sns.load_dataset("titanic")
        else:
            df = sns.load_dataset("planets")


if df is not None:
    st.markdown(f"### {title_str}")
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()
else:
    st.markdown("サイドバーでデータを選択してください")
