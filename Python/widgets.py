"""
Implements a widget for Ordmm_Land the same way as in the E6 notebook (GBV). 
The widget is implemented as a class that can be imported. To use the widget, 
create an object of the class in question and call its display method.

Example:
========
from widgets import Ordmm_Land_Widget
Ordmm_Land_Widget().display()
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from ipywidgets import interact, FloatSlider #, Button, Dropdown, Layout
import ORdmm_Land as model
import ORdmm_Land_em_coupling as model_em
import importlib
importlib.reload(model)
importlib.reload(model_em)


class Ordmm_Land_Widget:
    """A widget to solve the ORdmm_Land" model model"""

    # ----------------------------------------------------------------------------
    # The widget

    def __init__(self):
        interact(
            self.solve_and_plot,
            GNa_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gNa rate (I_Na)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            Gto_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gto rate (I_to)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GKr_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gKr rate (I_Kr)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GKs_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gKs rate (I_Ks)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GK1_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gK1 rate (I_K1)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            Gncx_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gncx rate (INaCa_i, INaCa_ss)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GKb_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gKb rate (I_Kb)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GpCa_coeff=FloatSlider(
                value=1,
                min=0,
                max=1000,
                step=0.1,
                description="gpCa rate (IpCa)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GNaL_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gNaL rate (I_NaL)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
        
        )

    # ----------------------------------------------------------------------------
    # The run function

    def solve_and_plot(
        self, 
        GNa_coeff, 
        Gto_coeff,
        GKr_coeff,
        GKs_coeff,
        GK1_coeff,
        Gncx_coeff,
        GKb_coeff,
        GpCa_coeff,
        GNaL_coeff,

    ):

        # cannot make this work
        Params_to_change = {
            "GNa": GNa_coeff,
        }

        # print(Params_to_change)
        # print(GNa_coeff)

        # run model
        parameters = model.init_parameter_values()
        y0 = model.init_state_values()
        T = np.linspace(0, 500, 501)
        Y = odeint(model.rhs, y0, T, args=(parameters,))

        # Extract monitored values
        monitor = np.array([model.monitor(r, t, parameters) for r, t in zip(Y, T)])

        fig, axs = plt.subplots(2, 2, figsize=(12,8))
        axs[0, 0].plot(T, Y[:, model.state_indices("v")])
        axs[0, 1].plot(T, Y[:, model.state_indices("cai")])
        axs[1, 0].plot(T, Y[:, model.monitor_indices('INa')])
        axs[1, 1].plot(T, Y[:, model.monitor_indices('INaL')])

        # parameters = model.init_parameter_values(Params_to_change)
        parameters = model.init_parameter_values(
            GNa_rate=GNa_coeff,
            Gto_rate=Gto_coeff,
            GKr_rate=GKr_coeff,
            GKs_rate=GKs_coeff,
            GK1_rate=GK1_coeff,
            Gncx_rate=Gncx_coeff,
            GKb_rate=GKb_coeff,
            GpCa_rate=GpCa_coeff,
            GNaL_rate=GNaL_coeff,
     
        )
        y0 = model.init_state_values()
        T = np.linspace(0, 500, 501)
        Y = odeint(model.rhs, y0, T, args=(parameters,))

        axs[0, 0].plot(T, Y[:, model.state_indices("v")])
        axs[0, 0].legend((r"Default", r"$new$"))
        axs[0, 0].set(ylabel="V(mV)")
        axs[0, 1].plot(T, Y[:, model.state_indices("cai")])
        axs[0, 1].legend((r"Default", r"$new$"))
        axs[0, 1].set(ylabel="Ca_i(mM)")
        axs[1, 0].plot(T, Y[:, model.monitor_indices('INa')])
        axs[1, 0].legend((r"Default", r"$new$"))
        axs[1, 0].set(ylabel="I_Na")
        axs[1, 1].plot(T, Y[:, model.monitor_indices('INaL')])
        axs[1, 1].legend((r"Default", r"$new$"))
        axs[1, 1].set(ylabel="INaL")
  

        plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
        plt.show()






class Ordmm_Land_em_Widget:
    """A widget to solve the ORdmm_Land_em_coupled" model"""

    # ----------------------------------------------------------------------------
    # The widget

    def __init__(self):
        interact(
            self.solve_and_plot,
            GNa_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gNa rate (I_Na)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            Gto_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gto rate (I_to)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GKr_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gKr rate (I_Kr)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GKs_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gKs rate (I_Ks)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GK1_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gK1 rate (I_K1)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            Gncx_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gncx rate (INaCa_i, INaCa_ss)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GKb_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gKb rate (I_Kb)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GpCa_coeff=FloatSlider(
                value=1,
                min=0,
                max=1000,
                step=0.1,
                description="gpCa rate (IpCa)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
            GNaL_coeff=FloatSlider(
                value=1,
                min=0,
                max=10,
                step=0.1,
                description="gNaL rate (I_NaL)",
                continuous_update=False,
                layout={'width': '600px'},
                style={'description_width': '250px'},
            ),
        
        )

    # ----------------------------------------------------------------------------
    # The run function

    def solve_and_plot(
        self, 
        GNa_coeff, 
        Gto_coeff,
        GKr_coeff,
        GKs_coeff,
        GK1_coeff,
        Gncx_coeff,
        GKb_coeff,
        GpCa_coeff,
        GNaL_coeff,

    ):

        # cannot make this work
        Params_to_change = {
            "GNa": GNa_coeff,
        }

        # print(Params_to_change)
        # print(GNa_coeff)

        # run model
        parameters = model_em.init_parameter_values()
        y0 = model_em.init_state_values(CaTrpn=0.0092)
        T = np.linspace(0, 500, 501)
        Y = odeint(model_em.rhs, y0, T, args=(parameters,))

        # Extract monitored values
        monitor = np.array([model_em.monitor(r, t, parameters) for r, t in zip(Y, T)])
        I_CaL_idx = model_em.monitor_indices('ICaL')
        I_CaL = monitor.T[I_CaL_idx]

        #ax[0].plot(tsteps, V)

        fig, axs = plt.subplots(2, 2, figsize=(12,8))
        axs[0, 0].plot(T, Y[:, model_em.state_indices("v")])
        axs[0, 1].plot(T, Y[:, model_em.state_indices("cai")])
        axs[1, 0].plot(T, Y[:, model_em.monitor_indices('INa')])
        #axs[1, 1].plot(T, Y[:, model_em.monitor_indices('ICaL')])
        axs[1, 1].plot(T, I_CaL)

        # parameters = model.init_parameter_values(Params_to_change)
        parameters = model_em.init_parameter_values(
            GNa_rate=GNa_coeff,
            Gto_rate=Gto_coeff,
            GKr_rate=GKr_coeff,
            GKs_rate=GKs_coeff,
            GK1_rate=GK1_coeff,
            Gncx_rate=Gncx_coeff,
            GKb_rate=GKb_coeff,
            GpCa_rate=GpCa_coeff,
            GNaL_rate=GNaL_coeff,
     
        )
        y0 = model_em.init_state_values(CaTrpn=0.0092)
        T = np.linspace(0, 500, 501)
        Y = odeint(model_em.rhs, y0, T, args=(parameters,))

        monitor = np.array([model_em.monitor(r, t, parameters) for r, t in zip(Y, T)])
        I_CaL_idx = model_em.monitor_indices('ICaL')
        I_CaL = monitor.T[I_CaL_idx]

        axs[0, 0].plot(T, Y[:, model_em.state_indices("v")])
        axs[0, 0].legend((r"Default", r"$new$"))
        axs[0, 0].set(ylabel="V(mV)")
        axs[0, 1].plot(T, Y[:, model_em.state_indices("cai")])
        axs[0, 1].legend((r"Default", r"$new$"))
        axs[0, 1].set(ylabel="Ca_i(mM)")
        axs[1, 0].plot(T, Y[:, model_em.monitor_indices('INa')])
        axs[1, 0].legend((r"Default", r"$new$"))
        axs[1, 0].set(ylabel="I_Na")
        #axs[1, 1].plot(T, Y[:, model_em.monitor_indices('ICaL')])
        axs[1, 1].plot(T, I_CaL)
        axs[1, 1].legend((r"Default", r"$new$"))
        axs[1, 1].set(ylabel="ICaL")
  

        plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
        plt.show()
    
