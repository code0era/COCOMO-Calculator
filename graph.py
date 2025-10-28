# graph.py
import matplotlib.pyplot as plt
import math
import os

def plot_results(results, project_name, save_path=None):
    """
    Plot a bar graph of COCOMO results and save to a file if save_path is given.
    """
    metrics = ['Effort (PM)', 'Development Time (Months)', 'Average Staff']
    values = [results[m] for m in metrics]
    ceiling_values = [math.ceil(results[m]) for m in metrics]

    x = range(len(metrics))

    plt.figure(figsize=(8,5))
    plt.bar(x, values, width=0.4, label='Calculated', color='skyblue')
    plt.bar([i + 0.4 for i in x], ceiling_values, width=0.4, label='Ceiling', color='lightgreen')

    plt.xticks([i + 0.2 for i in x], metrics)
    plt.ylabel('Values')
    plt.title(f'COCOMO Results: {project_name}')
    plt.legend()
    plt.tight_layout()

    if save_path:
        # Ensure folder exists
        folder = os.path.dirname(save_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()
