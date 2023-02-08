# Gotran generated code for the "ORdmm_Land_em_coupling" model
# changed to temporary values for parameters scaling (electro + mech)
# model can be used to doublecheck isometric contraction

from __future__ import division

import numpy as np
import math


def init_state_values(**values):
    """
    Initialize state values
    """
    # Init values
    # CaMKt=0, m=0, hf=1, hs=1, j=1, hsp=1, jp=1, mL=0, hL=1, hLp=1, a=0,
    # iF=1, iS=1, ap=0, iFp=1, iSp=1, d=0, ff=1, fs=1, fcaf=1,
    # fcas=1, jca=1, ffp=1, fcafp=1, nca=0, xrf=0, xrs=0, xs1=0,
    # xs2=0, xk1=1, v=-87, Jrelnp=0, Jrelp=0, nai=7, nass=7,
    # ki=145, kss=145, cass=0.0001, cansr=1.2, cajsr=1.2, XS=0,
    # XW=0, CaTrpn=1, TmB=1, Zetas=0, Zetaw=0, Cd=0, cai=0.0001

    #CaTrpn=0
    init_values = np.array(
        [
            0,
            0,
            1,
            1,
            1,
            1,
            1,
            0,
            1,
            1,
            0,
            1,
            1,
            0,
            1,
            1,
            0,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            1,
            -87,
            0,
            0,
            7,
            7,
            145,
            145,
            0.0001,
            1.2,
            1.2,
            0,
            0,
            0.0092, #CaTrpn
            1,
            0,
            0,
            0,
            0.0001,
        ],
        dtype=np.float_,
    )

    # State indices and limit checker
    state_ind = dict(
        [
            ("CaMKt", 0),
            ("m", 1),
            ("hf", 2),
            ("hs", 3),
            ("j", 4),
            ("hsp", 5),
            ("jp", 6),
            ("mL", 7),
            ("hL", 8),
            ("hLp", 9),
            ("a", 10),
            ("iF", 11),
            ("iS", 12),
            ("ap", 13),
            ("iFp", 14),
            ("iSp", 15),
            ("d", 16),
            ("ff", 17),
            ("fs", 18),
            ("fcaf", 19),
            ("fcas", 20),
            ("jca", 21),
            ("ffp", 22),
            ("fcafp", 23),
            ("nca", 24),
            ("xrf", 25),
            ("xrs", 26),
            ("xs1", 27),
            ("xs2", 28),
            ("xk1", 29),
            ("v", 30),
            ("Jrelnp", 31),
            ("Jrelp", 32),
            ("nai", 33),
            ("nass", 34),
            ("ki", 35),
            ("kss", 36),
            ("cass", 37),
            ("cansr", 38),
            ("cajsr", 39),
            ("XS", 40),
            ("XW", 41),
            ("CaTrpn", 42),
            ("TmB", 43),
            ("Zetas", 44),
            ("Zetaw", 45),
            ("Cd", 46),
            ("cai", 47),
        ]
    )

    for state_name, value in values.items():
        if state_name not in state_ind:
            raise ValueError("{0} is not a state.".format(state_name))
        ind = state_ind[state_name]

        # Assign value
        init_values[ind] = value

    return init_values


def init_parameter_values(**values):
    """
    Initialize parameter values
    """
    # Param values
    # scale_ICaL=1.018, scale_IK1=1.414, scale_IKr=1.119, scale_IKs=1.648,
    # scale_INaL=2.274, celltype=0, cao=1.8, ko=5.4, nao=140.0,
    # F=96485.0, R=8314.0, T=310.0, L=0.01, rad=0.0011, Ahf=0.99,
    # GNa=31, thL=200.0, Gto=0.02, delta_epi=1.0, Aff=0.6, Kmn=0.002,
    # k2n=1000.0, tjca=75.0, zca=2.0, bt=4.75, Beta0=2.3, Beta1=-2.4,
    # Tot_A=25, Tref=120, Trpn50=0.35, calib=1, cat50_ref=0.805,
    # dLambda=0, emcoupling=1, etal=200, etas=20, gammas=0.0085,
    # gammaw=0.615, isacs=0, ktrpn=0.1, ku=0.04, kuw=0.182,
    # kws=0.012, lmbda=1, mode=1, ntm=2.4, ntrpn=2, p_a=2.1,
    # p_b=9.1, p_k=7, phi=2.23, rs=0.25, rw=0.5, CaMKo=0.05,
    # KmCaM=0.0015, KmCaMK=0.15, aCaMK=0.05, bCaMK=0.00068,
    # PKNa=0.01833, Gncx=0.0008, KmCaAct=0.00015, kasymm=12.5,
    # kcaoff=5000.0, kcaon=1500000.0, kna1=15.0, kna2=5.0, kna3=88.12,
    # qca=0.167, qna=0.5224, wca=60000.0, wna=60000.0, wnaca=5000.0,
    # H=1e-07, Khp=1.698e-07, Kki=0.5, Kko=0.3582, Kmgatp=1.698e-07,
    # Knai0=9.073, Knao0=27.78, Knap=224.0, Kxkur=292.0, MgADP=0.05,
    # MgATP=9.8, Pnak=30, delta=-0.155, eP=4.2, k1m=182.4, k1p=949.5,
    # k2m=39.4, k2p=687.2, k3m=79300.0, k3p=1899.0, k4m=40.0,
    # k4p=639.0, zk=1.0, GKb=0.003, PNab=3.75e-10, PCab=2.5e-08,
    # GpCa=0.0005, Esac_ns=-10, Gsac_k=1.097904761904762, Gsac_ns=0.006,
    # lambda_max=1.1, amp=-80.0, duration=0.5, BSLmax=1.124,
    # BSRmax=0.047, KmBSL=0.0087, KmBSR=0.00087, cmdnmax=0.05,
    # csqnmax=10.0, kmcmdn=0.00238, kmcsqn=0.8, kmtrpn=0.0005,
    # trpnmax=0.07

    # GNa_rate=1, Gto_rate=1, GKr_rate=1, GKs_rate=1, GK1_rate=1,
    # Gncx_rate=1, GKb_rate=1, GpCa_rate=1, GNaL_rate=1

    #more HF
    #Jleak_rate,
    #Jserca_rate,
    #CaMKa_rate,
    
    #PNak_rate,
    #PNab_rate,
    #PCab_rate

    #Jrel_inf_sensitivity
    #Jrel_infp_sensitivity
    #thl_rate

    #mechanical parameters
    # ku_rate, kuw_rate, kws_rate
    # ktrpn, ntrpn, Trpn50_rate , DO NOT SCALE ntrpn!

    # mechanical, unsure which
    # gammaw_rate, gammas_rate -> gammawu_rate, gammasu_rate

    #mehanical implicit change (NOT ADDED)
    # kb_rate, kwu_rate, ksu_rate


    init_values = np.array(
        [
            1.018,
            1.414,
            1.119,
            1.648,
            2.274,
            0,
            1.8,
            5.4,
            140.0,
            96485.0,
            8314.0,
            310.0,
            0.01,
            0.0011,
            0.99,
            31,
            200.0,
            0.02,
            1.0,
            0.6,
            0.002,
            1000.0,
            75.0,
            2.0,
            4.75,
            2.3,
            -2.4,
            25,
            120,
            0.35,
            1,
            0.805,
            0,
            1,
            200,
            20,
            0.0085,
            0.615,
            0,
            0.1,
            0.04,
            0.182,
            0.012,
            1,
            1,
            2.4,
            2,
            2.1,
            9.1,
            7,
            2.23,
            0.25,
            0.5,
            0.05,
            0.0015,
            0.15,
            0.05,
            0.00068,
            0.01833,
            0.0008,
            0.00015,
            12.5,
            5000.0,
            1500000.0,
            15.0,
            5.0,
            88.12,
            0.167,
            0.5224,
            60000.0,
            60000.0,
            5000.0,
            1e-07,
            1.698e-07,
            0.5,
            0.3582,
            1.698e-07,
            9.073,
            27.78,
            224.0,
            292.0,
            0.05,
            9.8,
            30,
            -0.155,
            4.2,
            182.4,
            949.5,
            39.4,
            687.2,
            79300.0,
            1899.0,
            40.0,
            639.0,
            1.0,
            0.003,
            3.75e-10,
            2.5e-08,
            0.0005,
            -10,
            1.097904761904762,
            0.006,
            1.1,
            -80.0,
            0.5,
            1.124,
            0.047,
            0.0087,
            0.00087,
            0.05,
            10.0,
            0.00238,
            0.8,
            0.0005,
            0.07,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
        ],
        dtype=np.float_,
    )

    # Parameter indices and limit checker
    param_ind = dict(
        [
            ("scale_ICaL", 0),
            ("scale_IK1", 1),
            ("scale_IKr", 2),
            ("scale_IKs", 3),
            ("scale_INaL", 4),
            ("celltype", 5),
            ("cao", 6),
            ("ko", 7),
            ("nao", 8),
            ("F", 9),
            ("R", 10),
            ("T", 11),
            ("L", 12),
            ("rad", 13),
            ("Ahf", 14),
            ("GNa", 15),
            ("thL", 16),
            ("Gto", 17),
            ("delta_epi", 18),
            ("Aff", 19),
            ("Kmn", 20),
            ("k2n", 21),
            ("tjca", 22),
            ("zca", 23),
            ("bt", 24),
            ("Beta0", 25),
            ("Beta1", 26),
            ("Tot_A", 27),
            ("Tref", 28),
            ("Trpn50", 29),
            ("calib", 30),
            ("cat50_ref", 31),
            ("dLambda", 32),
            ("emcoupling", 33),
            ("etal", 34),
            ("etas", 35),
            ("gammas", 36),
            ("gammaw", 37),
            ("isacs", 38),
            ("ktrpn", 39),
            ("ku", 40),
            ("kuw", 41),
            ("kws", 42),
            ("lmbda", 43),
            ("mode", 44),
            ("ntm", 45),
            ("ntrpn", 46),
            ("p_a", 47),
            ("p_b", 48),
            ("p_k", 49),
            ("phi", 50),
            ("rs", 51),
            ("rw", 52),
            ("CaMKo", 53),
            ("KmCaM", 54),
            ("KmCaMK", 55),
            ("aCaMK", 56),
            ("bCaMK", 57),
            ("PKNa", 58),
            ("Gncx", 59),
            ("KmCaAct", 60),
            ("kasymm", 61),
            ("kcaoff", 62),
            ("kcaon", 63),
            ("kna1", 64),
            ("kna2", 65),
            ("kna3", 66),
            ("qca", 67),
            ("qna", 68),
            ("wca", 69),
            ("wna", 70),
            ("wnaca", 71),
            ("H", 72),
            ("Khp", 73),
            ("Kki", 74),
            ("Kko", 75),
            ("Kmgatp", 76),
            ("Knai0", 77),
            ("Knao0", 78),
            ("Knap", 79),
            ("Kxkur", 80),
            ("MgADP", 81),
            ("MgATP", 82),
            ("Pnak", 83),
            ("delta", 84),
            ("eP", 85),
            ("k1m", 86),
            ("k1p", 87),
            ("k2m", 88),
            ("k2p", 89),
            ("k3m", 90),
            ("k3p", 91),
            ("k4m", 92),
            ("k4p", 93),
            ("zk", 94),
            ("GKb", 95),
            ("PNab", 96),
            ("PCab", 97),
            ("GpCa", 98),
            ("Esac_ns", 99),
            ("Gsac_k", 100),
            ("Gsac_ns", 101),
            ("lambda_max", 102),
            ("amp", 103),
            ("duration", 104),
            ("BSLmax", 105),
            ("BSRmax", 106),
            ("KmBSL", 107),
            ("KmBSR", 108),
            ("cmdnmax", 109),
            ("csqnmax", 110),
            ("kmcmdn", 111),
            ("kmcsqn", 112),
            ("kmtrpn", 113),
            ("trpnmax", 114),
            ("GNa_rate", 115),
            ("Gto_rate", 116),
            ("GKr_rate", 117),
            ("GKs_rate", 118),
            ("GK1_rate", 119),
            ("Gncx_rate", 120),
            ("GKb_rate", 121),
            ("GpCa_rate", 122),
            ("GNaL_rate", 123),
            ("Jleak_rate", 124),
            ("Jserca_rate", 125),
            ("CaMKa_rate", 126),
            ("Pnak_rate", 127),
            ("Pnab_rate", 128),
            ("Pcab_rate", 129),
            ("thl_rate", 130),
            ("Jrel_inf_sensitivity", 131),
            ("Jrel_infp_sensitivity", 132),
            ("ku_rate", 133),
            ("kuw_rate", 134),
            ("kws_rate", 135),
            ("ktrpn_rate", 136),
            ("ntrpn_rate", 137),
            ("Trpn50_rate", 138),
            ("gammaw_rate", 139),
            ("gammas_rate", 140),
        ]
    )

    for param_name, value in values.items():
        if param_name not in param_ind:
            raise ValueError("{0} is not a parameter.".format(param_name))
        ind = param_ind[param_name]

        # Assign value
        init_values[ind] = value

    return init_values


def state_indices(*states):
    """
    State indices
    """
    state_inds = dict(
        [
            ("CaMKt", 0),
            ("m", 1),
            ("hf", 2),
            ("hs", 3),
            ("j", 4),
            ("hsp", 5),
            ("jp", 6),
            ("mL", 7),
            ("hL", 8),
            ("hLp", 9),
            ("a", 10),
            ("iF", 11),
            ("iS", 12),
            ("ap", 13),
            ("iFp", 14),
            ("iSp", 15),
            ("d", 16),
            ("ff", 17),
            ("fs", 18),
            ("fcaf", 19),
            ("fcas", 20),
            ("jca", 21),
            ("ffp", 22),
            ("fcafp", 23),
            ("nca", 24),
            ("xrf", 25),
            ("xrs", 26),
            ("xs1", 27),
            ("xs2", 28),
            ("xk1", 29),
            ("v", 30),
            ("Jrelnp", 31),
            ("Jrelp", 32),
            ("nai", 33),
            ("nass", 34),
            ("ki", 35),
            ("kss", 36),
            ("cass", 37),
            ("cansr", 38),
            ("cajsr", 39),
            ("XS", 40),
            ("XW", 41),
            ("CaTrpn", 42),
            ("TmB", 43),
            ("Zetas", 44),
            ("Zetaw", 45),
            ("Cd", 46),
            ("cai", 47),
        ]
    )

    indices = []
    for state in states:
        if state not in state_inds:
            raise ValueError("Unknown state: '{0}'".format(state))
        indices.append(state_inds[state])
    if len(indices) > 1:
        return indices
    else:
        return indices[0]


def parameter_indices(*params):
    """
    Parameter indices
    """
    param_inds = dict(
        [
            ("scale_ICaL", 0),
            ("scale_IK1", 1),
            ("scale_IKr", 2),
            ("scale_IKs", 3),
            ("scale_INaL", 4),
            ("celltype", 5),
            ("cao", 6),
            ("ko", 7),
            ("nao", 8),
            ("F", 9),
            ("R", 10),
            ("T", 11),
            ("L", 12),
            ("rad", 13),
            ("Ahf", 14),
            ("GNa", 15),
            ("thL", 16),
            ("Gto", 17),
            ("delta_epi", 18),
            ("Aff", 19),
            ("Kmn", 20),
            ("k2n", 21),
            ("tjca", 22),
            ("zca", 23),
            ("bt", 24),
            ("Beta0", 25),
            ("Beta1", 26),
            ("Tot_A", 27),
            ("Tref", 28),
            ("Trpn50", 29),
            ("calib", 30),
            ("cat50_ref", 31),
            ("dLambda", 32),
            ("emcoupling", 33),
            ("etal", 34),
            ("etas", 35),
            ("gammas", 36),
            ("gammaw", 37),
            ("isacs", 38),
            ("ktrpn", 39),
            ("ku", 40),
            ("kuw", 41),
            ("kws", 42),
            ("lmbda", 43),
            ("mode", 44),
            ("ntm", 45),
            ("ntrpn", 46),
            ("p_a", 47),
            ("p_b", 48),
            ("p_k", 49),
            ("phi", 50),
            ("rs", 51),
            ("rw", 52),
            ("CaMKo", 53),
            ("KmCaM", 54),
            ("KmCaMK", 55),
            ("aCaMK", 56),
            ("bCaMK", 57),
            ("PKNa", 58),
            ("Gncx", 59),
            ("KmCaAct", 60),
            ("kasymm", 61),
            ("kcaoff", 62),
            ("kcaon", 63),
            ("kna1", 64),
            ("kna2", 65),
            ("kna3", 66),
            ("qca", 67),
            ("qna", 68),
            ("wca", 69),
            ("wna", 70),
            ("wnaca", 71),
            ("H", 72),
            ("Khp", 73),
            ("Kki", 74),
            ("Kko", 75),
            ("Kmgatp", 76),
            ("Knai0", 77),
            ("Knao0", 78),
            ("Knap", 79),
            ("Kxkur", 80),
            ("MgADP", 81),
            ("MgATP", 82),
            ("Pnak", 83),
            ("delta", 84),
            ("eP", 85),
            ("k1m", 86),
            ("k1p", 87),
            ("k2m", 88),
            ("k2p", 89),
            ("k3m", 90),
            ("k3p", 91),
            ("k4m", 92),
            ("k4p", 93),
            ("zk", 94),
            ("GKb", 95),
            ("PNab", 96),
            ("PCab", 97),
            ("GpCa", 98),
            ("Esac_ns", 99),
            ("Gsac_k", 100),
            ("Gsac_ns", 101),
            ("lambda_max", 102),
            ("amp", 103),
            ("duration", 104),
            ("BSLmax", 105),
            ("BSRmax", 106),
            ("KmBSL", 107),
            ("KmBSR", 108),
            ("cmdnmax", 109),
            ("csqnmax", 110),
            ("kmcmdn", 111),
            ("kmcsqn", 112),
            ("kmtrpn", 113),
            ("trpnmax", 114),
            ("GNa_rate", 115),
            ("Gto_rate", 116),
            ("GKr_rate", 117),
            ("GKs_rate", 118),
            ("GK1_rate", 119),
            ("Gncx_rate", 120),
            ("GKb_rate", 121),
            ("GpCa_rate", 122),
            ("GNaL_rate", 123),
            ("Jleak_rate", 124),
            ("Jserca_rate", 125),
            ("CaMKa_rate", 126),
            ("Pnak_rate", 127),
            ("Pnab_rate", 128),
            ("Pcab_rate", 129),
            ("thl_rate", 130),
            ("Jrel_inf_sensitivity", 131),
            ("Jrel_infp_sensitivity", 132),
            ("ku_rate", 133),
            ("kuw_rate", 134),
            ("kws_rate", 135),
            ("ktrpn_rate", 136),
            ("ntrpn_rate", 137),
            ("Trpn50_rate", 138),
            ("gammaw_rate", 139),
            ("gammas_rate", 140),
        ]
    )

    indices = []
    for param in params:
        if param not in param_inds:
            raise ValueError("Unknown param: '{0}'".format(param))
        indices.append(param_inds[param])
    if len(indices) > 1:
        return indices
    else:
        return indices[0]


def monitor_indices(*monitored):
    """
    Monitor indices
    """
    monitor_inds = dict(
        [
            ("vcell", 0),
            ("Ageo", 1),
            ("Acap", 2),
            ("vmyo", 3),
            ("vnsr", 4),
            ("vjsr", 5),
            ("vss", 6),
            ("CaMKb", 7),
            ("CaMKa", 8),
            ("mss", 9),
            ("tm", 10),
            ("hss", 11),
            ("thf", 12),
            ("ths", 13),
            ("Ahs", 14),
            ("h", 15),
            ("jss", 16),
            ("tj", 17),
            ("hssp", 18),
            ("thsp", 19),
            ("hp", 20),
            ("tjp", 21),
            ("fINap", 22),
            ("INa", 23),
            ("mLss", 24),
            ("tmL", 25),
            ("hLss", 26),
            ("hLssp", 27),
            ("thLp", 28),
            ("GNaL", 29),
            ("fINaLp", 30),
            ("INaL", 31),
            ("ass", 32),
            ("ta", 33),
            ("iss", 34),
            ("tiF", 35),
            ("tiS", 36),
            ("AiF", 37),
            ("AiS", 38),
            ("i", 39),
            ("assp", 40),
            ("dti_develop", 41),
            ("dti_recover", 42),
            ("tiFp", 43),
            ("tiSp", 44),
            ("ip", 45),
            ("fItop", 46),
            ("Ito", 47),
            ("dss", 48),
            ("td", 49),
            ("fss", 50),
            ("tff", 51),
            ("tfs", 52),
            ("Afs", 53),
            ("f", 54),
            ("fcass", 55),
            ("tfcaf", 56),
            ("tfcas", 57),
            ("Afcaf", 58),
            ("Afcas", 59),
            ("fca", 60),
            ("tffp", 61),
            ("fp", 62),
            ("tfcafp", 63),
            ("fcap", 64),
            ("km2n", 65),
            ("anca", 66),
            ("PhiCaL", 67),
            ("PhiCaNa", 68),
            ("PhiCaK", 69),
            ("PCa", 70),
            ("PCap", 71),
            ("PCaNa", 72),
            ("PCaK", 73),
            ("PCaNap", 74),
            ("PCaKp", 75),
            ("fICaLp", 76),
            ("ICaL", 77),
            ("ICaNa", 78),
            ("ICaK", 79),
            ("xrss", 80),
            ("txrf", 81),
            ("txrs", 82),
            ("Axrf", 83),
            ("Axrs", 84),
            ("xr", 85),
            ("rkr", 86),
            ("GKr", 87),
            ("IKr", 88),
            ("xs1ss", 89),
            ("txs1", 90),
            ("xs2ss", 91),
            ("txs2", 92),
            ("KsCa", 93),
            ("GKs", 94),
            ("IKs", 95),
            ("xk1ss", 96),
            ("txk1", 97),
            ("rk1", 98),
            ("GK1", 99),
            ("IK1", 100),
            ("a_rel", 101),
            ("Jrel_inf", 102),
            ("tau_rel_tmp", 103),
            ("tau_rel", 104),
            ("btp", 105),
            ("a_relp", 106),
            ("Jrel_infp", 107),
            ("tau_relp_tmp", 108),
            ("tau_relp", 109),
            ("fJrelp", 110),
            ("Jrel", 111),
            ("Bcass", 112),
            ("Bcajsr", 113),
            ("XS_max", 114),
            ("XW_max", 115),
            ("CaTrpn_max", 116),
            ("kwu", 117),
            ("ksu", 118),
            ("Aw", 119),
            ("As", 120),
            ("cw", 121),
            ("cs", 122),
            ("lambda_min12", 123),
            ("lambda_min087", 124),
            ("h_lambda_prima", 125),
            ("h_lambda", 126),
            ("XU", 127),
            ("gammawu", 128),
            ("gammasu", 129),
            ("cat50", 130),
            ("kb", 131),
            ("Ta", 132),
            ("C", 133),
            ("dCd", 134),
            ("eta", 135),
            ("Fd", 136),
            ("F1", 137),
            ("Tp", 138),
            ("Ttot", 139),
            ("Bcai", 140),
            ("J_TRPN", 141),
            ("ENa", 142),
            ("EK", 143),
            ("EKs", 144),
            ("vffrt", 145),
            ("vfrt", 146),
            ("hca", 147),
            ("hna", 148),
            ("h1_i", 149),
            ("h2_i", 150),
            ("h3_i", 151),
            ("h4_i", 152),
            ("h5_i", 153),
            ("h6_i", 154),
            ("h7_i", 155),
            ("h8_i", 156),
            ("h9_i", 157),
            ("h10_i", 158),
            ("h11_i", 159),
            ("h12_i", 160),
            ("k1_i", 161),
            ("k2_i", 162),
            ("k3p_i", 163),
            ("k3pp_i", 164),
            ("k3_i", 165),
            ("k4p_i", 166),
            ("k4pp_i", 167),
            ("k4_i", 168),
            ("k5_i", 169),
            ("k6_i", 170),
            ("k7_i", 171),
            ("k8_i", 172),
            ("x1_i", 173),
            ("x2_i", 174),
            ("x3_i", 175),
            ("x4_i", 176),
            ("E1_i", 177),
            ("E2_i", 178),
            ("E3_i", 179),
            ("E4_i", 180),
            ("allo_i", 181),
            ("zna", 182),
            ("JncxNa_i", 183),
            ("JncxCa_i", 184),
            ("INaCa_i", 185),
            ("h1", 186),
            ("h2", 187),
            ("h3", 188),
            ("h4", 189),
            ("h5", 190),
            ("h6", 191),
            ("h7", 192),
            ("h8", 193),
            ("h9", 194),
            ("h10", 195),
            ("h11", 196),
            ("h12", 197),
            ("k1", 198),
            ("k2", 199),
            ("k3p_ss", 200),
            ("k3pp", 201),
            ("k3", 202),
            ("k4p_ss", 203),
            ("k4pp", 204),
            ("k4", 205),
            ("k5", 206),
            ("k6", 207),
            ("k7", 208),
            ("k8", 209),
            ("x1_ss", 210),
            ("x2_ss", 211),
            ("x3_ss", 212),
            ("x4_ss", 213),
            ("E1_ss", 214),
            ("E2_ss", 215),
            ("E3_ss", 216),
            ("E4_ss", 217),
            ("allo_ss", 218),
            ("JncxNa_ss", 219),
            ("JncxCa_ss", 220),
            ("INaCa_ss", 221),
            ("Knai", 222),
            ("Knao", 223),
            ("P", 224),
            ("a1", 225),
            ("b1", 226),
            ("a2", 227),
            ("b2", 228),
            ("a3", 229),
            ("b3", 230),
            ("a4", 231),
            ("b4", 232),
            ("x1", 233),
            ("x2", 234),
            ("x3", 235),
            ("x4", 236),
            ("E1", 237),
            ("E2", 238),
            ("E3", 239),
            ("E4", 240),
            ("JnakNa", 241),
            ("JnakK", 242),
            ("INaK", 243),
            ("xkb", 244),
            ("IKb", 245),
            ("INab", 246),
            ("ICab", 247),
            ("IpCa", 248),
            ("Isac_P_ns", 249),
            ("Isac_P_k", 250),
            ("Istim", 251),
            ("JdiffNa", 252),
            ("JdiffK", 253),
            ("Jdiff", 254),
            ("Jupnp", 255),
            ("Jupp", 256),
            ("fJupp", 257),
            ("Jleak", 258),
            ("Jup", 259),
            ("Jtr", 260),
            ("dCaMKt_dt", 261),
            ("dm_dt", 262),
            ("dhf_dt", 263),
            ("dhs_dt", 264),
            ("dj_dt", 265),
            ("dhsp_dt", 266),
            ("djp_dt", 267),
            ("dmL_dt", 268),
            ("dhL_dt", 269),
            ("dhLp_dt", 270),
            ("da_dt", 271),
            ("diF_dt", 272),
            ("diS_dt", 273),
            ("dap_dt", 274),
            ("diFp_dt", 275),
            ("diSp_dt", 276),
            ("dd_dt", 277),
            ("dff_dt", 278),
            ("dfs_dt", 279),
            ("dfcaf_dt", 280),
            ("dfcas_dt", 281),
            ("djca_dt", 282),
            ("dffp_dt", 283),
            ("dfcafp_dt", 284),
            ("dnca_dt", 285),
            ("dxrf_dt", 286),
            ("dxrs_dt", 287),
            ("dxs1_dt", 288),
            ("dxs2_dt", 289),
            ("dxk1_dt", 290),
            ("dv_dt", 291),
            ("dJrelnp_dt", 292),
            ("dJrelp_dt", 293),
            ("dnai_dt", 294),
            ("dnass_dt", 295),
            ("dki_dt", 296),
            ("dkss_dt", 297),
            ("dcass_dt", 298),
            ("dcansr_dt", 299),
            ("dcajsr_dt", 300),
            ("dXS_dt", 301),
            ("dXW_dt", 302),
            ("dCaTrpn_dt", 303),
            ("dTmB_dt", 304),
            ("dZetas_dt", 305),
            ("dZetaw_dt", 306),
            ("dCd_dt", 307),
            ("dcai_dt", 308),
        ]
    )

    indices = []
    for monitor in monitored:
        if monitor not in monitor_inds:
            raise ValueError("Unknown monitored: '{0}'".format(monitor))
        indices.append(monitor_inds[monitor])
    if len(indices) > 1:
        return indices
    else:
        return indices[0]


def rhs(states, t, parameters, values=None):
    """
    Compute the right hand side of the ORdmm_Land_em_coupling ODE
    """

    # Assign states
    assert len(states) == 48
    (
        CaMKt,
        m,
        hf,
        hs,
        j,
        hsp,
        jp,
        mL,
        hL,
        hLp,
        a,
        iF,
        iS,
        ap,
        iFp,
        iSp,
        d,
        ff,
        fs,
        fcaf,
        fcas,
        jca,
        ffp,
        fcafp,
        nca,
        xrf,
        xrs,
        xs1,
        xs2,
        xk1,
        v,
        Jrelnp,
        Jrelp,
        nai,
        nass,
        ki,
        kss,
        cass,
        cansr,
        cajsr,
        XS,
        XW,
        CaTrpn,
        TmB,
        Zetas,
        Zetaw,
        Cd,
        cai,
    ) = states

    # Assign parameters
    assert len(parameters) == 141
    scale_ICaL = parameters[0]
    scale_IK1 = parameters[1]
    scale_IKr = parameters[2]
    scale_IKs = parameters[3]
    scale_INaL = parameters[4]
    celltype = parameters[5]
    cao = parameters[6]
    ko = parameters[7]
    nao = parameters[8]
    F = parameters[9]
    R = parameters[10]
    T = parameters[11]
    L = parameters[12]
    rad = parameters[13]
    Ahf = parameters[14]
    GNa = parameters[15]
    thL = parameters[16]
    Gto = parameters[17]
    delta_epi = parameters[18]
    Aff = parameters[19]
    Kmn = parameters[20]
    k2n = parameters[21]
    tjca = parameters[22]
    zca = parameters[23]
    bt = parameters[24]
    Beta1 = parameters[26]
    Tot_A = parameters[27]
    Trpn50 = parameters[29]
    cat50_ref = parameters[31]
    dLambda = parameters[32]
    etal = parameters[34]
    etas = parameters[35]
    gammas = parameters[36]
    gammaw = parameters[37]
    ktrpn = parameters[39]
    ku = parameters[40]
    kuw = parameters[41]
    kws = parameters[42]
    lmbda = parameters[43]
    ntm = parameters[45]
    ntrpn = parameters[46]
    p_k = parameters[49]
    phi = parameters[50]
    rs = parameters[51]
    rw = parameters[52]
    CaMKo = parameters[53]
    KmCaM = parameters[54]
    KmCaMK = parameters[55]
    aCaMK = parameters[56]
    bCaMK = parameters[57]
    PKNa = parameters[58]
    Gncx = parameters[59]
    KmCaAct = parameters[60]
    kasymm = parameters[61]
    kcaoff = parameters[62]
    kcaon = parameters[63]
    kna1 = parameters[64]
    kna2 = parameters[65]
    kna3 = parameters[66]
    qca = parameters[67]
    qna = parameters[68]
    wca = parameters[69]
    wna = parameters[70]
    wnaca = parameters[71]
    H = parameters[72]
    Khp = parameters[73]
    Kki = parameters[74]
    Kko = parameters[75]
    Kmgatp = parameters[76]
    Knai0 = parameters[77]
    Knao0 = parameters[78]
    Knap = parameters[79]
    Kxkur = parameters[80]
    MgADP = parameters[81]
    MgATP = parameters[82]
    Pnak = parameters[83]
    delta = parameters[84]
    eP = parameters[85]
    k1m = parameters[86]
    k1p = parameters[87]
    k2m = parameters[88]
    k2p = parameters[89]
    k3m = parameters[90]
    k3p = parameters[91]
    k4m = parameters[92]
    k4p = parameters[93]
    zk = parameters[94]
    GKb = parameters[95]
    PNab = parameters[96]
    PCab = parameters[97]
    GpCa = parameters[98]
    amp = parameters[103]
    duration = parameters[104]
    BSLmax = parameters[105]
    BSRmax = parameters[106]
    KmBSL = parameters[107]
    KmBSR = parameters[108]
    cmdnmax = parameters[109]
    csqnmax = parameters[110]
    kmcmdn = parameters[111]
    kmcsqn = parameters[112]
    trpnmax = parameters[114]
    GNa_rate = parameters[115]
    Gto_rate = parameters[116]
    GKr_rate = parameters[117]
    GKs_rate = parameters[118]
    GK1_rate = parameters[119]
    Gncx_rate = parameters[120]
    GKb_rate = parameters[121]
    GpCa_rate = parameters[122]
    GNaL_rate = parameters[123]
    Jleak_rate = parameters[124]
    Jserca_rate = parameters[125]
    CaMKa_rate = parameters[126]
    Pnak_rate = parameters[127]
    Pnab_rate = parameters[128]
    Pcab_rate = parameters[129]
    thl_rate = parameters[130]
    Jrel_inf_sensitivity = parameters[131]
    Jrel_infp_sensitivity = parameters[132]
    ku_rate = parameters[133]
    kuw_rate = parameters[134]
    kws_rate = parameters[135]
    ktrpn_rate = parameters[136]
    ntrpn_rate = parameters[137]
    Trpn50_rate = parameters[138]
    gammaw_rate = parameters[139]
    gammas_rate = parameters[140]


    # Init return args
    if values is None:
        values = np.zeros((48,), dtype=np.float_)
    else:
        assert isinstance(values, np.ndarray) and values.shape == (48,)

    # Expressions for the cell geometry component
    vcell = 3140.0 * L * (rad * rad)
    Ageo = 6.28 * (rad * rad) + 6.28 * L * rad
    Acap = 2 * Ageo
    vmyo = 0.68 * vcell
    vnsr = 0.0552 * vcell
    vjsr = 0.0048 * vcell
    vss = 0.02 * vcell

    # Expressions for the CaMKt component
    CaMKb = CaMKo * (1.0 - CaMKt) / (1.0 + KmCaM / cass)
    CaMKa = CaMKb + CaMKt
    tmp_CaMKa = CaMKa*CaMKa_rate
    values[0] = -bCaMK * CaMKt + aCaMK * (CaMKb + CaMKt) * CaMKb

    # Expressions for the reversal potentials component
    ENa = R * T * math.log(nao / nai) / F
    EK = R * T * math.log(ko / ki) / F
    EKs = R * T * math.log((ko + PKNa * nao) / (PKNa * nai + ki)) / F
    vffrt = (F * F) * v / (R * T)
    vfrt = F * v / (R * T)

    # Expressions for the I_Na component
    mss = 1.0 / (1.0 + 0.0014599788446489682 * math.exp(-0.13333333333333333 * v))
    tm = 1.0 / (
        9.454904638564724 * math.exp(0.02876042565429968 * v)
        + 1.9314113558536928e-05 * math.exp(-0.16792611251049538 * v)
    )
    values[1] = (-m + mss) / tm
    hss = 1.0 / (1 + 302724.605401998 * math.exp(0.1607717041800643 * v))
    thf = 1.0 / (
        1.183856958289087e-05 * math.exp(-0.15910898965791567 * v)
        + 6.305549185817275 * math.exp(0.0493339911198816 * v)
    )
    ths = 1.0 / (
        0.005164670235381792 * math.exp(-0.035650623885918005 * v)
        + 0.36987619372096325 * math.exp(0.017649135192375574 * v)
    )
    Ahs = 1.0 - Ahf
    values[2] = (-hf + hss) / thf
    values[3] = (-hs + hss) / ths
    h = Ahf * hf + Ahs * hs
    jss = hss
    tj = 2.038 + 1.0 / (
        0.3131936394738773 * math.exp(0.02600780234070221 * v)
        + 1.1315282095590072e-07 * math.exp(-0.12075836251660427 * v)
    )
    values[4] = (-j + jss) / tj
    hssp = 1.0 / (1 + 820249.0921708513 * math.exp(0.1607717041800643 * v))
    thsp = 3.0 * ths
    values[5] = (-hsp + hssp) / thsp
    hp = Ahf * hf + Ahs * hsp
    tjp = 1.46 * tj
    values[6] = (-jp + jss) / tjp
    fINap = 1.0 / (1.0 + KmCaMK / tmp_CaMKa)
    tmp_GNa = GNa*GNa_rate
    INa = (
        tmp_GNa * math.pow(m, 3.0) * (-ENa + v) * ((1.0 - fINap) * h * j + fINap * hp * jp)
    )

    # Expressions for the INaL component
    mLss = 1.0 / (1.0 + 0.000291579585635531 * math.exp(-0.18996960486322187 * v))
    tmL = tm
    values[7] = (-mL + mLss) / tmL
    hLss = 1.0 / (1.0 + 120578.15595522427 * math.exp(0.13354700854700854 * v))
    tmp_thL = thL * thl_rate
    values[8] = (-hL + hLss) / tmp_thL
    hLssp = 1.0 / (1.0 + 275969.2903869871 * math.exp(0.13354700854700854 * v))
    thLp = 3.0 * tmp_thL
    values[9] = (-hLp + hLssp) / thLp
    GNaL = (0.0075 * scale_INaL) 
    tmp_GNaL = GNaL* GNaL_rate
    if celltype==1:
        tmp_GNaL = tmp_GNaL*0.6
    fINaLp = 1.0 / (1.0 + KmCaMK / tmp_CaMKa)
    INaL = (-ENa + v) * ((1.0 - fINaLp) * hL + fINaLp * hLp) * tmp_GNaL * mL

    # Expressions for the Ito component
    ass = 1.0 / (1.0 + 2.6316508161673635 * math.exp(-0.06747638326585695 * v))
    ta = 1.0515 / (
        1.0 / (1.2089 + 2.2621017070578837 * math.exp(-0.03403513787634354 * v))
        + 3.5 / (1.0 + 30.069572727397507 * math.exp(0.03403513787634354 * v))
    )
    values[10] = (-a + ass) / ta
    iss = 1.0 / (1.0 + 2194.970764538301 * math.exp(0.17510068289266328 * v))
    if celltype==1:
        delta_epi = 1.0 - (0.95/(1.0 + math.exp((v + 70.0)/5.0)))
    tiF = 4.562 + delta_epi / (
        0.14468698421272827 * math.exp(-0.01 * v)
        + 1.6300896349780942 * math.exp(0.06027727546714889 * v)
    )
    tiS = 23.62 + delta_epi / (
        0.00027617763953377436 * math.exp(-0.01693480101608806 * v)
        + 0.024208962804604526 * math.exp(0.12377769525931426 * v)
    )
    AiF = 1.0 / (1.0 + 0.24348537187522867 * math.exp(0.006613756613756614 * v))
    AiS = 1.0 - AiF
    values[11] = (-iF + iss) / tiF
    values[12] = (-iS + iss) / tiS
    i = AiF * iF + AiS * iS
    assp = 1.0 / (1.0 + 5.167428462230666 * math.exp(-0.06747638326585695 * v))
    values[13] = (-ap + assp) / ta
    dti_develop = 1.354 + 0.0001 / (
        2.6591269045230603e-05 * math.exp(0.06293266205160478 * v)
        + 4.5541779737128264e24 * math.exp(-4.642525533890436 * v)
    )
    dti_recover = 1.0 - 0.5 / (1.0 + 33.11545195869231 * math.exp(0.05 * v))
    tiFp = dti_develop * dti_recover * tiF
    tiSp = dti_develop * dti_recover * tiS
    values[14] = (-iFp + iss) / tiFp
    values[15] = (-iSp + iss) / tiSp
    ip = AiF * iFp + AiS * iSp
    fItop = 1.0 / (1.0 + KmCaMK / tmp_CaMKa)
    tmp_Gto = Gto*Gto_rate
    if celltype==1:
        tmp_Gto = tmp_Gto*4.0
    elif celltype==2:
        tmp_Gto = tmp_Gto*4.0
    Ito = tmp_Gto * (-EK + v) * ((1.0 - fItop) * a * i + ap * fItop * ip)

    # Expressions for the ICaL ICaNa ICaK component
    dss = 1.0 / (1.0 + 0.39398514226669484 * math.exp(-0.23640661938534277 * v))
    td = 0.6 + 1.0 / (
        3.5254214873653824 * math.exp(0.09 * v)
        + 0.7408182206817179 * math.exp(-0.05 * v)
    )
    values[16] = (-d + dss) / td
    fss = 1.0 / (1.0 + 199.86038496778565 * math.exp(0.27056277056277056 * v))
    tff = 7.0 + 1.0 / (
        0.03325075244518792 * math.exp(0.1 * v)
        + 0.0006090087745647571 * math.exp(-0.1 * v)
    )
    tfs = 1000.0 + 1.0 / (
        1.0027667890106652e-05 * math.exp(-0.25 * v)
        + 8.053415618124885e-05 * math.exp(0.16666666666666666 * v)
    )
    Afs = 1.0 - Aff
    values[17] = (-ff + fss) / tff
    values[18] = (-fs + fss) / tfs
    f = Aff * ff + Afs * fs
    fcass = fss
    tfcaf = 7.0 + 1.0 / (
        0.0708317980974062 * math.exp(-0.14285714285714285 * v)
        + 0.02258872488031037 * math.exp(0.14285714285714285 * v)
    )
    tfcas = 100.0 + 1.0 / (
        0.00012 * math.exp(0.14285714285714285 * v)
        + 0.00012 * math.exp(-0.3333333333333333 * v)
    )
    Afcaf = 0.3 + 0.6 / (1.0 + 0.36787944117144233 * math.exp(0.1 * v))
    Afcas = 1.0 - Afcaf
    values[19] = (-fcaf + fcass) / tfcaf
    values[20] = (-fcas + fcass) / tfcas
    fca = Afcaf * fcaf + Afcas * fcas
    values[21] = (-jca + fcass) / tjca
    tffp = 2.5 * tff
    values[22] = (-ffp + fss) / tffp
    fp = Aff * ffp + Afs * fs
    tfcafp = 2.5 * tfcaf
    values[23] = (-fcafp + fcass) / tfcafp
    fcap = Afcaf * fcafp + Afcas * fcas
    km2n = 1.0 * jca
    anca = 1.0 / (math.pow(1.0 + Kmn / cass, 4.0) + k2n / km2n)
    values[24] = k2n * anca - km2n * nca
    PhiCaL = (
        4.0
        * (-0.341 * cao + cass * math.exp(2.0 * vfrt))
        * vffrt
        / (-1.0 + math.exp(2.0 * vfrt))
    )
    PhiCaNa = (
        1.0
        * (-0.75 * nao + 0.75 * math.exp(1.0 * vfrt) * nass)
        * vffrt
        / (-1.0 + math.exp(1.0 * vfrt))
    )
    PhiCaK = (
        1.0
        * (-0.75 * ko + 0.75 * math.exp(1.0 * vfrt) * kss)
        * vffrt
        / (-1.0 + math.exp(1.0 * vfrt))
    )
    PCa = 0.0001 * scale_ICaL
    if celltype==1:
        PCa = PCa*1.2
    elif celltype==2:
        PCa = PCa*2.5
    PCap = 1.1 * PCa
    PCaNa = 0.00125 * PCa
    PCaK = 0.0003574 * PCa
    PCaNap = 0.00125 * PCap
    PCaKp = 0.0003574 * PCap
    fICaLp = 1.0 / (1.0 + KmCaMK / tmp_CaMKa)
    ICaL = (1.0 - fICaLp) * ((1.0 - nca) * f + fca * jca * nca) * PCa * PhiCaL * d + (
        (1.0 - nca) * fp + fcap * jca * nca
    ) * PCap * PhiCaL * d * fICaLp
    ICaNa = (
        (1.0 - fICaLp) * ((1.0 - nca) * f + fca * jca * nca) * PCaNa * PhiCaNa * d
        + ((1.0 - nca) * fp + fcap * jca * nca) * PCaNap * PhiCaNa * d * fICaLp
    )
    ICaK = (1.0 - fICaLp) * ((1.0 - nca) * f + fca * jca * nca) * PCaK * PhiCaK * d + (
        (1.0 - nca) * fp + fcap * jca * nca
    ) * PCaKp * PhiCaK * d * fICaLp

    # Expressions for the IKr component
    xrss = 1.0 / (1.0 + 0.29287308872377504 * math.exp(-0.14729709824716453 * v))
    txrf = 12.98 + 1.0 / (
        0.0001020239312894894 * math.exp(0.25846471956577927 * v)
        + 0.00042992960891929087 * math.exp(-0.04906771344455348 * v)
    )
    txrs = 1.865 + 1.0 / (
        0.0005922420036809394 * math.exp(0.13596193065941536 * v)
        + 3.549966111802463e-05 * math.exp(-0.03855050115651503 * v)
    )
    Axrf = 1.0 / (1.0 + 4.197299094734718 * math.exp(0.02617115938236064 * v))
    Axrs = 1.0 - Axrf
    values[25] = (-xrf + xrss) / txrf
    values[26] = (-xrs + xrss) / txrs
    xr = Axrf * xrf + Axrs * xrs
    rkr = 1.0 / (
        (1.0 + 2.0820090840784555 * math.exp(0.013333333333333334 * v))
        * (1.0 + 0.7165313105737893 * math.exp(0.03333333333333333 * v))
    )
    GKr = (0.046 * scale_IKr) * GKr_rate
    if celltype==1:
        GKr = GKr*1.3
    elif celltype==2:
        GKr = GKr*0.8
    IKr = 0.4303314829119352 * math.sqrt(ko) * (-EK + v) * GKr * rkr * xr

    # Expressions for the IKs component
    xs1ss = 1.0 / (1.0 + 0.27288596035656526 * math.exp(-0.11195700850873264 * v))
    txs1 = 817.3 + 1.0 / (
        0.003504067763074858 * math.exp(0.056179775280898875 * v)
        + 0.0005184809083581659 * math.exp(-0.004347826086956522 * v)
    )
    values[27] = (-xs1 + xs1ss) / txs1
    xs2ss = xs1ss
    txs2 = 1.0 / (
        0.0022561357010639103 * math.exp(-0.03225806451612903 * v)
        + 0.0008208499862389881 * math.exp(0.05 * v)
    )
    values[28] = (-xs2 + xs2ss) / txs2
    KsCa = 1.0 + 0.6 / (1.0 + 6.481821026062645e-07 * math.pow(1.0 / cai, 1.4))
    GKs = (0.0034 * scale_IKs) * GKs_rate
    if celltype==1:
        GKs = GKs*1.4
    IKs = (-EKs + v) * GKs * KsCa * xs1 * xs2
    xk1ss = 1.0 / (1.0 + math.exp((-144.59 - v - 2.5538 * ko) / (3.8115 + 1.5692 * ko)))
    txk1 = 122.2 / (
        0.0019352007631390235 * math.exp(-0.049115913555992145 * v)
        + 30.43364757524903 * math.exp(0.014423770373575654 * v)
    )
    values[29] = (-xk1 + xk1ss) / txk1
    rk1 = 1.0 / (
        1.0
        + 69220.6322106767
        * math.exp(0.10534077741493732 * v - 0.27388602127883704 * ko)
    )
    GK1 = (0.1908 * scale_IK1) 
    tmp_GK1 = GK1 * GK1_rate
    if celltype==1:
        tmp_GK1 = tmp_GK1*1.2
    elif celltype==2:
        tmp_GK1 = tmp_GK1*1.3
    IK1 = math.sqrt(ko) * (-EK + v) * tmp_GK1 * rk1 * xk1

    # Expressions for the INaCa_i component
    hca = math.exp(F * qca * v / (R * T))
    hna = math.exp(F * qna * v / (R * T))
    h1_i = 1 + (1 + hna) * nai / kna3
    h2_i = hna * nai / (kna3 * h1_i)
    h3_i = 1.0 / h1_i
    h4_i = 1.0 + (1 + nai / kna2) * nai / kna1
    h5_i = (nai * nai) / (kna1 * kna2 * h4_i)
    h6_i = 1.0 / h4_i
    h7_i = 1.0 + nao * (1.0 + 1.0 / hna) / kna3
    h8_i = nao / (kna3 * h7_i * hna)
    h9_i = 1.0 / h7_i
    h10_i = 1.0 + kasymm + nao * (1.0 + nao / kna2) / kna1
    h11_i = (nao * nao) / (kna1 * kna2 * h10_i)
    h12_i = 1.0 / h10_i
    k1_i = cao * kcaon * h12_i
    k2_i = kcaoff
    k3p_i = wca * h9_i
    k3pp_i = wnaca * h8_i
    k3_i = k3p_i + k3pp_i
    k4p_i = wca * h3_i / hca
    k4pp_i = wnaca * h2_i
    k4_i = k4p_i + k4pp_i
    k5_i = kcaoff
    k6_i = kcaon * cai * h6_i
    k7_i = wna * h2_i * h5_i
    k8_i = wna * h11_i * h8_i
    x1_i = (k2_i + k3_i) * k5_i * k7_i + (k6_i + k7_i) * k2_i * k4_i
    x2_i = (k1_i + k8_i) * k4_i * k6_i + (k4_i + k5_i) * k1_i * k7_i
    x3_i = (k2_i + k3_i) * k6_i * k8_i + (k6_i + k7_i) * k1_i * k3_i
    x4_i = (k1_i + k8_i) * k3_i * k5_i + (k4_i + k5_i) * k2_i * k8_i
    E1_i = x1_i / (x1_i + x2_i + x3_i + x4_i)
    E2_i = x2_i / (x1_i + x2_i + x3_i + x4_i)
    E3_i = x3_i / (x1_i + x2_i + x3_i + x4_i)
    E4_i = x4_i / (x1_i + x2_i + x3_i + x4_i)
    allo_i = 1.0 / (1.0 + math.pow(KmCaAct / cai, 2.0))
    zna = 1.0
    JncxNa_i = E3_i * k4pp_i - E2_i * k3pp_i + 3.0 * E4_i * k7_i - 3.0 * E1_i * k8_i
    JncxCa_i = E2_i * k2_i - E1_i * k1_i
    tmp_Gncx = Gncx * Gncx_rate
    if celltype==1:
        tmp_Gncx = tmp_Gncx*1.1
    elif celltype==2:
        tmp_Gncx = tmp_Gncx*1.4
    INaCa_i = 0.8 * tmp_Gncx * (zca * JncxCa_i + zna * JncxNa_i) * allo_i

    # Expressions for the INaCa_ss component
    h1 = 1 + (1 + hna) * nass / kna3
    h2 = hna * nass / (kna3 * h1)
    h3 = 1.0 / h1
    h4 = 1.0 + (1 + nass / kna2) * nass / kna1
    h5 = (nass * nass) / (kna1 * kna2 * h4)
    h6 = 1.0 / h4
    h7 = 1.0 + nao * (1.0 + 1.0 / hna) / kna3
    h8 = nao / (kna3 * h7 * hna)
    h9 = 1.0 / h7
    h10 = 1.0 + kasymm + nao * (1 + nao / kna2) / kna1
    h11 = (nao * nao) / (kna1 * kna2 * h10)
    h12 = 1.0 / h10
    k1 = cao * kcaon * h12
    k2 = kcaoff
    k3p_ss = wca * h9
    k3pp = wnaca * h8
    k3 = k3p_ss + k3pp
    k4p_ss = wca * h3 / hca
    k4pp = wnaca * h2
    k4 = k4p_ss + k4pp
    k5 = kcaoff
    k6 = kcaon * cass * h6
    k7 = wna * h2 * h5
    k8 = wna * h11 * h8
    x1_ss = (k2 + k3) * k5 * k7 + (k6 + k7) * k2 * k4
    x2_ss = (k1 + k8) * k4 * k6 + (k4 + k5) * k1 * k7
    x3_ss = (k2 + k3) * k6 * k8 + (k6 + k7) * k1 * k3
    x4_ss = (k1 + k8) * k3 * k5 + (k4 + k5) * k2 * k8
    E1_ss = x1_ss / (x1_ss + x2_ss + x3_ss + x4_ss)
    E2_ss = x2_ss / (x1_ss + x2_ss + x3_ss + x4_ss)
    E3_ss = x3_ss / (x1_ss + x2_ss + x3_ss + x4_ss)
    E4_ss = x4_ss / (x1_ss + x2_ss + x3_ss + x4_ss)
    allo_ss = 1.0 / (1.0 + math.pow(KmCaAct / cass, 2.0))
    JncxNa_ss = E3_ss * k4pp - E2_ss * k3pp + 3.0 * E4_ss * k7 - 3.0 * E1_ss * k8
    JncxCa_ss = E2_ss * k2 - E1_ss * k1
    INaCa_ss = 0.2 * tmp_Gncx * (zca * JncxCa_ss + zna * JncxNa_ss) * allo_ss

    # Expressions for the INaK component
    Knai = Knai0 * math.exp(0.3333333333333333 * F * delta * v / (R * T))
    Knao = Knao0 * math.exp(0.3333333333333333 * F * (1.0 - delta) * v / (R * T))
    P = eP / (1.0 + H / Khp + nai / Knap + ki / Kxkur)
    a1 = (
        k1p
        * math.pow(nai / Knai, 3.0)
        / (-1.0 + math.pow(1.0 + ki / Kki, 2.0) + math.pow(1.0 + nai / Knai, 3.0))
    )
    b1 = MgADP * k1m
    a2 = k2p
    b2 = (
        k2m
        * math.pow(nao / Knao, 3.0)
        / (-1.0 + math.pow(1.0 + ko / Kko, 2.0) + math.pow(1.0 + nao / Knao, 3.0))
    )
    a3 = (
        k3p
        * math.pow(ko / Kko, 2.0)
        / (-1.0 + math.pow(1.0 + ko / Kko, 2.0) + math.pow(1.0 + nao / Knao, 3.0))
    )
    b3 = H * k3m * P / (1.0 + MgATP / Kmgatp)
    a4 = MgATP * k4p / (Kmgatp * (1.0 + MgATP / Kmgatp))
    b4 = (
        k4m
        * math.pow(ki / Kki, 2.0)
        / (-1.0 + math.pow(1.0 + ki / Kki, 2.0) + math.pow(1.0 + nai / Knai, 3.0))
    )
    x1 = a1 * a2 * a4 + a1 * a2 * b3 + a2 * b3 * b4 + b2 * b3 * b4
    x2 = a1 * a2 * a3 + a2 * a3 * b4 + a3 * b1 * b4 + b1 * b2 * b4
    x3 = a2 * a3 * a4 + a3 * a4 * b1 + a4 * b1 * b2 + b1 * b2 * b3
    x4 = a1 * a3 * a4 + a1 * a4 * b2 + a1 * b2 * b3 + b2 * b3 * b4
    E1 = x1 / (x1 + x2 + x3 + x4)
    E2 = x2 / (x1 + x2 + x3 + x4)
    E3 = x3 / (x1 + x2 + x3 + x4)
    E4 = x4 / (x1 + x2 + x3 + x4)
    JnakNa = 3.0 * E1 * a3 - 3.0 * E2 * b3
    JnakK = 2.0 * E4 * b1 - 2.0 * E3 * a1
    tmp_Pnak = Pnak*Pnak_rate
    if celltype==1:
        tmp_Pnak = tmp_Pnak*0.9
    elif celltype==2:
        tmp_Pnak = tmp_Pnak*0.7
    INaK = tmp_Pnak * (zk * JnakK + zna * JnakNa)

    # Expressions for the IKb component
    xkb = 1.0 / (1.0 + 2.202363450949239 * math.exp(-0.05452562704471101 * v))
    tmp_GKb = GKb*GKb_rate
    if celltype==1:
        tmp_GKb = tmp_GKb*0.6
    IKb = tmp_GKb * (-EK + v) * xkb

    # Expressions for the INab component
    INab = (PNab*Pnab_rate) * (-nao + math.exp(vfrt) * nai) * vffrt / (-1.0 + math.exp(vfrt))

    # Expressions for the ICab component
    ICab = (
        4.0
        * (PCab*Pcab_rate)
        * (-0.341 * cao + cai * math.exp(2.0 * vfrt))
        * vffrt
        / (-1.0 + math.exp(2.0 * vfrt))
    )

    # Expressions for the IpCa component
    tmp_GpCa = GpCa*GpCa_rate
    IpCa = tmp_GpCa * cai / (0.0005 + cai)

    # Expressions for the Isac (Pueyo)--> ns + k component
    Isac_P_ns = 0
    Isac_P_k = 0

    # Expressions for the Istim component
    Istim = amp * (t <= duration)

    # Expressions for the membrane potential component
    values[30] = (
        -Isac_P_k
        - Isac_P_ns
        - ICaK
        - ICaL
        - ICaNa
        - ICab
        - IK1
        - IKb
        - IKr
        - IKs
        - INa
        - INaCa_i
        - INaCa_ss
        - INaK
        - INaL
        - INab
        - IpCa
        - Istim
        - Ito
    )

    # Expressions for the diffusion fluxes component
    JdiffNa = 0.5 * nass - 0.5 * nai
    JdiffK = 0.5 * kss - 0.5 * ki
    Jdiff = 5.0 * cass - 5.0 * cai

    # Expressions for the ryanodione receptor component
    a_rel = 0.5 * bt
    #Jrel_inf = -ICaL * a_rel / (1.0 + 25.62890625 * math.pow(1.0 / cajsr, 8.0))
    Jrel_inf = -ICaL * a_rel / (1.0 + math.pow((1.5*Jrel_inf_sensitivity) / cajsr, 8.0))
    if celltype==2:
        Jrel_inf = Jrel_inf*1.7
    tau_rel_tmp = bt / (1.0 + 0.0123 / cajsr)
    tau_rel = 0.001 if tau_rel_tmp < 0.001 else tau_rel_tmp
    values[31] = (-Jrelnp + Jrel_inf) / tau_rel
    btp = 1.25 * bt
    a_relp = 0.5 * btp
    #Jrel_infp = -ICaL * a_relp / (1.0 + 25.62890625 * math.pow(1.0 / cajsr, 8.0))
    Jrel_infp = -ICaL * a_relp / (1.0 + math.pow((1.5*Jrel_infp_sensitivity) / cajsr, 8.0))
    if celltype==2:
        Jrel_infp = Jrel_infp*1.7
    tau_relp_tmp = btp / (1.0 + 0.0123 / cajsr)
    tau_relp = 0.001 if tau_relp_tmp < 0.001 else tau_relp_tmp
    values[32] = (-Jrelp + Jrel_infp) / tau_relp
    fJrelp = 1.0 / (1.0 + KmCaMK / tmp_CaMKa)
    Jrel = (1.0 - fJrelp) * Jrelnp + Jrelp * fJrelp

    # Expressions for the calcium buffers component
    Jupnp = 0.004375 * cai / (0.00092 + cai)
    Jupp = 0.01203125 * cai / (0.00075 + cai)
    if celltype==1:
        Jupnp = Jupnp*1.3
        Jupp = Jupp*1.3
    fJupp = 1.0 / (1.0 + KmCaMK / tmp_CaMKa)
    Jleak = (0.0002625 * cansr)
    tmp_Jleak = Jleak*Jleak_rate
    Jserca = ((1.0 - fJupp) * Jupnp + Jupp * fJupp)
    tmp_Jserca = Jserca*Jserca_rate
    Jup = -tmp_Jleak + tmp_Jserca
    Jtr = 0.01 * cansr - 0.01 * cajsr

    # Expressions for the intracellular concentrations component
    if celltype==1:
        tmp_cmdnmax = cmdnmax*1.3
    else:
        tmp_cmdnmax = cmdnmax
    values[33] = JdiffNa * vss / vmyo + (
        -INa - INaL - INab - Isac_P_ns / 3 - 3.0 * INaCa_i - 3.0 * INaK
    ) * Acap / (F * vmyo)
    values[34] = -JdiffNa + (-ICaNa - 3.0 * INaCa_ss) * Acap / (F * vss)
    values[35] = JdiffK * vss / vmyo + (
        -Isac_P_k - IK1 - IKb - IKr - IKs - Istim - Ito - Isac_P_ns / 3 + 2.0 * INaK
    ) * Acap / (F * vmyo)
    values[36] = -JdiffK - Acap * ICaK / (F * vss)
    Bcass = 1.0 / (
        1.0
        + BSLmax * KmBSL * math.pow(KmBSL + cass, -2.0)
        + BSRmax * KmBSR * math.pow(KmBSR + cass, -2.0)
    )
    values[37] = (
        -Jdiff + Jrel * vjsr / vss + 0.5 * (-ICaL + 2.0 * INaCa_ss) * Acap / (F * vss)
    ) * Bcass
    values[38] = -Jtr * vjsr / vnsr + Jup
    Bcajsr = 1.0 / (1.0 + csqnmax * kmcsqn * math.pow(kmcsqn + cajsr, -2.0))
    values[39] = (-Jrel + Jtr) * Bcajsr

    # Expressions for the mechanics component

    tmp_ku = ku * ku_rate 
    tmp_kuw = kuw * kuw_rate 
    tmp_kws = kws * kws_rate 

    kwu = -tmp_kws + tmp_kuw * (-1 + 1.0 / rw)
    ksu = tmp_kws * rw * (-1 + 1.0 / rs)
    Aw = Tot_A * rs / (rs + rw * (1 - rs))
    As = Aw
    cw = tmp_kuw * phi * (1 - rw) / rw
    cs = tmp_kws * phi * rw * (1 - rs) / rs
    lambda_min12 = lmbda if lmbda < 1.2 else 1.2
    XU = 1 - TmB - XS - XW
    gammawu = (gammaw*gammaw_rate) * math.fabs(Zetaw)
    gammasu = (gammas*gammas_rate) * (
        Zetas * (Zetas > 0)
        if Zetas * (Zetas > 0) > (-1 - Zetas) * (Zetas < -1)
        else (-1 - Zetas) * (Zetas < -1)
    )
    values[40] = tmp_kws * XW - XS * gammasu - XS * ksu
    values[41] = tmp_kuw * XU - tmp_kws * XW - XW * gammawu - XW * kwu
    cat50 = cat50_ref + Beta1 * (-1 + lambda_min12)
    # CATRPN
    values[42] = (ktrpn*ktrpn_rate) * (-CaTrpn + math.pow(1000 * cai / cat50, (ntrpn*ntrpn_rate)) * (1 - CaTrpn))
    kb = tmp_ku * math.pow((Trpn50*Trpn50_rate), ntm) / (1 - rs - rw * (1 - rs))


    values[43] = (
        math.pow(CaTrpn, -ntm / 2) if math.pow(CaTrpn, -ntm / 2) < 100 else 100
    ) * XU * kb - tmp_ku * math.pow(CaTrpn, ntm / 2) * TmB
    values[44] = dLambda * As - Zetas * cs
    values[45] = dLambda * Aw - Zetaw * cw
    C = -1 + lambda_min12
    dCd = -Cd + C
    eta = etas if dCd < 0 else etal
    values[46] = p_k * (-Cd + C) / eta
    Bcai = 1.0 / (1.0 + tmp_cmdnmax * kmcmdn * math.pow(kmcmdn + cai, -2.0))
    J_TRPN = trpnmax * values[42]
    values[47] = (
        -J_TRPN
        + Jdiff * vss / vmyo
        - Jup * vnsr / vmyo
        + 0.5 * (-ICab - IpCa - Isac_P_ns / 3 + 2.0 * INaCa_i) * Acap / (F * vmyo)
    ) * Bcai

    # Return results
    return values


def monitor(states, t, parameters, monitored=None):
    """
    Computes monitored expressions of the ORdmm_Land_em_coupling ODE
    """

    # Assign states
    assert len(states) == 48
    (
        CaMKt,
        m,
        hf,
        hs,
        j,
        hsp,
        jp,
        mL,
        hL,
        hLp,
        a,
        iF,
        iS,
        ap,
        iFp,
        iSp,
        d,
        ff,
        fs,
        fcaf,
        fcas,
        jca,
        ffp,
        fcafp,
        nca,
        xrf,
        xrs,
        xs1,
        xs2,
        xk1,
        v,
        Jrelnp,
        Jrelp,
        nai,
        nass,
        ki,
        kss,
        cass,
        cansr,
        cajsr,
        XS,
        XW,
        CaTrpn,
        TmB,
        Zetas,
        Zetaw,
        Cd,
        cai,
    ) = states

    # Assign parameters
    assert len(parameters) == 141
    scale_ICaL = parameters[0]
    scale_IK1 = parameters[1]
    scale_IKr = parameters[2]
    scale_IKs = parameters[3]
    scale_INaL = parameters[4]
    celltype = parameters[5]
    cao = parameters[6]
    ko = parameters[7]
    nao = parameters[8]
    F = parameters[9]
    R = parameters[10]
    T = parameters[11]
    L = parameters[12]
    rad = parameters[13]
    Ahf = parameters[14]
    GNa = parameters[15]
    thL = parameters[16]
    Gto = parameters[17]
    delta_epi = parameters[18]
    Aff = parameters[19]
    Kmn = parameters[20]
    k2n = parameters[21]
    tjca = parameters[22]
    zca = parameters[23]
    bt = parameters[24]
    Beta0 = parameters[25]
    Beta1 = parameters[26]
    Tot_A = parameters[27]
    Tref = parameters[28]
    Trpn50 = parameters[29]
    cat50_ref = parameters[31]
    dLambda = parameters[32]
    etal = parameters[34]
    etas = parameters[35]
    gammas = parameters[36]
    gammaw = parameters[37]
    ktrpn = parameters[39]
    ku = parameters[40]
    kuw = parameters[41]
    kws = parameters[42]
    lmbda = parameters[43]
    ntm = parameters[45]
    ntrpn = parameters[46]
    p_a = parameters[47]
    p_b = parameters[48]
    p_k = parameters[49]
    phi = parameters[50]
    rs = parameters[51]
    rw = parameters[52]
    CaMKo = parameters[53]
    KmCaM = parameters[54]
    KmCaMK = parameters[55]
    aCaMK = parameters[56]
    bCaMK = parameters[57]
    PKNa = parameters[58]
    Gncx = parameters[59]
    KmCaAct = parameters[60]
    kasymm = parameters[61]
    kcaoff = parameters[62]
    kcaon = parameters[63]
    kna1 = parameters[64]
    kna2 = parameters[65]
    kna3 = parameters[66]
    qca = parameters[67]
    qna = parameters[68]
    wca = parameters[69]
    wna = parameters[70]
    wnaca = parameters[71]
    H = parameters[72]
    Khp = parameters[73]
    Kki = parameters[74]
    Kko = parameters[75]
    Kmgatp = parameters[76]
    Knai0 = parameters[77]
    Knao0 = parameters[78]
    Knap = parameters[79]
    Kxkur = parameters[80]
    MgADP = parameters[81]
    MgATP = parameters[82]
    Pnak = parameters[83]
    delta = parameters[84]
    eP = parameters[85]
    k1m = parameters[86]
    k1p = parameters[87]
    k2m = parameters[88]
    k2p = parameters[89]
    k3m = parameters[90]
    k3p = parameters[91]
    k4m = parameters[92]
    k4p = parameters[93]
    zk = parameters[94]
    GKb = parameters[95]
    PNab = parameters[96]
    PCab = parameters[97]
    GpCa = parameters[98]
    amp = parameters[103]
    duration = parameters[104]
    BSLmax = parameters[105]
    BSRmax = parameters[106]
    KmBSL = parameters[107]
    KmBSR = parameters[108]
    cmdnmax = parameters[109]
    csqnmax = parameters[110]
    kmcmdn = parameters[111]
    kmcsqn = parameters[112]
    trpnmax = parameters[114]
    GNa_rate = parameters[115]
    Gto_rate = parameters[116]
    GKr_rate = parameters[117]
    GKs_rate = parameters[118]
    GK1_rate = parameters[119]
    Gncx_rate = parameters[120]
    GKb_rate = parameters[121]
    GpCa_rate = parameters[122]
    GNaL_rate = parameters[123]
    Jleak_rate = parameters[124]
    Jserca_rate = parameters[125]
    CaMKa_rate = parameters[126]
    Pnak_rate = parameters[127]
    Pnab_rate = parameters[128]
    Pcab_rate = parameters[129]
    thl_rate = parameters[130]
    Jrel_inf_sensitivity = parameters[131]
    Jrel_infp_sensitivity = parameters[132]
    ku_rate = parameters[133]
    kuw_rate = parameters[134]
    kws_rate = parameters[135]
    ktrpn_rate = parameters[136]
    ntrpn_rate = parameters[137]
    Trpn50_rate = parameters[138]
    gammaw_rate = parameters[139]
    gammas_rate = parameters[140]


    # Init return args
    if monitored is None:
        monitored = np.zeros((309,), dtype=np.float_)
    else:
        assert isinstance(monitored, np.ndarray) and monitored.shape == (309,)

    # Expressions for the cell geometry component
    monitored[0] = 3140.0 * L * (rad * rad)
    monitored[1] = 6.28 * (rad * rad) + 6.28 * L * rad
    monitored[2] = 2 * monitored[1]
    monitored[3] = 0.68 * monitored[0]
    monitored[4] = 0.0552 * monitored[0]
    monitored[5] = 0.0048 * monitored[0]
    monitored[6] = 0.02 * monitored[0]

    # Expressions for the CaMKt component
    monitored[7] = CaMKo * (1.0 - CaMKt) / (1.0 + KmCaM / cass)
    monitored[8] = (CaMKt + monitored[7])*CaMKa_rate
    monitored[261] = -bCaMK * CaMKt + aCaMK * (CaMKt + monitored[7]) * monitored[7]

    # Expressions for the reversal potentials component
    monitored[142] = R * T * math.log(nao / nai) / F
    monitored[143] = R * T * math.log(ko / ki) / F
    monitored[144] = R * T * math.log((ko + PKNa * nao) / (PKNa * nai + ki)) / F
    monitored[145] = (F * F) * v / (R * T)
    monitored[146] = F * v / (R * T)

    # Expressions for the I_Na component
    monitored[9] = 1.0 / (
        1.0 + 0.0014599788446489682 * math.exp(-0.13333333333333333 * v)
    )
    monitored[10] = 1.0 / (
        9.454904638564724 * math.exp(0.02876042565429968 * v)
        + 1.9314113558536928e-05 * math.exp(-0.16792611251049538 * v)
    )
    monitored[262] = (-m + monitored[9]) / monitored[10]
    monitored[11] = 1.0 / (1 + 302724.605401998 * math.exp(0.1607717041800643 * v))
    monitored[12] = 1.0 / (
        1.183856958289087e-05 * math.exp(-0.15910898965791567 * v)
        + 6.305549185817275 * math.exp(0.0493339911198816 * v)
    )
    monitored[13] = 1.0 / (
        0.005164670235381792 * math.exp(-0.035650623885918005 * v)
        + 0.36987619372096325 * math.exp(0.017649135192375574 * v)
    )
    monitored[14] = 1.0 - Ahf
    monitored[263] = (-hf + monitored[11]) / monitored[12]
    monitored[264] = (-hs + monitored[11]) / monitored[13]
    monitored[15] = Ahf * hf + hs * monitored[14]
    monitored[16] = monitored[11]
    monitored[17] = 2.038 + 1.0 / (
        0.3131936394738773 * math.exp(0.02600780234070221 * v)
        + 1.1315282095590072e-07 * math.exp(-0.12075836251660427 * v)
    )
    monitored[265] = (-j + monitored[16]) / monitored[17]
    monitored[18] = 1.0 / (1 + 820249.0921708513 * math.exp(0.1607717041800643 * v))
    monitored[19] = 3.0 * monitored[13]
    monitored[266] = (-hsp + monitored[18]) / monitored[19]
    monitored[20] = Ahf * hf + hsp * monitored[14]
    monitored[21] = 1.46 * monitored[17]
    monitored[267] = (-jp + monitored[16]) / monitored[21]
    monitored[22] = 1.0 / (1.0 + KmCaMK / monitored[8])
    tmp_GNa = GNa*GNa_rate
    monitored[23] = (
        tmp_GNa
        * math.pow(m, 3.0)
        * (-monitored[142] + v)
        * (
            (1.0 - monitored[22]) * j * monitored[15]
            + jp * monitored[20] * monitored[22]
        )
    )

    # Expressions for the INaL component
    monitored[24] = 1.0 / (
        1.0 + 0.000291579585635531 * math.exp(-0.18996960486322187 * v)
    )
    monitored[25] = monitored[10]
    monitored[268] = (-mL + monitored[24]) / monitored[25]
    monitored[26] = 1.0 / (1.0 + 120578.15595522427 * math.exp(0.13354700854700854 * v))
    tmp_thL = thL * thl_rate
    monitored[269] = (-hL + monitored[26]) / tmp_thL
    monitored[27] = 1.0 / (1.0 + 275969.2903869871 * math.exp(0.13354700854700854 * v))
    monitored[28] = 3.0 * tmp_thL
    monitored[270] = (-hLp + monitored[27]) / monitored[28]
    monitored[29] = (0.0075 * scale_INaL) * GNaL_rate
    if celltype==1:
        monitored[29] = monitored[29]*0.6
    monitored[30] = 1.0 / (1.0 + KmCaMK / monitored[8])
    monitored[31] = (
        (-monitored[142] + v)
        * ((1.0 - monitored[30]) * hL + hLp * monitored[30])
        * mL
        * monitored[29]
    )

    # Expressions for the Ito component
    monitored[32] = 1.0 / (
        1.0 + 2.6316508161673635 * math.exp(-0.06747638326585695 * v)
    )
    monitored[33] = 1.0515 / (
        1.0 / (1.2089 + 2.2621017070578837 * math.exp(-0.03403513787634354 * v))
        + 3.5 / (1.0 + 30.069572727397507 * math.exp(0.03403513787634354 * v))
    )
    monitored[271] = (-a + monitored[32]) / monitored[33]
    monitored[34] = 1.0 / (1.0 + 2194.970764538301 * math.exp(0.17510068289266328 * v))
    if celltype==1:
        delta_epi = 1.0 - (0.95/(1.0 + math.exp((v + 70.0)/5.0)))
    monitored[35] = 4.562 + delta_epi / (
        0.14468698421272827 * math.exp(-0.01 * v)
        + 1.6300896349780942 * math.exp(0.06027727546714889 * v)
    )
    monitored[36] = 23.62 + delta_epi / (
        0.00027617763953377436 * math.exp(-0.01693480101608806 * v)
        + 0.024208962804604526 * math.exp(0.12377769525931426 * v)
    )
    monitored[37] = 1.0 / (
        1.0 + 0.24348537187522867 * math.exp(0.006613756613756614 * v)
    )
    monitored[38] = 1.0 - monitored[37]
    monitored[272] = (-iF + monitored[34]) / monitored[35]
    monitored[273] = (-iS + monitored[34]) / monitored[36]
    monitored[39] = iF * monitored[37] + iS * monitored[38]
    monitored[40] = 1.0 / (1.0 + 5.167428462230666 * math.exp(-0.06747638326585695 * v))
    monitored[274] = (-ap + monitored[40]) / monitored[33]
    monitored[41] = 1.354 + 0.0001 / (
        2.6591269045230603e-05 * math.exp(0.06293266205160478 * v)
        + 4.5541779737128264e24 * math.exp(-4.642525533890436 * v)
    )
    monitored[42] = 1.0 - 0.5 / (1.0 + 33.11545195869231 * math.exp(0.05 * v))
    monitored[43] = monitored[35] * monitored[41] * monitored[42]
    monitored[44] = monitored[36] * monitored[41] * monitored[42]
    monitored[275] = (-iFp + monitored[34]) / monitored[43]
    monitored[276] = (-iSp + monitored[34]) / monitored[44]
    monitored[45] = iFp * monitored[37] + iSp * monitored[38]
    monitored[46] = 1.0 / (1.0 + KmCaMK / monitored[8])
    tmp_Gto = Gto*Gto_rate
    if celltype==1:
        tmp_Gto = tmp_Gto*4.0
    elif celltype==2:
        tmp_Gto = tmp_Gto*4.0
    monitored[47] = (
        tmp_Gto
        * (-monitored[143] + v)
        * (
            (1.0 - monitored[46]) * a * monitored[39]
            + ap * monitored[45] * monitored[46]
        )
    )

    # Expressions for the ICaL ICaNa ICaK component
    monitored[48] = 1.0 / (
        1.0 + 0.39398514226669484 * math.exp(-0.23640661938534277 * v)
    )
    monitored[49] = 0.6 + 1.0 / (
        3.5254214873653824 * math.exp(0.09 * v)
        + 0.7408182206817179 * math.exp(-0.05 * v)
    )
    monitored[277] = (-d + monitored[48]) / monitored[49]
    monitored[50] = 1.0 / (1.0 + 199.86038496778565 * math.exp(0.27056277056277056 * v))
    monitored[51] = 7.0 + 1.0 / (
        0.03325075244518792 * math.exp(0.1 * v)
        + 0.0006090087745647571 * math.exp(-0.1 * v)
    )
    monitored[52] = 1000.0 + 1.0 / (
        1.0027667890106652e-05 * math.exp(-0.25 * v)
        + 8.053415618124885e-05 * math.exp(0.16666666666666666 * v)
    )
    monitored[53] = 1.0 - Aff
    monitored[278] = (-ff + monitored[50]) / monitored[51]
    monitored[279] = (-fs + monitored[50]) / monitored[52]
    monitored[54] = Aff * ff + fs * monitored[53]
    monitored[55] = monitored[50]
    monitored[56] = 7.0 + 1.0 / (
        0.0708317980974062 * math.exp(-0.14285714285714285 * v)
        + 0.02258872488031037 * math.exp(0.14285714285714285 * v)
    )
    monitored[57] = 100.0 + 1.0 / (
        0.00012 * math.exp(0.14285714285714285 * v)
        + 0.00012 * math.exp(-0.3333333333333333 * v)
    )
    monitored[58] = 0.3 + 0.6 / (1.0 + 0.36787944117144233 * math.exp(0.1 * v))
    monitored[59] = 1.0 - monitored[58]
    monitored[280] = (-fcaf + monitored[55]) / monitored[56]
    monitored[281] = (-fcas + monitored[55]) / monitored[57]
    monitored[60] = fcaf * monitored[58] + fcas * monitored[59]
    monitored[282] = (-jca + monitored[55]) / tjca
    monitored[61] = 2.5 * monitored[51]
    monitored[283] = (-ffp + monitored[50]) / monitored[61]
    monitored[62] = Aff * ffp + fs * monitored[53]
    monitored[63] = 2.5 * monitored[56]
    monitored[284] = (-fcafp + monitored[55]) / monitored[63]
    monitored[64] = fcafp * monitored[58] + fcas * monitored[59]
    monitored[65] = 1.0 * jca
    monitored[66] = 1.0 / (math.pow(1.0 + Kmn / cass, 4.0) + k2n / monitored[65])
    monitored[285] = k2n * monitored[66] - monitored[65] * nca
    monitored[67] = (
        4.0
        * (-0.341 * cao + cass * math.exp(2.0 * monitored[146]))
        * monitored[145]
        / (-1.0 + math.exp(2.0 * monitored[146]))
    )
    monitored[68] = (
        1.0
        * (-0.75 * nao + 0.75 * math.exp(1.0 * monitored[146]) * nass)
        * monitored[145]
        / (-1.0 + math.exp(1.0 * monitored[146]))
    )
    monitored[69] = (
        1.0
        * (-0.75 * ko + 0.75 * math.exp(1.0 * monitored[146]) * kss)
        * monitored[145]
        / (-1.0 + math.exp(1.0 * monitored[146]))
    )
    monitored[70] = 0.0001 * scale_ICaL
    if celltype==1:
        monitored[70] = monitored[70]*1.2
    elif celltype==2:
        monitored[70] = monitored[70]*2.5
    monitored[71] = 1.1 * monitored[70]
    monitored[72] = 0.00125 * monitored[70]
    monitored[73] = 0.0003574 * monitored[70]
    monitored[74] = 0.00125 * monitored[71]
    monitored[75] = 0.0003574 * monitored[71]
    monitored[76] = 1.0 / (1.0 + KmCaMK / monitored[8])
    monitored[77] = (
        (1.0 - monitored[76])
        * ((1.0 - nca) * monitored[54] + jca * monitored[60] * nca)
        * d
        * monitored[67]
        * monitored[70]
        + ((1.0 - nca) * monitored[62] + jca * monitored[64] * nca)
        * d
        * monitored[67]
        * monitored[71]
        * monitored[76]
    )
    monitored[78] = (
        (1.0 - monitored[76])
        * ((1.0 - nca) * monitored[54] + jca * monitored[60] * nca)
        * d
        * monitored[68]
        * monitored[72]
        + ((1.0 - nca) * monitored[62] + jca * monitored[64] * nca)
        * d
        * monitored[68]
        * monitored[74]
        * monitored[76]
    )
    monitored[79] = (
        (1.0 - monitored[76])
        * ((1.0 - nca) * monitored[54] + jca * monitored[60] * nca)
        * d
        * monitored[69]
        * monitored[73]
        + ((1.0 - nca) * monitored[62] + jca * monitored[64] * nca)
        * d
        * monitored[69]
        * monitored[75]
        * monitored[76]
    )

    # Expressions for the IKr component
    monitored[80] = 1.0 / (
        1.0 + 0.29287308872377504 * math.exp(-0.14729709824716453 * v)
    )
    monitored[81] = 12.98 + 1.0 / (
        0.0001020239312894894 * math.exp(0.25846471956577927 * v)
        + 0.00042992960891929087 * math.exp(-0.04906771344455348 * v)
    )
    monitored[82] = 1.865 + 1.0 / (
        0.0005922420036809394 * math.exp(0.13596193065941536 * v)
        + 3.549966111802463e-05 * math.exp(-0.03855050115651503 * v)
    )
    monitored[83] = 1.0 / (1.0 + 4.197299094734718 * math.exp(0.02617115938236064 * v))
    monitored[84] = 1.0 - monitored[83]
    monitored[286] = (-xrf + monitored[80]) / monitored[81]
    monitored[287] = (-xrs + monitored[80]) / monitored[82]
    monitored[85] = monitored[83] * xrf + monitored[84] * xrs
    monitored[86] = 1.0 / (
        (1.0 + 2.0820090840784555 * math.exp(0.013333333333333334 * v))
        * (1.0 + 0.7165313105737893 * math.exp(0.03333333333333333 * v))
    )
    monitored[87] = (0.046 * scale_IKr) * GKr_rate
    if celltype==1:
        monitored[87] = monitored[87]*1.3
    elif celltype==2:
        monitored[87] = monitored[87]*0.8
    monitored[88] = (
        0.4303314829119352
        * math.sqrt(ko)
        * (-monitored[143] + v)
        * monitored[85]
        * monitored[86]
        * monitored[87]
    )

    # Expressions for the IKs component
    monitored[89] = 1.0 / (
        1.0 + 0.27288596035656526 * math.exp(-0.11195700850873264 * v)
    )
    monitored[90] = 817.3 + 1.0 / (
        0.003504067763074858 * math.exp(0.056179775280898875 * v)
        + 0.0005184809083581659 * math.exp(-0.004347826086956522 * v)
    )
    monitored[288] = (-xs1 + monitored[89]) / monitored[90]
    monitored[91] = monitored[89]
    monitored[92] = 1.0 / (
        0.0022561357010639103 * math.exp(-0.03225806451612903 * v)
        + 0.0008208499862389881 * math.exp(0.05 * v)
    )
    monitored[289] = (-xs2 + monitored[91]) / monitored[92]
    monitored[93] = 1.0 + 0.6 / (1.0 + 6.481821026062645e-07 * math.pow(1.0 / cai, 1.4))
    monitored[94] = (0.0034 * scale_IKs) * GKs_rate
    if celltype==1:
        monitored[94] = monitored[94]*1.4
    monitored[95] = (-monitored[144] + v) * monitored[93] * monitored[94] * xs1 * xs2
    monitored[96] = 1.0 / (
        1.0 + math.exp((-144.59 - v - 2.5538 * ko) / (3.8115 + 1.5692 * ko))
    )
    monitored[97] = 122.2 / (
        0.0019352007631390235 * math.exp(-0.049115913555992145 * v)
        + 30.43364757524903 * math.exp(0.014423770373575654 * v)
    )
    monitored[290] = (-xk1 + monitored[96]) / monitored[97]
    monitored[98] = 1.0 / (
        1.0
        + 69220.6322106767
        * math.exp(0.10534077741493732 * v - 0.27388602127883704 * ko)
    )
    monitored[99] = (0.1908 * scale_IK1) * GK1_rate
    if celltype==1:
        monitored[99] = monitored[99]*1.2
    elif celltype==2:
        monitored[99] = monitored[99]*1.3
    monitored[100] = (
        math.sqrt(ko) * (-monitored[143] + v) * monitored[98] * monitored[99] * xk1
    )

    # Expressions for the INaCa_i component
    monitored[147] = math.exp(F * qca * v / (R * T))
    monitored[148] = math.exp(F * qna * v / (R * T))
    monitored[149] = 1 + (1 + monitored[148]) * nai / kna3
    monitored[150] = monitored[148] * nai / (kna3 * monitored[149])
    monitored[151] = 1.0 / monitored[149]
    monitored[152] = 1.0 + (1 + nai / kna2) * nai / kna1
    monitored[153] = (nai * nai) / (kna1 * kna2 * monitored[152])
    monitored[154] = 1.0 / monitored[152]
    monitored[155] = 1.0 + nao * (1.0 + 1.0 / monitored[148]) / kna3
    monitored[156] = nao / (kna3 * monitored[148] * monitored[155])
    monitored[157] = 1.0 / monitored[155]
    monitored[158] = 1.0 + kasymm + nao * (1.0 + nao / kna2) / kna1
    monitored[159] = (nao * nao) / (kna1 * kna2 * monitored[158])
    monitored[160] = 1.0 / monitored[158]
    monitored[161] = cao * kcaon * monitored[160]
    monitored[162] = kcaoff
    monitored[163] = wca * monitored[157]
    monitored[164] = wnaca * monitored[156]
    monitored[165] = monitored[163] + monitored[164]
    monitored[166] = wca * monitored[151] / monitored[147]
    monitored[167] = wnaca * monitored[150]
    monitored[168] = monitored[166] + monitored[167]
    monitored[169] = kcaoff
    monitored[170] = kcaon * cai * monitored[154]
    monitored[171] = wna * monitored[150] * monitored[153]
    monitored[172] = wna * monitored[156] * monitored[159]
    monitored[173] = (monitored[162] + monitored[165]) * monitored[169] * monitored[
        171
    ] + (monitored[170] + monitored[171]) * monitored[162] * monitored[168]
    monitored[174] = (monitored[161] + monitored[172]) * monitored[168] * monitored[
        170
    ] + (monitored[168] + monitored[169]) * monitored[161] * monitored[171]
    monitored[175] = (monitored[162] + monitored[165]) * monitored[170] * monitored[
        172
    ] + (monitored[170] + monitored[171]) * monitored[161] * monitored[165]
    monitored[176] = (monitored[161] + monitored[172]) * monitored[165] * monitored[
        169
    ] + (monitored[168] + monitored[169]) * monitored[162] * monitored[172]
    monitored[177] = monitored[173] / (
        monitored[173] + monitored[174] + monitored[175] + monitored[176]
    )
    monitored[178] = monitored[174] / (
        monitored[173] + monitored[174] + monitored[175] + monitored[176]
    )
    monitored[179] = monitored[175] / (
        monitored[173] + monitored[174] + monitored[175] + monitored[176]
    )
    monitored[180] = monitored[176] / (
        monitored[173] + monitored[174] + monitored[175] + monitored[176]
    )
    monitored[181] = 1.0 / (1.0 + math.pow(KmCaAct / cai, 2.0))
    monitored[182] = 1.0
    monitored[183] = (
        monitored[167] * monitored[179]
        - monitored[164] * monitored[178]
        + 3.0 * monitored[171] * monitored[180]
        - 3.0 * monitored[172] * monitored[177]
    )
    monitored[184] = monitored[162] * monitored[178] - monitored[161] * monitored[177]
    tmp_Gncx = Gncx * Gncx_rate
    if celltype==1:
        tmp_Gncx = tmp_Gncx*1.1
    elif celltype==2:
        tmp_Gncx = tmp_Gncx*1.4
    monitored[185] = (
        0.8
        * tmp_Gncx
        * (monitored[182] * monitored[183] + zca * monitored[184])
        * monitored[181]
    )

    # Expressions for the INaCa_ss component
    monitored[186] = 1 + (1 + monitored[148]) * nass / kna3
    monitored[187] = monitored[148] * nass / (kna3 * monitored[186])
    monitored[188] = 1.0 / monitored[186]
    monitored[189] = 1.0 + (1 + nass / kna2) * nass / kna1
    monitored[190] = (nass * nass) / (kna1 * kna2 * monitored[189])
    monitored[191] = 1.0 / monitored[189]
    monitored[192] = 1.0 + nao * (1.0 + 1.0 / monitored[148]) / kna3
    monitored[193] = nao / (kna3 * monitored[148] * monitored[192])
    monitored[194] = 1.0 / monitored[192]
    monitored[195] = 1.0 + kasymm + nao * (1 + nao / kna2) / kna1
    monitored[196] = (nao * nao) / (kna1 * kna2 * monitored[195])
    monitored[197] = 1.0 / monitored[195]
    monitored[198] = cao * kcaon * monitored[197]
    monitored[199] = kcaoff
    monitored[200] = wca * monitored[194]
    monitored[201] = wnaca * monitored[193]
    monitored[202] = monitored[200] + monitored[201]
    monitored[203] = wca * monitored[188] / monitored[147]
    monitored[204] = wnaca * monitored[187]
    monitored[205] = monitored[203] + monitored[204]
    monitored[206] = kcaoff
    monitored[207] = kcaon * cass * monitored[191]
    monitored[208] = wna * monitored[187] * monitored[190]
    monitored[209] = wna * monitored[193] * monitored[196]
    monitored[210] = (monitored[199] + monitored[202]) * monitored[206] * monitored[
        208
    ] + (monitored[207] + monitored[208]) * monitored[199] * monitored[205]
    monitored[211] = (monitored[198] + monitored[209]) * monitored[205] * monitored[
        207
    ] + (monitored[205] + monitored[206]) * monitored[198] * monitored[208]
    monitored[212] = (monitored[199] + monitored[202]) * monitored[207] * monitored[
        209
    ] + (monitored[207] + monitored[208]) * monitored[198] * monitored[202]
    monitored[213] = (monitored[198] + monitored[209]) * monitored[202] * monitored[
        206
    ] + (monitored[205] + monitored[206]) * monitored[199] * monitored[209]
    monitored[214] = monitored[210] / (
        monitored[210] + monitored[211] + monitored[212] + monitored[213]
    )
    monitored[215] = monitored[211] / (
        monitored[210] + monitored[211] + monitored[212] + monitored[213]
    )
    monitored[216] = monitored[212] / (
        monitored[210] + monitored[211] + monitored[212] + monitored[213]
    )
    monitored[217] = monitored[213] / (
        monitored[210] + monitored[211] + monitored[212] + monitored[213]
    )
    monitored[218] = 1.0 / (1.0 + math.pow(KmCaAct / cass, 2.0))
    monitored[219] = (
        monitored[204] * monitored[216]
        - monitored[201] * monitored[215]
        + 3.0 * monitored[208] * monitored[217]
        - 3.0 * monitored[209] * monitored[214]
    )
    monitored[220] = monitored[199] * monitored[215] - monitored[198] * monitored[214]
    monitored[221] = (
        0.2
        * tmp_Gncx
        * (monitored[182] * monitored[219] + zca * monitored[220])
        * monitored[218]
    )

    # Expressions for the INaK component
    monitored[222] = Knai0 * math.exp(0.3333333333333333 * F * delta * v / (R * T))
    monitored[223] = Knao0 * math.exp(
        0.3333333333333333 * F * (1.0 - delta) * v / (R * T)
    )
    monitored[224] = eP / (1.0 + H / Khp + nai / Knap + ki / Kxkur)
    monitored[225] = (
        k1p
        * math.pow(nai / monitored[222], 3.0)
        / (
            -1.0
            + math.pow(1.0 + ki / Kki, 2.0)
            + math.pow(1.0 + nai / monitored[222], 3.0)
        )
    )
    monitored[226] = MgADP * k1m
    monitored[227] = k2p
    monitored[228] = (
        k2m
        * math.pow(nao / monitored[223], 3.0)
        / (
            -1.0
            + math.pow(1.0 + ko / Kko, 2.0)
            + math.pow(1.0 + nao / monitored[223], 3.0)
        )
    )
    monitored[229] = (
        k3p
        * math.pow(ko / Kko, 2.0)
        / (
            -1.0
            + math.pow(1.0 + ko / Kko, 2.0)
            + math.pow(1.0 + nao / monitored[223], 3.0)
        )
    )
    monitored[230] = H * k3m * monitored[224] / (1.0 + MgATP / Kmgatp)
    monitored[231] = MgATP * k4p / (Kmgatp * (1.0 + MgATP / Kmgatp))
    monitored[232] = (
        k4m
        * math.pow(ki / Kki, 2.0)
        / (
            -1.0
            + math.pow(1.0 + ki / Kki, 2.0)
            + math.pow(1.0 + nai / monitored[222], 3.0)
        )
    )
    monitored[233] = (
        monitored[225] * monitored[227] * monitored[230]
        + monitored[225] * monitored[227] * monitored[231]
        + monitored[227] * monitored[230] * monitored[232]
        + monitored[228] * monitored[230] * monitored[232]
    )
    monitored[234] = (
        monitored[225] * monitored[227] * monitored[229]
        + monitored[226] * monitored[228] * monitored[232]
        + monitored[226] * monitored[229] * monitored[232]
        + monitored[227] * monitored[229] * monitored[232]
    )
    monitored[235] = (
        monitored[226] * monitored[228] * monitored[230]
        + monitored[226] * monitored[228] * monitored[231]
        + monitored[226] * monitored[229] * monitored[231]
        + monitored[227] * monitored[229] * monitored[231]
    )
    monitored[236] = (
        monitored[225] * monitored[228] * monitored[230]
        + monitored[225] * monitored[228] * monitored[231]
        + monitored[225] * monitored[229] * monitored[231]
        + monitored[228] * monitored[230] * monitored[232]
    )
    monitored[237] = monitored[233] / (
        monitored[233] + monitored[234] + monitored[235] + monitored[236]
    )
    monitored[238] = monitored[234] / (
        monitored[233] + monitored[234] + monitored[235] + monitored[236]
    )
    monitored[239] = monitored[235] / (
        monitored[233] + monitored[234] + monitored[235] + monitored[236]
    )
    monitored[240] = monitored[236] / (
        monitored[233] + monitored[234] + monitored[235] + monitored[236]
    )
    monitored[241] = (
        3.0 * monitored[229] * monitored[237] - 3.0 * monitored[230] * monitored[238]
    )
    monitored[242] = (
        2.0 * monitored[226] * monitored[240] - 2.0 * monitored[225] * monitored[239]
    )
    
    tmp_Pnak = Pnak*Pnak_rate
    if celltype==1:
        tmp_Pnak = tmp_Pnak*0.9
    elif celltype==2:
        tmp_Pnak = tmp_Pnak*0.7
    monitored[243] = tmp_Pnak * (monitored[182] * monitored[241] + zk * monitored[242])

    # Expressions for the IKb component
    monitored[244] = 1.0 / (
        1.0 + 2.202363450949239 * math.exp(-0.05452562704471101 * v)
    )
    tmp_GKb = GKb*GKb_rate
    if celltype==1:
        tmp_GKb = tmp_GKb*0.6
    monitored[245] = tmp_GKb * (-monitored[143] + v) * monitored[244]

    # Expressions for the INab component
    monitored[246] = (
        (PNab*Pnab_rate)
        * (-nao + math.exp(monitored[146]) * nai)
        * monitored[145]
        / (-1.0 + math.exp(monitored[146]))
    )

    # Expressions for the ICab component
    monitored[247] = (
        4.0
        * (PCab*Pcab_rate)
        * (-0.341 * cao + cai * math.exp(2.0 * monitored[146]))
        * monitored[145]
        / (-1.0 + math.exp(2.0 * monitored[146]))
    )

    # Expressions for the IpCa component
    tmp_GpCa = GpCa*GpCa_rate
    monitored[248] = tmp_GpCa * cai / (0.0005 + cai)

    # Expressions for the Isac (Pueyo)--> ns + k component
    monitored[249] = 0
    monitored[250] = 0

    # Expressions for the Istim component
    monitored[251] = amp * (t <= duration)

    # Expressions for the membrane potential component
    monitored[291] = (
        -monitored[249]
        - monitored[250]
        - monitored[100]
        - monitored[185]
        - monitored[221]
        - monitored[23]
        - monitored[243]
        - monitored[245]
        - monitored[246]
        - monitored[247]
        - monitored[248]
        - monitored[251]
        - monitored[31]
        - monitored[47]
        - monitored[77]
        - monitored[78]
        - monitored[79]
        - monitored[88]
        - monitored[95]
    )

    # Expressions for the diffusion fluxes component
    monitored[252] = 0.5 * nass - 0.5 * nai
    monitored[253] = 0.5 * kss - 0.5 * ki
    monitored[254] = 5.0 * cass - 5.0 * cai

    # Expressions for the ryanodione receptor component
    monitored[101] = 0.5 * bt
    monitored[102] = (
        -monitored[101]
        * monitored[77]
        / (1.0 + math.pow((1.5*Jrel_inf_sensitivity) / cajsr, 8.0))
    )
    if celltype==2:
        monitored[102] = monitored[102]*1.7
    monitored[103] = bt / (1.0 + 0.0123 / cajsr)
    monitored[104] = 0.001 if monitored[103] < 0.001 else monitored[103]
    monitored[292] = (-Jrelnp + monitored[102]) / monitored[104]
    monitored[105] = 1.25 * bt
    monitored[106] = 0.5 * monitored[105]
    monitored[107] = (
        -monitored[106]
        * monitored[77]
        / (1.0 + math.pow((1.5*Jrel_infp_sensitivity) / cajsr, 8.0))
    )
    if celltype==2:
        monitored[107] = monitored[107]*1.7
    monitored[108] = monitored[105] / (1.0 + 0.0123 / cajsr)
    monitored[109] = 0.001 if monitored[108] < 0.001 else monitored[108]
    monitored[293] = (-Jrelp + monitored[107]) / monitored[109]
    monitored[110] = 1.0 / (1.0 + KmCaMK / monitored[8])
    monitored[111] = (1.0 - monitored[110]) * Jrelnp + Jrelp * monitored[110]

    # Expressions for the calcium buffers component
    monitored[255] = 0.004375 * cai / (0.00092 + cai)
    monitored[256] = 0.01203125 * cai / (0.00075 + cai)
    if celltype==1:
        monitored[255] = monitored[255]*1.3
        monitored[256] = monitored[256]*1.3
    monitored[257] = 1.0 / (1.0 + KmCaMK / monitored[8])
    monitored[258] = (0.0002625 * cansr)*Jleak_rate
    monitored[259] = (
        -monitored[258]
        + ((1.0 - monitored[257]) * monitored[255]
        + monitored[256] * monitored[257])*Jserca_rate
    )
    monitored[260] = 0.01 * cansr - 0.01 * cajsr

    # Expressions for the intracellular concentrations component
    if celltype==1:
        tmp_cmdnmax = cmdnmax*1.3
    else:
        tmp_cmdnmax = cmdnmax
    monitored[294] = monitored[252] * monitored[6] / monitored[3] + (
        -monitored[23]
        - monitored[246]
        - monitored[31]
        - monitored[249] / 3
        - 3.0 * monitored[185]
        - 3.0 * monitored[243]
    ) * monitored[2] / (F * monitored[3])
    monitored[295] = -monitored[252] + (
        -monitored[78] - 3.0 * monitored[221]
    ) * monitored[2] / (F * monitored[6])
    monitored[296] = monitored[253] * monitored[6] / monitored[3] + (
        -monitored[250]
        - monitored[100]
        - monitored[245]
        - monitored[251]
        - monitored[47]
        - monitored[88]
        - monitored[95]
        - monitored[249] / 3
        + 2.0 * monitored[243]
    ) * monitored[2] / (F * monitored[3])
    monitored[297] = -monitored[253] - monitored[2] * monitored[79] / (F * monitored[6])
    monitored[112] = 1.0 / (
        1.0
        + BSLmax * KmBSL * math.pow(KmBSL + cass, -2.0)
        + BSRmax * KmBSR * math.pow(KmBSR + cass, -2.0)
    )
    monitored[298] = (
        -monitored[254]
        + monitored[111] * monitored[5] / monitored[6]
        + 0.5
        * (-monitored[77] + 2.0 * monitored[221])
        * monitored[2]
        / (F * monitored[6])
    ) * monitored[112]
    monitored[299] = -monitored[260] * monitored[5] / monitored[4] + monitored[259]
    monitored[113] = 1.0 / (1.0 + csqnmax * kmcsqn * math.pow(kmcsqn + cajsr, -2.0))
    monitored[300] = (-monitored[111] + monitored[260]) * monitored[113]

    # Expressions for the mechanics component

    tmp_ku = ku * ku_rate 
    tmp_kuw = kuw * kuw_rate
    tmp_kws = kws * kws_rate

    monitored[114] = XS if XS > 0 else 0
    monitored[115] = XW if XW > 0 else 0
    monitored[116] = CaTrpn if CaTrpn > 0 else 0
    monitored[117] = -tmp_kws + tmp_kuw * (-1 + 1.0 / rw)
    monitored[118] = tmp_kws * rw * (-1 + 1.0 / rs)
    monitored[119] = Tot_A * rs / (rs + rw * (1 - rs))
    monitored[120] = monitored[119]
    monitored[121] = tmp_kuw * phi * (1 - rw) / rw
    monitored[122] = tmp_kws * phi * rw * (1 - rs) / rs
    monitored[123] = lmbda if lmbda < 1.2 else 1.2
    monitored[124] = monitored[123] if monitored[123] < 0.87 else 0.87
    monitored[125] = 1 + Beta0 * (-1.87 + monitored[123] + monitored[124])
    monitored[126] = monitored[125] if monitored[125] > 0 else 0
    monitored[127] = 1 - TmB - XS - XW
    monitored[128] = (gammaw*gammaw_rate) * math.fabs(Zetaw)
    monitored[129] = (gammas*gammas_rate) * (
        Zetas * (Zetas > 0)
        if Zetas * (Zetas > 0) > (-1 - Zetas) * (Zetas < -1)
        else (-1 - Zetas) * (Zetas < -1)
    )
    monitored[301] = tmp_kws * XW - XS * monitored[118] - XS * monitored[129]
    monitored[302] = (
        tmp_kuw * monitored[127] - tmp_kws * XW - XW * monitored[117] - XW * monitored[128]
    )
    monitored[130] = cat50_ref + Beta1 * (-1 + monitored[123])
    monitored[303] = (ktrpn*ktrpn_rate) * (
        -CaTrpn + math.pow(1000 * cai / monitored[130], (ntrpn*ntrpn_rate)) * (1 - CaTrpn)
    )
    monitored[131] = tmp_ku * math.pow((Trpn50*Trpn50_rate), ntm) / (1 - rs - rw * (1 - rs))
    #from IPython import embed; embed()
    monitored[304] = (
        math.pow(CaTrpn, -ntm / 2) if math.pow(CaTrpn, -ntm / 2) < 100 else 100
    ) * monitored[127] * monitored[131] - tmp_ku * math.pow(CaTrpn, ntm / 2) * TmB
    monitored[305] = dLambda * monitored[120] - Zetas * monitored[122]
    monitored[306] = dLambda * monitored[119] - Zetaw * monitored[121]
    monitored[132] = Tref * ((1 + Zetas) * XS + XW * Zetaw) * monitored[126] / rs
    monitored[133] = -1 + monitored[123]
    monitored[134] = -Cd + monitored[133]
    monitored[135] = etas if monitored[134] < 0 else etal
    monitored[307] = p_k * (-Cd + monitored[133]) / monitored[135]
    monitored[136] = monitored[134] * monitored[135]
    monitored[137] = -1 + math.exp(p_b * monitored[133])
    monitored[138] = p_a * (monitored[136] + monitored[137])
    monitored[139] = monitored[132] + monitored[138]
    monitored[140] = 1.0 / (1.0 + tmp_cmdnmax * kmcmdn * math.pow(kmcmdn + cai, -2.0))
    monitored[141] = trpnmax * monitored[303]
    monitored[308] = (
        -monitored[141]
        + monitored[254] * monitored[6] / monitored[3]
        - monitored[259] * monitored[4] / monitored[3]
        + 0.5
        * (-monitored[247] - monitored[248] - monitored[249] / 3 + 2.0 * monitored[185])
        * monitored[2]
        / (F * monitored[3])
    ) * monitored[140]

    # Return results
    return monitored
