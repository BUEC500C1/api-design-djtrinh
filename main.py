import weather_api as w_api
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def plot_data(data, code):
    periods = data['properties']['periods']

    x = []
    x_label = []
    y = []

    for i, period in enumerate(periods):
        if i == 25:
            break
        time = int(period['startTime'].split(':')[0][-2:])
        if time > 12:
            time = str(time-12)+"pm"
        elif time == 12:
            time = "12pm"
        elif time == 0:
            time = "12am"
        else:
            time = str(time)+"am"

        x_label.append(time)
        x.append(i)
        y.append(period['temperature'])

    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.canvas.draw()
    plt.plot(x, y)
    ax.set_xticklabels(x_label)
    plt.xticks(np.arange(min(x), max(x)+1, 1.0), rotation=45)
    plt.ylabel('Temperaute in F')
    plt.title("Weather Plot for "+code)
    plt.show()


def main():
    api = w_api.weather_api()

    while(1):
        code = input("Enter Airport Code\n")

        if(code.lower() == "exit"):
            break
        else:
            data = api.get_weather(code, 1)
            if data != -1:
                plot_data(data, code)


main()
