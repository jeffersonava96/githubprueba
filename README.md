# Calculadora Aritmética (consola + GUI)

Pequeña calculadora en Python que soporta suma, resta, multiplicación y división.

Uso
- Consola:

```bash
python main.py
```

- Interfaz gráfica (tkinter):

```bash
python main.py gui
```

Tests

Instalar dependencias y ejecutar tests:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

CI

Se incluye un workflow de GitHub Actions en `.github/workflows/ci.yml` que ejecuta los tests en `push` y `pull_request`.

Archivos clave
- `main.py` — calculadora (consola y GUI)
- `tests/test_calc.py` — tests unitarios
- `requirements.txt` — dependencias para test (`pytest`)
- `.github/workflows/ci.yml` — workflow de CI

Licencia

Proyecto de ejemplo sin licencia específica.
