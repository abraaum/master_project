# Gotran generated code for the "ORdmm_Land2" model
from __future__ import division
from matplotlib.pyplot import get_plot_commands

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
    # ki=145, kss=145, cai=0.0001, cass=0.0001, cansr=1.2, cajsr=1.2,
    # XS=0, XW=0, CaTrpn=0, TmB=1, Zetas=0, Zetaw=0, Cd=0
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
            0.0001,
            1.2,
            1.2,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
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
            ("cai", 37),
            ("cass", 38),
            ("cansr", 39),
            ("cajsr", 40),
            ("XS", 41),
            ("XW", 42),
            ("CaTrpn", 43),
            ("TmB", 44),
            ("Zetas", 45),
            ("Zetaw", 46),
            ("Cd", 47),
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
    # scale_INaL=2.274, celltype=0, calib=1, dLambda=0, emcoupling=0,
    # isacs=0, lmbda=1, mode=1, cao=1.8, ko=5.4, nao=140.0,
    # F=96485.0, R=8314.0, T=310.0, L=0.01, rad=0.0011, Ahf=0.99,
    # GNa=31, thL=200.0, Gto=0.02, delta_epi=1.0, Aff=0.6, Kmn=0.002,
    # k2n=1000.0, tjca=75.0, zca=2.0, bt=4.75, CaMKo=0.05,
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

    init_values = np.array(
        [
            1.018,
            1.414,
            1.119,
            1.648,
            2.274,
            0,
            1,
            0,
            0,
            0,
            1,
            1,
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
            ("calib", 6),
            ("dLambda", 7),
            ("emcoupling", 8),
            ("isacs", 9),
            ("lmbda", 10),
            ("mode", 11),
            ("cao", 12),
            ("ko", 13),
            ("nao", 14),
            ("F", 15),
            ("R", 16),
            ("T", 17),
            ("L", 18),
            ("rad", 19),
            ("Ahf", 20),
            ("GNa", 21),
            ("thL", 22),
            ("Gto", 23),
            ("delta_epi", 24),
            ("Aff", 25),
            ("Kmn", 26),
            ("k2n", 27),
            ("tjca", 28),
            ("zca", 29),
            ("bt", 30),
            ("CaMKo", 31),
            ("KmCaM", 32),
            ("KmCaMK", 33),
            ("aCaMK", 34),
            ("bCaMK", 35),
            ("PKNa", 36),
            ("Gncx", 37),
            ("KmCaAct", 38),
            ("kasymm", 39),
            ("kcaoff", 40),
            ("kcaon", 41),
            ("kna1", 42),
            ("kna2", 43),
            ("kna3", 44),
            ("qca", 45),
            ("qna", 46),
            ("wca", 47),
            ("wna", 48),
            ("wnaca", 49),
            ("H", 50),
            ("Khp", 51),
            ("Kki", 52),
            ("Kko", 53),
            ("Kmgatp", 54),
            ("Knai0", 55),
            ("Knao0", 56),
            ("Knap", 57),
            ("Kxkur", 58),
            ("MgADP", 59),
            ("MgATP", 60),
            ("Pnak", 61),
            ("delta", 62),
            ("eP", 63),
            ("k1m", 64),
            ("k1p", 65),
            ("k2m", 66),
            ("k2p", 67),
            ("k3m", 68),
            ("k3p", 69),
            ("k4m", 70),
            ("k4p", 71),
            ("zk", 72),
            ("GKb", 73),
            ("PNab", 74),
            ("PCab", 75),
            ("GpCa", 76),
            ("Esac_ns", 77),
            ("Gsac_k", 78),
            ("Gsac_ns", 79),
            ("lambda_max", 80),
            ("amp", 81),
            ("duration", 82),
            ("BSLmax", 83),
            ("BSRmax", 84),
            ("KmBSL", 85),
            ("KmBSR", 86),
            ("cmdnmax", 87),
            ("csqnmax", 88),
            ("kmcmdn", 89),
            ("kmcsqn", 90),
            ("kmtrpn", 91),
            ("trpnmax", 92),
            ("GNa_rate", 93),
            ("Gto_rate", 94),
            ("GKr_rate", 95),
            ("GKs_rate", 96),
            ("GK1_rate", 97),
            ("Gncx_rate", 98),
            ("GKb_rate", 99),
            ("GpCa_rate", 100),
            ("GNaL_rate", 101),
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
            ("cai", 37),
            ("cass", 38),
            ("cansr", 39),
            ("cajsr", 40),
            ("XS", 41),
            ("XW", 42),
            ("CaTrpn", 43),
            ("TmB", 44),
            ("Zetas", 45),
            ("Zetaw", 46),
            ("Cd", 47),
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
            ("calib", 6),
            ("dLambda", 7),
            ("emcoupling", 8),
            ("isacs", 9),
            ("lmbda", 10),
            ("mode", 11),
            ("cao", 12),
            ("ko", 13),
            ("nao", 14),
            ("F", 15),
            ("R", 16),
            ("T", 17),
            ("L", 18),
            ("rad", 19),
            ("Ahf", 20),
            ("GNa", 21),
            ("thL", 22),
            ("Gto", 23),
            ("delta_epi", 24),
            ("Aff", 25),
            ("Kmn", 26),
            ("k2n", 27),
            ("tjca", 28),
            ("zca", 29),
            ("bt", 30),
            ("CaMKo", 31),
            ("KmCaM", 32),
            ("KmCaMK", 33),
            ("aCaMK", 34),
            ("bCaMK", 35),
            ("PKNa", 36),
            ("Gncx", 37),
            ("KmCaAct", 38),
            ("kasymm", 39),
            ("kcaoff", 40),
            ("kcaon", 41),
            ("kna1", 42),
            ("kna2", 43),
            ("kna3", 44),
            ("qca", 45),
            ("qna", 46),
            ("wca", 47),
            ("wna", 48),
            ("wnaca", 49),
            ("H", 50),
            ("Khp", 51),
            ("Kki", 52),
            ("Kko", 53),
            ("Kmgatp", 54),
            ("Knai0", 55),
            ("Knao0", 56),
            ("Knap", 57),
            ("Kxkur", 58),
            ("MgADP", 59),
            ("MgATP", 60),
            ("Pnak", 61),
            ("delta", 62),
            ("eP", 63),
            ("k1m", 64),
            ("k1p", 65),
            ("k2m", 66),
            ("k2p", 67),
            ("k3m", 68),
            ("k3p", 69),
            ("k4m", 70),
            ("k4p", 71),
            ("zk", 72),
            ("GKb", 73),
            ("PNab", 74),
            ("PCab", 75),
            ("GpCa", 76),
            ("Esac_ns", 77),
            ("Gsac_k", 78),
            ("Gsac_ns", 79),
            ("lambda_max", 80),
            ("amp", 81),
            ("duration", 82),
            ("BSLmax", 83),
            ("BSRmax", 84),
            ("KmBSL", 85),
            ("KmBSR", 86),
            ("cmdnmax", 87),
            ("csqnmax", 88),
            ("kmcmdn", 89),
            ("kmcsqn", 90),
            ("kmtrpn", 91),
            ("trpnmax", 92),
            ("GNa_rate", 93),
            ("Gto_rate", 94),
            ("GKr_rate", 95),
            ("GKs_rate", 96),
            ("GK1_rate", 97),
            ("Gncx_rate", 98),
            ("GKb_rate", 99),
            ("GpCa_rate", 100),
            ("GNaL_rate", 101),
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
            ("Bcai", 112),
            ("Bcass", 113),
            ("Bcajsr", 114),
            ("ENa", 115),
            ("EK", 116),
            ("EKs", 117),
            ("vffrt", 118),
            ("vfrt", 119),
            ("hca", 120),
            ("hna", 121),
            ("h1_i", 122),
            ("h2_i", 123),
            ("h3_i", 124),
            ("h4_i", 125),
            ("h5_i", 126),
            ("h6_i", 127),
            ("h7_i", 128),
            ("h8_i", 129),
            ("h9_i", 130),
            ("h10_i", 131),
            ("h11_i", 132),
            ("h12_i", 133),
            ("k1_i", 134),
            ("k2_i", 135),
            ("k3p_i", 136),
            ("k3pp_i", 137),
            ("k3_i", 138),
            ("k4p_i", 139),
            ("k4pp_i", 140),
            ("k4_i", 141),
            ("k5_i", 142),
            ("k6_i", 143),
            ("k7_i", 144),
            ("k8_i", 145),
            ("x1_i", 146),
            ("x2_i", 147),
            ("x3_i", 148),
            ("x4_i", 149),
            ("E1_i", 150),
            ("E2_i", 151),
            ("E3_i", 152),
            ("E4_i", 153),
            ("allo_i", 154),
            ("zna", 155),
            ("JncxNa_i", 156),
            ("JncxCa_i", 157),
            ("INaCa_i", 158),
            ("h1", 159),
            ("h2", 160),
            ("h3", 161),
            ("h4", 162),
            ("h5", 163),
            ("h6", 164),
            ("h7", 165),
            ("h8", 166),
            ("h9", 167),
            ("h10", 168),
            ("h11", 169),
            ("h12", 170),
            ("k1", 171),
            ("k2", 172),
            ("k3p_ss", 173),
            ("k3pp", 174),
            ("k3", 175),
            ("k4p_ss", 176),
            ("k4pp", 177),
            ("k4", 178),
            ("k5", 179),
            ("k6", 180),
            ("k7", 181),
            ("k8", 182),
            ("x1_ss", 183),
            ("x2_ss", 184),
            ("x3_ss", 185),
            ("x4_ss", 186),
            ("E1_ss", 187),
            ("E2_ss", 188),
            ("E3_ss", 189),
            ("E4_ss", 190),
            ("allo_ss", 191),
            ("JncxNa_ss", 192),
            ("JncxCa_ss", 193),
            ("INaCa_ss", 194),
            ("Knai", 195),
            ("Knao", 196),
            ("P", 197),
            ("a1", 198),
            ("b1", 199),
            ("a2", 200),
            ("b2", 201),
            ("a3", 202),
            ("b3", 203),
            ("a4", 204),
            ("b4", 205),
            ("x1", 206),
            ("x2", 207),
            ("x3", 208),
            ("x4", 209),
            ("E1", 210),
            ("E2", 211),
            ("E3", 212),
            ("E4", 213),
            ("JnakNa", 214),
            ("JnakK", 215),
            ("INaK", 216),
            ("xkb", 217),
            ("IKb", 218),
            ("INab", 219),
            ("ICab", 220),
            ("IpCa", 221),
            ("Isac_P_ns", 222),
            ("Isac_P_k", 223),
            ("Istim", 224),
            ("JdiffNa", 225),
            ("JdiffK", 226),
            ("Jdiff", 227),
            ("Jupnp", 228),
            ("Jupp", 229),
            ("fJupp", 230),
            ("Jleak", 231),
            ("Jup", 232),
            ("Jtr", 233),
            ("Ttot", 234),
            ("Ta", 235),
            ("Tp", 236),
            ("dCaMKt_dt", 237),
            ("dm_dt", 238),
            ("dhf_dt", 239),
            ("dhs_dt", 240),
            ("dj_dt", 241),
            ("dhsp_dt", 242),
            ("djp_dt", 243),
            ("dmL_dt", 244),
            ("dhL_dt", 245),
            ("dhLp_dt", 246),
            ("da_dt", 247),
            ("diF_dt", 248),
            ("diS_dt", 249),
            ("dap_dt", 250),
            ("diFp_dt", 251),
            ("diSp_dt", 252),
            ("dd_dt", 253),
            ("dff_dt", 254),
            ("dfs_dt", 255),
            ("dfcaf_dt", 256),
            ("dfcas_dt", 257),
            ("djca_dt", 258),
            ("dffp_dt", 259),
            ("dfcafp_dt", 260),
            ("dnca_dt", 261),
            ("dxrf_dt", 262),
            ("dxrs_dt", 263),
            ("dxs1_dt", 264),
            ("dxs2_dt", 265),
            ("dxk1_dt", 266),
            ("dv_dt", 267),
            ("dJrelnp_dt", 268),
            ("dJrelp_dt", 269),
            ("dnai_dt", 270),
            ("dnass_dt", 271),
            ("dki_dt", 272),
            ("dkss_dt", 273),
            ("dcai_dt", 274),
            ("dcass_dt", 275),
            ("dcansr_dt", 276),
            ("dcajsr_dt", 277),
            ("dXS_dt", 278),
            ("dXW_dt", 279),
            ("dCaTrpn_dt", 280),
            ("dTmB_dt", 281),
            ("dZetas_dt", 282),
            ("dZetaw_dt", 283),
            ("dCd_dt", 284),
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
    Compute the right hand side of the ORdmm_Land2 ODE
    """

    # Assign states
    assert len(states) == 48
    CaMKt = states[0]
    m = states[1]
    hf = states[2]
    hs = states[3]
    j = states[4]
    hsp = states[5]
    jp = states[6]
    mL = states[7]
    hL = states[8]
    hLp = states[9]
    a = states[10]
    iF = states[11]
    iS = states[12]
    ap = states[13]
    iFp = states[14]
    iSp = states[15]
    d = states[16]
    ff = states[17]
    fs = states[18]
    fcaf = states[19]
    fcas = states[20]
    jca = states[21]
    ffp = states[22]
    fcafp = states[23]
    nca = states[24]
    xrf = states[25]
    xrs = states[26]
    xs1 = states[27]
    xs2 = states[28]
    xk1 = states[29]
    v = states[30]
    Jrelnp = states[31]
    Jrelp = states[32]
    nai = states[33]
    nass = states[34]
    ki = states[35]
    kss = states[36]
    cai = states[37]
    cass = states[38]
    cansr = states[39]
    cajsr = states[40]

    # Assign parameters
    assert len(parameters) == 102
    scale_ICaL = parameters[0]
    scale_IK1 = parameters[1]
    scale_IKr = parameters[2]
    scale_IKs = parameters[3]
    scale_INaL = parameters[4]
    cao = parameters[12]
    ko = parameters[13]
    nao = parameters[14]
    F = parameters[15]
    R = parameters[16]
    T = parameters[17]
    L = parameters[18]
    rad = parameters[19]
    Ahf = parameters[20]
    GNa = parameters[21]
    thL = parameters[22]
    Gto = parameters[23]
    delta_epi = parameters[24]
    Aff = parameters[25]
    Kmn = parameters[26]
    k2n = parameters[27]
    tjca = parameters[28]
    zca = parameters[29]
    bt = parameters[30]
    CaMKo = parameters[31]
    KmCaM = parameters[32]
    KmCaMK = parameters[33]
    aCaMK = parameters[34]
    bCaMK = parameters[35]
    PKNa = parameters[36]
    Gncx = parameters[37]
    KmCaAct = parameters[38]
    kasymm = parameters[39]
    kcaoff = parameters[40]
    kcaon = parameters[41]
    kna1 = parameters[42]
    kna2 = parameters[43]
    kna3 = parameters[44]
    qca = parameters[45]
    qna = parameters[46]
    wca = parameters[47]
    wna = parameters[48]
    wnaca = parameters[49]
    H = parameters[50]
    Khp = parameters[51]
    Kki = parameters[52]
    Kko = parameters[53]
    Kmgatp = parameters[54]
    Knai0 = parameters[55]
    Knao0 = parameters[56]
    Knap = parameters[57]
    Kxkur = parameters[58]
    MgADP = parameters[59]
    MgATP = parameters[60]
    Pnak = parameters[61]
    delta = parameters[62]
    eP = parameters[63]
    k1m = parameters[64]
    k1p = parameters[65]
    k2m = parameters[66]
    k2p = parameters[67]
    k3m = parameters[68]
    k3p = parameters[69]
    k4m = parameters[70]
    k4p = parameters[71]
    zk = parameters[72]
    GKb = parameters[73]
    PNab = parameters[74]
    PCab = parameters[75]
    GpCa = parameters[76]
    amp = parameters[81]
    duration = parameters[82]
    BSLmax = parameters[83]
    BSRmax = parameters[84]
    KmBSL = parameters[85]
    KmBSR = parameters[86]
    cmdnmax = parameters[87]
    csqnmax = parameters[88]
    kmcmdn = parameters[89]
    kmcsqn = parameters[90]
    kmtrpn = parameters[91]
    trpnmax = parameters[92]
    GNa_rate = parameters[93]
    Gto_rate = parameters[94]
    GKr_rate = parameters[95]
    GKs_rate = parameters[96]
    GK1_rate = parameters[97]
    Gncx_rate = parameters[98]
    GKb_rate = parameters[99]
    GpCa_rate = parameters[100]
    GNaL_rate = parameters[101]

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
    fINap = 1.0 / (1.0 + KmCaMK / CaMKa)
    GNa *= GNa_rate
    INa = (
        GNa * math.pow(m, 3.0) * (-ENa + v) * ((1.0 - fINap) * h * j + fINap * hp * jp)
    )

    # Expressions for the INaL component
    mLss = 1.0 / (1.0 + 0.000291579585635531 * math.exp(-0.18996960486322187 * v))
    tmL = tm
    values[7] = (-mL + mLss) / tmL
    hLss = 1.0 / (1.0 + 120578.15595522427 * math.exp(0.13354700854700854 * v))
    values[8] = (-hL + hLss) / thL
    hLssp = 1.0 / (1.0 + 275969.2903869871 * math.exp(0.13354700854700854 * v))
    thLp = 3.0 * thL
    values[9] = (-hLp + hLssp) / thLp
    GNaL = (0.0075 * scale_INaL) * GNaL_rate
    fINaLp = 1.0 / (1.0 + KmCaMK / CaMKa)
    INaL = (-ENa + v) * ((1.0 - fINaLp) * hL + fINaLp * hLp) * GNaL * mL

    # Expressions for the Ito component
    ass = 1.0 / (1.0 + 2.6316508161673635 * math.exp(-0.06747638326585695 * v))
    ta = 1.0515 / (
        1.0 / (1.2089 + 2.2621017070578837 * math.exp(-0.03403513787634354 * v))
        + 3.5 / (1.0 + 30.069572727397507 * math.exp(0.03403513787634354 * v))
    )
    values[10] = (-a + ass) / ta
    iss = 1.0 / (1.0 + 2194.970764538301 * math.exp(0.17510068289266328 * v))
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
    fItop = 1.0 / (1.0 + KmCaMK / CaMKa)
    Gto *= Gto_rate
    Ito = Gto * (-EK + v) * ((1.0 - fItop) * a * i + ap * fItop * ip)

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
    PCap = 1.1 * PCa
    PCaNa = 0.00125 * PCa
    PCaK = 0.0003574 * PCa
    PCaNap = 0.00125 * PCap
    PCaKp = 0.0003574 * PCap
    fICaLp = 1.0 / (1.0 + KmCaMK / CaMKa)
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
    GK1 = (0.1908 * scale_IK1) * GK1_rate
    IK1 = math.sqrt(ko) * (-EK + v) * GK1 * rk1 * xk1

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
    INaCa_i = 0.8 * (Gncx * Gncx_rate) * (zca * JncxCa_i + zna * JncxNa_i) * allo_i

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
    INaCa_ss = 0.2 * (Gncx * Gncx_rate) * (zca * JncxCa_ss + zna * JncxNa_ss) * allo_ss

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
    INaK = Pnak * (zk * JnakK + zna * JnakNa)

    # Expressions for the IKb component
    xkb = 1.0 / (1.0 + 2.202363450949239 * math.exp(-0.05452562704471101 * v))
    GKb *= GKb_rate
    IKb = GKb * (-EK + v) * xkb

    # Expressions for the INab component
    INab = PNab * (-nao + math.exp(vfrt) * nai) * vffrt / (-1.0 + math.exp(vfrt))

    # Expressions for the ICab component
    ICab = (
        4.0
        * PCab
        * (-0.341 * cao + cai * math.exp(2.0 * vfrt))
        * vffrt
        / (-1.0 + math.exp(2.0 * vfrt))
    )

    # Expressions for the IpCa component
    GpCa *= GpCa_rate
    IpCa = GpCa * cai / (0.0005 + cai)

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
    Jrel_inf = -ICaL * a_rel / (1.0 + 25.62890625 * math.pow(1.0 / cajsr, 8.0))
    tau_rel_tmp = bt / (1.0 + 0.0123 / cajsr)
    tau_rel = 0.001 if tau_rel_tmp < 0.001 else tau_rel_tmp
    values[31] = (-Jrelnp + Jrel_inf) / tau_rel
    btp = 1.25 * bt
    a_relp = 0.5 * btp
    Jrel_infp = -ICaL * a_relp / (1.0 + 25.62890625 * math.pow(1.0 / cajsr, 8.0))
    tau_relp_tmp = btp / (1.0 + 0.0123 / cajsr)
    tau_relp = 0.001 if tau_relp_tmp < 0.001 else tau_relp_tmp
    values[32] = (-Jrelp + Jrel_infp) / tau_relp
    fJrelp = 1.0 / (1.0 + KmCaMK / CaMKa)
    Jrel = (1.0 - fJrelp) * Jrelnp + Jrelp * fJrelp

    # Expressions for the calcium buffers component
    Jupnp = 0.004375 * cai / (0.00092 + cai)
    Jupp = 0.01203125 * cai / (0.00075 + cai)
    fJupp = 1.0 / (1.0 + KmCaMK / CaMKa)
    Jleak = 0.0002625 * cansr
    Jup = -Jleak + (1.0 - fJupp) * Jupnp + Jupp * fJupp
    Jtr = 0.01 * cansr - 0.01 * cajsr

    # Expressions for the intracellular concentrations component
    values[33] = JdiffNa * vss / vmyo + (
        -INa - INaL - INab - Isac_P_ns / 3 - 3.0 * INaCa_i - 3.0 * INaK
    ) * Acap / (F * vmyo)
    values[34] = -JdiffNa + (-ICaNa - 3.0 * INaCa_ss) * Acap / (F * vss)
    values[35] = JdiffK * vss / vmyo + (
        -Isac_P_k - IK1 - IKb - IKr - IKs - Istim - Ito - Isac_P_ns / 3 + 2.0 * INaK
    ) * Acap / (F * vmyo)
    values[36] = -JdiffK - Acap * ICaK / (F * vss)
    Bcai = 1.0 / (
        1.0
        + cmdnmax * kmcmdn * math.pow(kmcmdn + cai, -2.0)
        + kmtrpn * trpnmax * math.pow(kmtrpn + cai, -2.0)
    )
    values[37] = (
        Jdiff * vss / vmyo
        - Jup * vnsr / vmyo
        + 0.5 * (-ICab - IpCa - Isac_P_ns / 3 + 2.0 * INaCa_i) * Acap / (F * vmyo)
    ) * Bcai
    Bcass = 1.0 / (
        1.0
        + BSLmax * KmBSL * math.pow(KmBSL + cass, -2.0)
        + BSRmax * KmBSR * math.pow(KmBSR + cass, -2.0)
    )
    values[38] = (
        -Jdiff + Jrel * vjsr / vss + 0.5 * (-ICaL + 2.0 * INaCa_ss) * Acap / (F * vss)
    ) * Bcass
    values[39] = -Jtr * vjsr / vnsr + Jup
    Bcajsr = 1.0 / (1.0 + csqnmax * kmcsqn * math.pow(kmcsqn + cajsr, -2.0))
    values[40] = (-Jrel + Jtr) * Bcajsr

    # Expressions for the mechanics component
    values[41] = 0
    values[42] = 0
    values[43] = 0
    values[44] = 0
    values[45] = 0
    values[46] = 0
    values[47] = 0

    # Return results
    return values


def monitor(states, t, parameters, monitored=None):
    """
    Computes monitored expressions of the ORdmm_Land2 ODE
    """

    # Assign states
    assert len(states) == 48
    CaMKt = states[0]
    m = states[1]
    hf = states[2]
    hs = states[3]
    j = states[4]
    hsp = states[5]
    jp = states[6]
    mL = states[7]
    hL = states[8]
    hLp = states[9]
    a = states[10]
    iF = states[11]
    iS = states[12]
    ap = states[13]
    iFp = states[14]
    iSp = states[15]
    d = states[16]
    ff = states[17]
    fs = states[18]
    fcaf = states[19]
    fcas = states[20]
    jca = states[21]
    ffp = states[22]
    fcafp = states[23]
    nca = states[24]
    xrf = states[25]
    xrs = states[26]
    xs1 = states[27]
    xs2 = states[28]
    xk1 = states[29]
    v = states[30]
    Jrelnp = states[31]
    Jrelp = states[32]
    nai = states[33]
    nass = states[34]
    ki = states[35]
    kss = states[36]
    cai = states[37]
    cass = states[38]
    cansr = states[39]
    cajsr = states[40]

    # Assign parameters
    assert len(parameters) == 102
    scale_ICaL = parameters[0]
    scale_IK1 = parameters[1]
    scale_IKr = parameters[2]
    scale_IKs = parameters[3]
    scale_INaL = parameters[4]
    cao = parameters[12]
    ko = parameters[13]
    nao = parameters[14]
    F = parameters[15]
    R = parameters[16]
    T = parameters[17]
    L = parameters[18]
    rad = parameters[19]
    Ahf = parameters[20]
    GNa = parameters[21]
    thL = parameters[22]
    Gto = parameters[23]
    delta_epi = parameters[24]
    Aff = parameters[25]
    Kmn = parameters[26]
    k2n = parameters[27]
    tjca = parameters[28]
    zca = parameters[29]
    bt = parameters[30]
    CaMKo = parameters[31]
    KmCaM = parameters[32]
    KmCaMK = parameters[33]
    aCaMK = parameters[34]
    bCaMK = parameters[35]
    PKNa = parameters[36]
    Gncx = parameters[37]
    KmCaAct = parameters[38]
    kasymm = parameters[39]
    kcaoff = parameters[40]
    kcaon = parameters[41]
    kna1 = parameters[42]
    kna2 = parameters[43]
    kna3 = parameters[44]
    qca = parameters[45]
    qna = parameters[46]
    wca = parameters[47]
    wna = parameters[48]
    wnaca = parameters[49]
    H = parameters[50]
    Khp = parameters[51]
    Kki = parameters[52]
    Kko = parameters[53]
    Kmgatp = parameters[54]
    Knai0 = parameters[55]
    Knao0 = parameters[56]
    Knap = parameters[57]
    Kxkur = parameters[58]
    MgADP = parameters[59]
    MgATP = parameters[60]
    Pnak = parameters[61]
    delta = parameters[62]
    eP = parameters[63]
    k1m = parameters[64]
    k1p = parameters[65]
    k2m = parameters[66]
    k2p = parameters[67]
    k3m = parameters[68]
    k3p = parameters[69]
    k4m = parameters[70]
    k4p = parameters[71]
    zk = parameters[72]
    GKb = parameters[73]
    PNab = parameters[74]
    PCab = parameters[75]
    GpCa = parameters[76]
    amp = parameters[81]
    duration = parameters[82]
    BSLmax = parameters[83]
    BSRmax = parameters[84]
    KmBSL = parameters[85]
    KmBSR = parameters[86]
    cmdnmax = parameters[87]
    csqnmax = parameters[88]
    kmcmdn = parameters[89]
    kmcsqn = parameters[90]
    kmtrpn = parameters[91]
    trpnmax = parameters[92]
    GNa_rate = parameters[93]
    Gto_rate = parameters[94]
    GKr_rate = parameters[95]
    GKs_rate = parameters[96]
    GK1_rate = parameters[97]
    Gncx_rate = parameters[98]
    GKb_rate = parameters[99]
    GpCa_rate = parameters[100]
    GNaL_rate = parameters[101]

    # Init return args
    if monitored is None:
        monitored = np.zeros((285,), dtype=np.float_)
    else:
        assert isinstance(monitored, np.ndarray) and monitored.shape == (285,)

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
    monitored[8] = CaMKt + monitored[7]
    monitored[237] = -bCaMK * CaMKt + aCaMK * (CaMKt + monitored[7]) * monitored[7]

    # Expressions for the reversal potentials component
    monitored[115] = R * T * math.log(nao / nai) / F
    monitored[116] = R * T * math.log(ko / ki) / F
    monitored[117] = R * T * math.log((ko + PKNa * nao) / (PKNa * nai + ki)) / F
    monitored[118] = (F * F) * v / (R * T)
    monitored[119] = F * v / (R * T)

    # Expressions for the I_Na component
    monitored[9] = 1.0 / (
        1.0 + 0.0014599788446489682 * math.exp(-0.13333333333333333 * v)
    )
    monitored[10] = 1.0 / (
        9.454904638564724 * math.exp(0.02876042565429968 * v)
        + 1.9314113558536928e-05 * math.exp(-0.16792611251049538 * v)
    )
    monitored[238] = (-m + monitored[9]) / monitored[10]
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
    monitored[239] = (-hf + monitored[11]) / monitored[12]
    monitored[240] = (-hs + monitored[11]) / monitored[13]
    monitored[15] = Ahf * hf + hs * monitored[14]
    monitored[16] = monitored[11]
    monitored[17] = 2.038 + 1.0 / (
        0.3131936394738773 * math.exp(0.02600780234070221 * v)
        + 1.1315282095590072e-07 * math.exp(-0.12075836251660427 * v)
    )
    monitored[241] = (-j + monitored[16]) / monitored[17]
    monitored[18] = 1.0 / (1 + 820249.0921708513 * math.exp(0.1607717041800643 * v))
    monitored[19] = 3.0 * monitored[13]
    monitored[242] = (-hsp + monitored[18]) / monitored[19]
    monitored[20] = Ahf * hf + hsp * monitored[14]
    monitored[21] = 1.46 * monitored[17]
    monitored[243] = (-jp + monitored[16]) / monitored[21]
    monitored[22] = 1.0 / (1.0 + KmCaMK / monitored[8])
    GNa *= GNa_rate
    monitored[23] = (
        GNa
        * math.pow(m, 3.0)
        * (-monitored[115] + v)
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
    monitored[244] = (-mL + monitored[24]) / monitored[25]
    monitored[26] = 1.0 / (1.0 + 120578.15595522427 * math.exp(0.13354700854700854 * v))
    monitored[245] = (-hL + monitored[26]) / thL
    monitored[27] = 1.0 / (1.0 + 275969.2903869871 * math.exp(0.13354700854700854 * v))
    monitored[28] = 3.0 * thL
    monitored[246] = (-hLp + monitored[27]) / monitored[28]
    monitored[29] = (0.0075 * scale_INaL) * GNaL_rate
    monitored[30] = 1.0 / (1.0 + KmCaMK / monitored[8])
    monitored[31] = (
        (-monitored[115] + v)
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
    monitored[247] = (-a + monitored[32]) / monitored[33]
    monitored[34] = 1.0 / (1.0 + 2194.970764538301 * math.exp(0.17510068289266328 * v))
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
    monitored[248] = (-iF + monitored[34]) / monitored[35]
    monitored[249] = (-iS + monitored[34]) / monitored[36]
    monitored[39] = iF * monitored[37] + iS * monitored[38]
    monitored[40] = 1.0 / (1.0 + 5.167428462230666 * math.exp(-0.06747638326585695 * v))
    monitored[250] = (-ap + monitored[40]) / monitored[33]
    monitored[41] = 1.354 + 0.0001 / (
        2.6591269045230603e-05 * math.exp(0.06293266205160478 * v)
        + 4.5541779737128264e24 * math.exp(-4.642525533890436 * v)
    )
    monitored[42] = 1.0 - 0.5 / (1.0 + 33.11545195869231 * math.exp(0.05 * v))
    monitored[43] = monitored[35] * monitored[41] * monitored[42]
    monitored[44] = monitored[36] * monitored[41] * monitored[42]
    monitored[251] = (-iFp + monitored[34]) / monitored[43]
    monitored[252] = (-iSp + monitored[34]) / monitored[44]
    monitored[45] = iFp * monitored[37] + iSp * monitored[38]
    monitored[46] = 1.0 / (1.0 + KmCaMK / monitored[8])
    Gto *= Gto_rate
    monitored[47] = (
        Gto
        * (-monitored[116] + v)
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
    monitored[253] = (-d + monitored[48]) / monitored[49]
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
    monitored[254] = (-ff + monitored[50]) / monitored[51]
    monitored[255] = (-fs + monitored[50]) / monitored[52]
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
    monitored[256] = (-fcaf + monitored[55]) / monitored[56]
    monitored[257] = (-fcas + monitored[55]) / monitored[57]
    monitored[60] = fcaf * monitored[58] + fcas * monitored[59]
    monitored[258] = (-jca + monitored[55]) / tjca
    monitored[61] = 2.5 * monitored[51]
    monitored[259] = (-ffp + monitored[50]) / monitored[61]
    monitored[62] = Aff * ffp + fs * monitored[53]
    monitored[63] = 2.5 * monitored[56]
    monitored[260] = (-fcafp + monitored[55]) / monitored[63]
    monitored[64] = fcafp * monitored[58] + fcas * monitored[59]
    monitored[65] = 1.0 * jca
    monitored[66] = 1.0 / (math.pow(1.0 + Kmn / cass, 4.0) + k2n / monitored[65])
    monitored[261] = k2n * monitored[66] - monitored[65] * nca
    monitored[67] = (
        4.0
        * (-0.341 * cao + cass * math.exp(2.0 * monitored[119]))
        * monitored[118]
        / (-1.0 + math.exp(2.0 * monitored[119]))
    )
    monitored[68] = (
        1.0
        * (-0.75 * nao + 0.75 * math.exp(1.0 * monitored[119]) * nass)
        * monitored[118]
        / (-1.0 + math.exp(1.0 * monitored[119]))
    )
    monitored[69] = (
        1.0
        * (-0.75 * ko + 0.75 * math.exp(1.0 * monitored[119]) * kss)
        * monitored[118]
        / (-1.0 + math.exp(1.0 * monitored[119]))
    )
    monitored[70] = 0.0001 * scale_ICaL
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
    monitored[262] = (-xrf + monitored[80]) / monitored[81]
    monitored[263] = (-xrs + monitored[80]) / monitored[82]
    monitored[85] = monitored[83] * xrf + monitored[84] * xrs
    monitored[86] = 1.0 / (
        (1.0 + 2.0820090840784555 * math.exp(0.013333333333333334 * v))
        * (1.0 + 0.7165313105737893 * math.exp(0.03333333333333333 * v))
    )
    monitored[87] = (0.046 * scale_IKr) * GKr_rate
    monitored[88] = (
        0.4303314829119352
        * math.sqrt(ko)
        * (-monitored[116] + v)
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
    monitored[264] = (-xs1 + monitored[89]) / monitored[90]
    monitored[91] = monitored[89]
    monitored[92] = 1.0 / (
        0.0022561357010639103 * math.exp(-0.03225806451612903 * v)
        + 0.0008208499862389881 * math.exp(0.05 * v)
    )
    monitored[265] = (-xs2 + monitored[91]) / monitored[92]
    monitored[93] = 1.0 + 0.6 / (1.0 + 6.481821026062645e-07 * math.pow(1.0 / cai, 1.4))
    monitored[94] = (0.0034 * scale_IKs)*GKs_rate 
    monitored[95] = (-monitored[117] + v) * monitored[93] * monitored[94] * xs1 * xs2
    monitored[96] = 1.0 / (
        1.0 + math.exp((-144.59 - v - 2.5538 * ko) / (3.8115 + 1.5692 * ko))
    )
    monitored[97] = 122.2 / (
        0.0019352007631390235 * math.exp(-0.049115913555992145 * v)
        + 30.43364757524903 * math.exp(0.014423770373575654 * v)
    )
    monitored[266] = (-xk1 + monitored[96]) / monitored[97]
    monitored[98] = 1.0 / (
        1.0
        + 69220.6322106767
        * math.exp(0.10534077741493732 * v - 0.27388602127883704 * ko)
    )
    monitored[99] = (0.1908 * scale_IK1) * GK1_rate
    monitored[100] = (
        math.sqrt(ko) * (-monitored[116] + v) * monitored[98] * monitored[99] * xk1
    )

    # Expressions for the INaCa_i component
    monitored[120] = math.exp(F * qca * v / (R * T))
    monitored[121] = math.exp(F * qna * v / (R * T))
    monitored[122] = 1 + (1 + monitored[121]) * nai / kna3
    monitored[123] = monitored[121] * nai / (kna3 * monitored[122])
    monitored[124] = 1.0 / monitored[122]
    monitored[125] = 1.0 + (1 + nai / kna2) * nai / kna1
    monitored[126] = (nai * nai) / (kna1 * kna2 * monitored[125])
    monitored[127] = 1.0 / monitored[125]
    monitored[128] = 1.0 + nao * (1.0 + 1.0 / monitored[121]) / kna3
    monitored[129] = nao / (kna3 * monitored[121] * monitored[128])
    monitored[130] = 1.0 / monitored[128]
    monitored[131] = 1.0 + kasymm + nao * (1.0 + nao / kna2) / kna1
    monitored[132] = (nao * nao) / (kna1 * kna2 * monitored[131])
    monitored[133] = 1.0 / monitored[131]
    monitored[134] = cao * kcaon * monitored[133]
    monitored[135] = kcaoff
    monitored[136] = wca * monitored[130]
    monitored[137] = wnaca * monitored[129]
    monitored[138] = monitored[136] + monitored[137]
    monitored[139] = wca * monitored[124] / monitored[120]
    monitored[140] = wnaca * monitored[123]
    monitored[141] = monitored[139] + monitored[140]
    monitored[142] = kcaoff
    monitored[143] = kcaon * cai * monitored[127]
    monitored[144] = wna * monitored[123] * monitored[126]
    monitored[145] = wna * monitored[129] * monitored[132]
    monitored[146] = (monitored[135] + monitored[138]) * monitored[142] * monitored[
        144
    ] + (monitored[143] + monitored[144]) * monitored[135] * monitored[141]
    monitored[147] = (monitored[134] + monitored[145]) * monitored[141] * monitored[
        143
    ] + (monitored[141] + monitored[142]) * monitored[134] * monitored[144]
    monitored[148] = (monitored[135] + monitored[138]) * monitored[143] * monitored[
        145
    ] + (monitored[143] + monitored[144]) * monitored[134] * monitored[138]
    monitored[149] = (monitored[134] + monitored[145]) * monitored[138] * monitored[
        142
    ] + (monitored[141] + monitored[142]) * monitored[135] * monitored[145]
    monitored[150] = monitored[146] / (
        monitored[146] + monitored[147] + monitored[148] + monitored[149]
    )
    monitored[151] = monitored[147] / (
        monitored[146] + monitored[147] + monitored[148] + monitored[149]
    )
    monitored[152] = monitored[148] / (
        monitored[146] + monitored[147] + monitored[148] + monitored[149]
    )
    monitored[153] = monitored[149] / (
        monitored[146] + monitored[147] + monitored[148] + monitored[149]
    )
    monitored[154] = 1.0 / (1.0 + math.pow(KmCaAct / cai, 2.0))
    monitored[155] = 1.0
    monitored[156] = (
        monitored[140] * monitored[152]
        - monitored[137] * monitored[151]
        + 3.0 * monitored[144] * monitored[153]
        - 3.0 * monitored[145] * monitored[150]
    )
    monitored[157] = monitored[135] * monitored[151] - monitored[134] * monitored[150]
    monitored[158] = (
        0.8
        * (Gncx * Gncx_rate)
        * (monitored[155] * monitored[156] + zca * monitored[157])
        * monitored[154]
    )

    # Expressions for the INaCa_ss component
    monitored[159] = 1 + (1 + monitored[121]) * nass / kna3
    monitored[160] = monitored[121] * nass / (kna3 * monitored[159])
    monitored[161] = 1.0 / monitored[159]
    monitored[162] = 1.0 + (1 + nass / kna2) * nass / kna1
    monitored[163] = (nass * nass) / (kna1 * kna2 * monitored[162])
    monitored[164] = 1.0 / monitored[162]
    monitored[165] = 1.0 + nao * (1.0 + 1.0 / monitored[121]) / kna3
    monitored[166] = nao / (kna3 * monitored[121] * monitored[165])
    monitored[167] = 1.0 / monitored[165]
    monitored[168] = 1.0 + kasymm + nao * (1 + nao / kna2) / kna1
    monitored[169] = (nao * nao) / (kna1 * kna2 * monitored[168])
    monitored[170] = 1.0 / monitored[168]
    monitored[171] = cao * kcaon * monitored[170]
    monitored[172] = kcaoff
    monitored[173] = wca * monitored[167]
    monitored[174] = wnaca * monitored[166]
    monitored[175] = monitored[173] + monitored[174]
    monitored[176] = wca * monitored[161] / monitored[120]
    monitored[177] = wnaca * monitored[160]
    monitored[178] = monitored[176] + monitored[177]
    monitored[179] = kcaoff
    monitored[180] = kcaon * cass * monitored[164]
    monitored[181] = wna * monitored[160] * monitored[163]
    monitored[182] = wna * monitored[166] * monitored[169]
    monitored[183] = (monitored[172] + monitored[175]) * monitored[179] * monitored[
        181
    ] + (monitored[180] + monitored[181]) * monitored[172] * monitored[178]
    monitored[184] = (monitored[171] + monitored[182]) * monitored[178] * monitored[
        180
    ] + (monitored[178] + monitored[179]) * monitored[171] * monitored[181]
    monitored[185] = (monitored[172] + monitored[175]) * monitored[180] * monitored[
        182
    ] + (monitored[180] + monitored[181]) * monitored[171] * monitored[175]
    monitored[186] = (monitored[171] + monitored[182]) * monitored[175] * monitored[
        179
    ] + (monitored[178] + monitored[179]) * monitored[172] * monitored[182]
    monitored[187] = monitored[183] / (
        monitored[183] + monitored[184] + monitored[185] + monitored[186]
    )
    monitored[188] = monitored[184] / (
        monitored[183] + monitored[184] + monitored[185] + monitored[186]
    )
    monitored[189] = monitored[185] / (
        monitored[183] + monitored[184] + monitored[185] + monitored[186]
    )
    monitored[190] = monitored[186] / (
        monitored[183] + monitored[184] + monitored[185] + monitored[186]
    )
    monitored[191] = 1.0 / (1.0 + math.pow(KmCaAct / cass, 2.0))
    monitored[192] = (
        monitored[177] * monitored[189]
        - monitored[174] * monitored[188]
        + 3.0 * monitored[181] * monitored[190]
        - 3.0 * monitored[182] * monitored[187]
    )
    monitored[193] = monitored[172] * monitored[188] - monitored[171] * monitored[187]
    monitored[194] = (
        0.2
        * (Gncx * Gncx_rate)
        * (monitored[155] * monitored[192] + zca * monitored[193])
        * monitored[191]
    )

    # Expressions for the INaK component
    monitored[195] = Knai0 * math.exp(0.3333333333333333 * F * delta * v / (R * T))
    monitored[196] = Knao0 * math.exp(
        0.3333333333333333 * F * (1.0 - delta) * v / (R * T)
    )
    monitored[197] = eP / (1.0 + H / Khp + nai / Knap + ki / Kxkur)
    monitored[198] = (
        k1p
        * math.pow(nai / monitored[195], 3.0)
        / (
            -1.0
            + math.pow(1.0 + ki / Kki, 2.0)
            + math.pow(1.0 + nai / monitored[195], 3.0)
        )
    )
    monitored[199] = MgADP * k1m
    monitored[200] = k2p
    monitored[201] = (
        k2m
        * math.pow(nao / monitored[196], 3.0)
        / (
            -1.0
            + math.pow(1.0 + ko / Kko, 2.0)
            + math.pow(1.0 + nao / monitored[196], 3.0)
        )
    )
    monitored[202] = (
        k3p
        * math.pow(ko / Kko, 2.0)
        / (
            -1.0
            + math.pow(1.0 + ko / Kko, 2.0)
            + math.pow(1.0 + nao / monitored[196], 3.0)
        )
    )
    monitored[203] = H * k3m * monitored[197] / (1.0 + MgATP / Kmgatp)
    monitored[204] = MgATP * k4p / (Kmgatp * (1.0 + MgATP / Kmgatp))
    monitored[205] = (
        k4m
        * math.pow(ki / Kki, 2.0)
        / (
            -1.0
            + math.pow(1.0 + ki / Kki, 2.0)
            + math.pow(1.0 + nai / monitored[195], 3.0)
        )
    )
    monitored[206] = (
        monitored[198] * monitored[200] * monitored[203]
        + monitored[198] * monitored[200] * monitored[204]
        + monitored[200] * monitored[203] * monitored[205]
        + monitored[201] * monitored[203] * monitored[205]
    )
    monitored[207] = (
        monitored[198] * monitored[200] * monitored[202]
        + monitored[199] * monitored[201] * monitored[205]
        + monitored[199] * monitored[202] * monitored[205]
        + monitored[200] * monitored[202] * monitored[205]
    )
    monitored[208] = (
        monitored[199] * monitored[201] * monitored[203]
        + monitored[199] * monitored[201] * monitored[204]
        + monitored[199] * monitored[202] * monitored[204]
        + monitored[200] * monitored[202] * monitored[204]
    )
    monitored[209] = (
        monitored[198] * monitored[201] * monitored[203]
        + monitored[198] * monitored[201] * monitored[204]
        + monitored[198] * monitored[202] * monitored[204]
        + monitored[201] * monitored[203] * monitored[205]
    )
    monitored[210] = monitored[206] / (
        monitored[206] + monitored[207] + monitored[208] + monitored[209]
    )
    monitored[211] = monitored[207] / (
        monitored[206] + monitored[207] + monitored[208] + monitored[209]
    )
    monitored[212] = monitored[208] / (
        monitored[206] + monitored[207] + monitored[208] + monitored[209]
    )
    monitored[213] = monitored[209] / (
        monitored[206] + monitored[207] + monitored[208] + monitored[209]
    )
    monitored[214] = (
        3.0 * monitored[202] * monitored[210] - 3.0 * monitored[203] * monitored[211]
    )
    monitored[215] = (
        2.0 * monitored[199] * monitored[213] - 2.0 * monitored[198] * monitored[212]
    )
    monitored[216] = Pnak * (monitored[155] * monitored[214] + zk * monitored[215])

    # Expressions for the IKb component
    monitored[217] = 1.0 / (
        1.0 + 2.202363450949239 * math.exp(-0.05452562704471101 * v)
    )
    GKb *= GKb_rate
    monitored[218] = GKb * (-monitored[116] + v) * monitored[217]

    # Expressions for the INab component
    monitored[219] = (
        PNab
        * (-nao + math.exp(monitored[119]) * nai)
        * monitored[118]
        / (-1.0 + math.exp(monitored[119]))
    )

    # Expressions for the ICab component
    monitored[220] = (
        4.0
        * PCab
        * (-0.341 * cao + cai * math.exp(2.0 * monitored[119]))
        * monitored[118]
        / (-1.0 + math.exp(2.0 * monitored[119]))
    )

    # Expressions for the IpCa component
    GpCa *= GpCa_rate
    monitored[221] = GpCa * cai / (0.0005 + cai)

    # Expressions for the Isac (Pueyo)--> ns + k component
    monitored[222] = 0
    monitored[223] = 0

    # Expressions for the Istim component
    monitored[224] = amp * (t <= duration)

    # Expressions for the membrane potential component
    monitored[267] = (
        -monitored[222]
        - monitored[223]
        - monitored[100]
        - monitored[158]
        - monitored[194]
        - monitored[216]
        - monitored[218]
        - monitored[219]
        - monitored[220]
        - monitored[221]
        - monitored[224]
        - monitored[23]
        - monitored[31]
        - monitored[47]
        - monitored[77]
        - monitored[78]
        - monitored[79]
        - monitored[88]
        - monitored[95]
    )

    # Expressions for the diffusion fluxes component
    monitored[225] = 0.5 * nass - 0.5 * nai
    monitored[226] = 0.5 * kss - 0.5 * ki
    monitored[227] = 5.0 * cass - 5.0 * cai

    # Expressions for the ryanodione receptor component
    monitored[101] = 0.5 * bt
    monitored[102] = (
        -monitored[101]
        * monitored[77]
        / (1.0 + 25.62890625 * math.pow(1.0 / cajsr, 8.0))
    )
    monitored[103] = bt / (1.0 + 0.0123 / cajsr)
    monitored[104] = 0.001 if monitored[103] < 0.001 else monitored[103]
    monitored[268] = (-Jrelnp + monitored[102]) / monitored[104]
    monitored[105] = 1.25 * bt
    monitored[106] = 0.5 * monitored[105]
    monitored[107] = (
        -monitored[106]
        * monitored[77]
        / (1.0 + 25.62890625 * math.pow(1.0 / cajsr, 8.0))
    )
    monitored[108] = monitored[105] / (1.0 + 0.0123 / cajsr)
    monitored[109] = 0.001 if monitored[108] < 0.001 else monitored[108]
    monitored[269] = (-Jrelp + monitored[107]) / monitored[109]
    monitored[110] = 1.0 / (1.0 + KmCaMK / monitored[8])
    monitored[111] = (1.0 - monitored[110]) * Jrelnp + Jrelp * monitored[110]

    # Expressions for the calcium buffers component
    monitored[228] = 0.004375 * cai / (0.00092 + cai)
    monitored[229] = 0.01203125 * cai / (0.00075 + cai)
    monitored[230] = 1.0 / (1.0 + KmCaMK / monitored[8])
    monitored[231] = 0.0002625 * cansr
    monitored[232] = (
        -monitored[231]
        + (1.0 - monitored[230]) * monitored[228]
        + monitored[229] * monitored[230]
    )
    monitored[233] = 0.01 * cansr - 0.01 * cajsr

    # Expressions for the intracellular concentrations component
    monitored[270] = monitored[225] * monitored[6] / monitored[3] + (
        -monitored[219]
        - monitored[23]
        - monitored[31]
        - monitored[222] / 3
        - 3.0 * monitored[158]
        - 3.0 * monitored[216]
    ) * monitored[2] / (F * monitored[3])
    monitored[271] = -monitored[225] + (
        -monitored[78] - 3.0 * monitored[194]
    ) * monitored[2] / (F * monitored[6])
    monitored[272] = monitored[226] * monitored[6] / monitored[3] + (
        -monitored[223]
        - monitored[100]
        - monitored[218]
        - monitored[224]
        - monitored[47]
        - monitored[88]
        - monitored[95]
        - monitored[222] / 3
        + 2.0 * monitored[216]
    ) * monitored[2] / (F * monitored[3])
    monitored[273] = -monitored[226] - monitored[2] * monitored[79] / (F * monitored[6])
    monitored[112] = 1.0 / (
        1.0
        + cmdnmax * kmcmdn * math.pow(kmcmdn + cai, -2.0)
        + kmtrpn * trpnmax * math.pow(kmtrpn + cai, -2.0)
    )
    monitored[274] = (
        monitored[227] * monitored[6] / monitored[3]
        - monitored[232] * monitored[4] / monitored[3]
        + 0.5
        * (-monitored[220] - monitored[221] - monitored[222] / 3 + 2.0 * monitored[158])
        * monitored[2]
        / (F * monitored[3])
    ) * monitored[112]
    monitored[113] = 1.0 / (
        1.0
        + BSLmax * KmBSL * math.pow(KmBSL + cass, -2.0)
        + BSRmax * KmBSR * math.pow(KmBSR + cass, -2.0)
    )
    monitored[275] = (
        -monitored[227]
        + monitored[111] * monitored[5] / monitored[6]
        + 0.5
        * (-monitored[77] + 2.0 * monitored[194])
        * monitored[2]
        / (F * monitored[6])
    ) * monitored[113]
    monitored[276] = -monitored[233] * monitored[5] / monitored[4] + monitored[232]
    monitored[114] = 1.0 / (1.0 + csqnmax * kmcsqn * math.pow(kmcsqn + cajsr, -2.0))
    monitored[277] = (-monitored[111] + monitored[233]) * monitored[114]

    # Expressions for the mechanics component
    monitored[278] = 0
    monitored[279] = 0
    monitored[280] = 0
    monitored[281] = 0
    monitored[282] = 0
    monitored[283] = 0
    monitored[284] = 0
    monitored[234] = 0
    monitored[235] = 0
    monitored[236] = 0

    # Return results
    return monitored
