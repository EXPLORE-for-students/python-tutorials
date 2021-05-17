def rho_NFW(*params):
    rho_s, rs = params
    def rho_function(r):
        return rho_s/(r/rs)/(1+r/rs)**2
    return rho_function

def rho_burkert(*params):
    rho_0, r0 = params
    def rho_function(r):
        return rho_0*r0**3/(r+r0)/(r**2+r0**2)
    return rho_function