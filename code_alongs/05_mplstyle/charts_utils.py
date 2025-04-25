def horizontal_bar_options(ax, **options):

    ax.set_title(options.get("title", ""), loc="left", pad=20)
    ax.set_xlabel(options.get("xlabel", ""), loc="left")
    ax.set_ylabel(options.get("ylabel", ""), rotation=0)
    ax.yaxis.set_label_coords(
        options.get("ylabel_x_coord", -0.1), options.get("ylabel_y_coord", 1)
    )

    ax.legend().remove()
    ax.invert_yaxis()

    return ax

def save_fig_from_ax(ax, save_path):
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(save_path)
