import taipy.gui.builder as tgb
from taipy.gui import Gui
import pandas as pd
from utils.constants import DATA_DIRECTORY
from frontend.charts import create_municipality_bar

df = pd.read_excel(
    DATA_DIRECTORY / "resultat-ansokningsomgang-2024.xlsx",
    sheet_name="Tabell 3",
    skiprows=5,
)


def filter_df_municipality(df, educational_area="Data/IT"):
    return (
        df.query("Utbildningsområde == @educational_area")["Kommun"]
        .value_counts()
        .reset_index()
        .rename({"count": "Ansökta utbildningar"}, axis=1)
    )


def filter_data(state):
    print(state)
    df_municipality = filter_df_municipality(state.df)

    state.municipality_chart = create_municipality_bar(
        df_municipality.head(state.number_municipalities),
        xlabel="# ANSÖKTA UTBILDNINGAR",
        ylabel="KOMMUN",
    )


df_municipality = filter_df_municipality(df)


municipality_chart = create_municipality_bar(
    df_municipality, xlabel="# ANSÖKTA UTBILDNINGAR", ylabel="KOMMUN"
)

number_municipalities = 5


with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("# MYH dashboard 2024", mode="md")

        with tgb.layout(columns="2 1"):
            with tgb.part(class_name="card"):
                tgb.text("Graph")
                tgb.chart(figure="{municipality_chart}")

            with tgb.part(class_name="card"):
                tgb.text("## Filtrera data", mode="md")
                tgb.text("Filtrera antalet kommuner", mode="md")

                tgb.slider(
                    "{number_municipalities}",
                    min=5,
                    max=len(df_municipality),
                    continuous=False,
                    # on_change=filter_data
                )

                tgb.button("FILTRERA DATA", class_name="plain", on_action=filter_data)

        with tgb.part(class_name="card"):
            tgb.text("Raw data")
            tgb.table("{df}")


if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
