
"""
Script for running plots smoothly, using parameter scaling from Gomez.
Using Ordmm_Land, not coupled
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import ORdmm_Land as model

def plot_state_hf_ordmm(hf_type, ms=1000, state="v", label="V (mV)", title="", size=(15,5), out=None):
    """ Plotting blablabla.

    Args:
        hf_type (str):
        ms (int): 
        state (str): State value to plot.
        label (str): Plot label, should match state value.
        title (str): Title of plot.
        size (tuple): Size of plot.
        out (str): If provided, equals desired filename/path to save plot. 

    Returns: 
        fig ():

    """

    tsteps = np.arange(0.0, 1000, 0.1)
    steps = ms*10

    y_endo_c = np.load('init_values/control_endo_ordmm.npy')
    y_epi_c = np.load('init_values/control_epi_ordmm.npy')
    y_m_c = np.load('init_values/control_m_ordmm.npy')

    y_endo_hf = np.load(f'init_values/{hf_type}_endo_ordmm.npy')
    y_epi_hf = np.load(f'init_values/{hf_type}_epi_ordmm.npy')
    y_m_hf = np.load(f'init_values/{hf_type}_m_ordmm.npy')

    fig, axs = plt.subplots(1, 3, figsize=size)
    axs[0].plot(tsteps[:steps], y_endo_c[:, model.state_indices(state)][:steps])
    axs[1].plot(tsteps[:steps], y_epi_c[:, model.state_indices(state)][:steps])
    axs[2].plot(tsteps[:steps], y_m_c[:, model.state_indices(state)][:steps])

    axs[0].plot(tsteps[:steps], y_endo_hf[:, model.state_indices(state)][:steps])
    axs[1].plot(tsteps[:steps], y_epi_hf[:, model.state_indices(state)][:steps])
    axs[2].plot(tsteps[:steps], y_m_hf[:, model.state_indices(state)][:steps])

    axs[0].set(ylabel=f"{label}")
    axs[0].legend((r"Control endo", r"HF endo"))
    axs[1].legend((r"Control epi", r"HF epi"))
    axs[2].legend((r"Control m", r"HF m"))
    plt.suptitle(f"{title}")

    if out != None:
        # save plot
        if not os.path.isdir("plots"):
            os.mkdir("plots")
        
        path = os.path.join("plots", out)
        plt.savefig(path)
    
    return fig


if __name__ == "__main__":
    fig1 = plot_state_hf_ordmm(hf_type="gomez", 
                               ms=500, 
                               state='v',
                               label='V (mV)',
                               title="Ionic HF remodelling vs. control", 
                               out="gomez_V.png")
    fig2 = plot_state_hf_ordmm(hf_type="gomez_hetero", 
                               ms=500, 
                               state='v',
                               label='V (mV)',
                               title="Heterogenous transmural Ionic HF remodelling vs. control", 
                               out="hetero_gomez_V.png")
    plt.show()