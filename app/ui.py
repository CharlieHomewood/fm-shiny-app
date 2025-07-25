from shiny import ui

app_ui = ui.page_fluid(
    ui.h2("My First Shiny App"),
    ui.input_slider("num", "Choose a number", min=1, max=100, value=50),
    ui.output_text("result"),
)