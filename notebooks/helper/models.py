import numpy as np

def compute_y_linear_invariant(D: float, x: float) -> float:
    """Compute the token Y amount given the token X amount in a Linear Invariant 
    model.

    x + y = k -> y = k -x

    Args:
        D (float): total token at equilibrium
        x (float): amount of token X in the pool

    Returns:
        float: token Y amount
    """
    return D - x

def compute_y_product_invariant(D: float, x: float) -> float:
    """Compute the token Y amount given the token X amount in a Contasnt Product 
    Invariant model.

    Args:
        D (float): total token at equilibrium
        x (float): amount of token X in the pool

    Returns:
        float: token Y amount
    """
    return D / x

def compute_y_stableswap_no_chi (D: float, x: float) -> float:
    """Compute the token Y amount given the token X amount in a Stableswap model
    without the leverage parameter.

    Args:
        D (float): total token at equilibrium
        x (float): amount of token X in the pool

    Returns:
        float: token Y amount
    """
    return  (D + (D / 2) ** 2 - x) / (1 + x)

def compute_y_stableswap_static (D: float, x: float, chi: int = 2) -> float:
    """Compute the token Y amount given the token X amount in a Stableswap model
    with a static leverage parameter.

    Args:
        D (float): total token at equilibrium
        x (float): amount of token X in the pool
        chi (int): leverage parameter

    Returns:
        float: token Y amount
    """
    return  (chi * D + (D / 2) ** 2 - chi * x) / (chi + x)

def compute_y_stableswap_dynamic (D: float, x: float, A: int = 2) -> float:
    """Compute the token Y amount given the token X amount in a Stableswap model
    with a dynamic leverage parameter.

    Args:
        D (float): total token at equilibrium
        x (float): amount of token X in the pool
        A (int): dimensionles and dynamic leverage parameter

    Returns:
        float: token Y amount
    """

    t1 = (4 * (1 - 4 * A) * D * x + 16 * A * (x ** 2))
    t2 = 64 * A * (D ** 3) * x
    t3 = 32 * A * x
    y1 =  ( -t1 + np.sqrt(t1 ** 2 + t2) ) / ( t3 )
    # y2 = ( -t1 - np.sqrt(t1 ** 2 + t2) ) / ( t3 )
    return y1

def compute_dy (D: float, x: float) -> float:
    return -(1 + (D + (D / 2) ** 2 - x) / (1 + x)) / (1 + x)