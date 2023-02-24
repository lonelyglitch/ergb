import matplotlib.pyplot as plt


# sample data
def display_graph(currency, time,value):

    # plot the data
    plt.plot(time, value)
    # add labels
    plt.xlabel("time")
    plt.ylabel("value")
    plt.title(f'{currency} table')

    # display the plot
    plt.show()