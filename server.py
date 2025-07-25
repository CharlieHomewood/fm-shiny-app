from shiny import render

def server(input, output, session):
    @output
    @render.text
    def result():
        return f"You chose: {input.num()}"