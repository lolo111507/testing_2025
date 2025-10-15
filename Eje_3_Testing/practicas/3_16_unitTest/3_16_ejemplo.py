def es_par(n):
    return n % 2 == 0

### Test unitario básico con `assert`
# Pruebas manuales
assert es_par(2) == True
assert es_par(3) == False
assert es_par(0) == True
