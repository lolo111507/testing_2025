## Testing_2025

*Repositorio para Espacio Curricular de Testing - Escuela PROA - Corral de Bustos*
**2025**

``` JavaScript
// suma.js
function sumar(a, b) {
    return a + b;
}

module.exports = sumar;


// suma.test.js
const sumar = require('./suma');

test('suma 1 + 2 para obtener 3', () => {
    expect(sumar(1, 2)).toBe(3);
});
```

_*lole*_
