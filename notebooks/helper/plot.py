import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
import colorsys
import numpy as np

black_light = '#2b2b2b'
black_deep = '#242424'
gray= '#f7f7f7'
starting_color_hsv = 167 / 360
ending_color_hsv = 270 / 360

mpl.rcParams['axes.prop_cycle'] = cycler(
    color = ['#33FFA7', '#33FFDC', '#33EEFF', '#33C0FF', '#339EFF', '#335AFF', '#5933FF', '#8433FF', '#AF33FF', '#D433FF', '#FC33FF']
)
mpl.rcParams["figure.figsize"] = [7.50, 4.50]


def make_color_line(n: int, start_h: float = starting_color_hsv, final_h: float = ending_color_hsv):

    h_list = np.linspace(start_h, final_h, n)

    color_list = []

    for h in h_list:
        color_list.append(colorsys.hsv_to_rgb(h, 1, 1))

    mpl.rcParams['axes.prop_cycle'] = cycler(
        color = color_list
    )


def make_plot (data: list, title: str, boundaries: int, legend: list, save_fig: bool = False, fig_title: str = ''):

    make_color_line(len(data))

    plt.figure(figsize=(7,7), facecolor=black_deep)
    ax = plt.axes()
    ax.set_facecolor(black_light)
    ax.spines['bottom'].set_color(gray)
    ax.spines['left'].set_color(gray)
    ax.spines['top'].set_color(gray)
    ax.spines['right'].set_color(gray)
    ax.xaxis.label.set_color(gray)
    ax.yaxis.label.set_color(gray)
    ax.title.set_color(gray)
    ax.tick_params(axis='x', colors=gray)
    ax.tick_params(axis='y', colors=gray)
    plt.annotate(
        r'@stepyt', xy=(0.5, 0.5), alpha=0.5,
        ha='left', va='bottom', color=gray, size=11
    )
    for curve in data:
        plt.plot(curve[0], curve[1], linewidth=3)
    plt.title(f'{title.upper()}', fontweight='bold', fontsize='16', pad=20)
    plt.xlim([0, boundaries])
    plt.ylim([0, boundaries])
    plt.xlabel("Token A [amount]", fontweight='bold', fontsize='13')
    plt.ylabel("Token B [amount]", fontweight='bold', fontsize='13')
    if legend:
        plt.legend(legend)
    plt.grid()
    if save_fig:
        plt.savefig(f'../assets/images/{fig_title}', format='png', dpi=600)

def make_plot_just_line (data: list, title: str, boundaries: int, legend: list, save_fig: bool = False, fig_title: str = ''):

    make_color_line(len(data))

    plt.figure(figsize=(7,7))
    ax = plt.axes()
    ax.axis('off')
    for curve in data:
        plt.plot(curve[0], curve[1], linewidth=3)
    plt.xlim([0, boundaries])
    plt.ylim([0, boundaries])
    ax.patch.set_alpha(0.)
    if save_fig:
        plt.savefig(f'../assets/images/{fig_title}', transparent=True, format='png', dpi=600)
        
def make_plot_price (
    data: list,
    points: list,
    title: str, 
    boundaries: int, 
    legend: list,
    save_fig: bool = False, 
    fig_title: str = ''
    ):

    make_color_line(len(data))

    plt.figure(figsize=(7,7), facecolor=black_deep)
    ax = plt.axes()
    ax.set_facecolor(black_light)
    ax.spines['bottom'].set_color(gray)
    ax.spines['left'].set_color(gray)
    ax.spines['top'].set_color(gray)
    ax.spines['right'].set_color(gray)
    ax.xaxis.label.set_color(gray)
    ax.yaxis.label.set_color(gray)
    ax.title.set_color(gray)
    ax.tick_params(axis='x', colors=gray)
    ax.tick_params(axis='y', colors=gray)
    plt.annotate(
        r'@stepyt', xy=(0.5, 0.5), alpha=0.5,
        ha='left', va='bottom', color=gray, size=11
        )
    for curve in data:
        plt.plot(curve[0], curve[1], linewidth=3)
    plt.scatter(points[0], points[1], color='r', linewidth=5, zorder=10)
    plt.plot(points[0], [points[1][0], points[1][0]], '--r')
    plt.plot([points[0][1], points[0][1]], points[1], '--r')
    plt.annotate(
        r'$\Delta A$', xy=((points[0][0] + points[0][1]) / 2, points[1][0]),
        ha='center', va='bottom', color=gray, size=15
        )
    plt.annotate(
        r'$\Delta B$', xy=(points[0][1], (points[1][0] + points[1][1]) / 2),
        ha='left', va='center', color=gray, size=15
        )
    plt.title(f'{title.upper()}', fontweight='bold', fontsize='16', pad=20)
    plt.xlim([0, boundaries])
    plt.ylim([0, boundaries])
    plt.xlabel("Token A [amount]", fontweight='bold', fontsize='13')
    plt.ylabel("Token B [amount]", fontweight='bold', fontsize='13')
    if legend:
        plt.legend(legend)
    plt.grid()
    if save_fig:
        plt.savefig(f'../assets/images/{fig_title}', format='png', dpi=600)