import math

def foura(a, b, c, d):
    """
    Forward and Backward Pass For 4a
    """
    ### FORWARD PASS ###
    # step 1
    E = a * b
    F = c + d

    # step 2
    G = E * F

    # step 3
    H = math.exp(G)

    # step 4
    L = 1 / H


    ### BACKWARD PASS ###
    # step 1
    dL_dL = 1

    # step 2
    dL_dH = -1 / (H ** 2) * dL_dL

    # step 3
    dH_dG = H
    dL_dG = dL_dH * dH_dG

    # step 4
    dG_dE = F
    dG_dF = E
    dL_dE = dL_dG * dG_dE
    dL_dF = dL_dG * dG_dF

    # step 5
    dE_da = b
    dE_db = a
    dL_da = dL_dE * dE_da
    dL_db = dL_dE * dE_db

    # step 6
    dF_dc = 1
    dF_dd = 1
    dL_dc = dL_dF * dF_dc
    dL_dd = dL_dF * dF_dd

    # return gradients
    return dL_da, dL_db, dL_dc, dL_dd


def fourc(x, y, z):
    """
    Forward and Backward Pass For 4c
    """
    ### FORWARD PASS ###
    # step 1
    A = x * 2
    B = 1 / x
    C = 3 * y

    # step 2
    D = A - B
    E = C * z

    # step 3
    F = D + E

    # step 4
    G = math.exp(F)

    # step 5
    H = G + 1

    # step 6
    L = 1 / H


    ### BACKWARD PASS ###
    # Start backward pass
    dL_dL = 1  # Gradient of L w.r.t. L

    # Step 6: L = 1 / H
    dL_dH = -1 / (H ** 2) * dL_dL

    # Step 5: H = G + 1
    dH_dG = 1
    dL_dG = dL_dH * dH_dG

    # Step 4: G = e^F
    dG_dF = G
    dL_dF = dL_dG * dG_dF

    # Step 3: F = D + E
    dF_dD = 1
    dF_dE = 1
    dL_dD = dL_dF * dF_dD
    dL_dE = dL_dF * dF_dE

    # Step 2a: D = A - B
    dD_dA = 1
    dD_dB = -1
    dL_dA = dL_dD * dD_dA
    dL_dB = dL_dD * dD_dB

    # Step 2b: E = C * z
    dE_dC = z
    dE_dz = C
    dL_dC = dL_dE * dE_dC
    dL_dz = dL_dE * dE_dz

    # Step 1a: A = x * 2
    dA_dx = 2
    dL_dx_A = dL_dA * dA_dx

    # Step 1b: B = 1 / x
    dB_dx = -1 / (x ** 2)
    dL_dx_B = dL_dB * dB_dx

    # Combine gradients for x from both paths (A and B contribute to dL/dx)
    dL_dx = dL_dx_A + dL_dx_B

    # Step 1c: C = 3 * y
    dC_dy = 3
    dL_dy = dL_dC * dC_dy

    # Return gradients w.r.t. each input variable
    return dL_dx, dL_dy, dL_dz




print(foura(1, 2, 3, 4))

print(fourc(1, 2, 3))

