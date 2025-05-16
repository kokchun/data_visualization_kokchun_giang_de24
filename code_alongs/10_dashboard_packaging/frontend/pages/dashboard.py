import taipy.gui.builder as tgb
from backend.data_processing import filter_df_municipality, df
from frontend.charts import create_municipality_bar
from backend.updates import filter_data

number_municipalities = 5
max_municipalities = len(filter_df_municipality(df))

selected_educational_area = "Data/IT"

municipalities_chart_title = number_municipalities
educational_area_chart_title = selected_educational_area

df_municipality = filter_df_municipality(df, selected_educational_area).head(
    number_municipalities
)

municipality_chart = create_municipality_bar(
    df_municipality, xlabel="# ANSÖKTA UTBILDNINGAR", ylabel="KOMMUN"
)

with tgb.Page() as dashboard_page:
    with tgb.part(class_name="container card stack-large"):
        tgb.navbar()
        tgb.text("# MYH dashboard 2024", mode="md")

        with tgb.layout(columns="2 1"):
            with tgb.part(class_name="card"):
                tgb.text(
                    "## Antalet ansökta YH utbildningar per kommun (topp {municipalities_chart_title}) för {educational_area_chart_title}",
                    class_name="title-chart",
                    mode="md",
                )
                tgb.chart(figure="{municipality_chart}")

            with tgb.part(class_name="card left-margin-md"):
                tgb.text("## Filtrera data", mode="md")
                tgb.text("Filtrera antalet kommuner", mode="md")

                tgb.slider(
                    "{number_municipalities}",
                    min=5,
                    max="{max_municipalities}",
                    continuous=False,
                    # on_change=filter_data
                )

                tgb.text("Välj utbildningsområde", mode="md")
                tgb.selector(
                    "{selected_educational_area}",
                    lov=df["Utbildningsområde"].unique(),
                    dropdown=True,
                    # on_change=update_slider_max,
                )

                tgb.button("FILTRERA DATA", class_name="button-color", on_action=filter_data)


