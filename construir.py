"""Arma las páginas del sitio.

Cabecera, bloque "El origen" y pie son comunes a todas las páginas y viven acá.
El contenido de cada página está en fuente/<nombre>.html; la primera línea es
<!-- titulo | descripcion -->. Correr:  python construir.py
"""
from pathlib import Path

RAIZ = Path(__file__).parent
MARCA = "El Muelle"

NAV = [
    ("index.html", "Inicio"),
    ("nosotros.html", "Nosotros"),
    ("carta.html", "Carta"),
    ("franquicias.html", "Franquicias"),
    ("blog.html", "Blog"),
    ("prensa.html", "Prensa"),
    ("contacto.html", "Contacto"),
]

REDES = """<li><a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook"></i></a></li>
        <li><a href="#" aria-label="X"><i class="fa-brands fa-x-twitter"></i></a></li>
        <li><a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a></li>
        <li><a href="#" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a></li>"""


def logo(clase, enlace=False):
    interior = """<i class="fa-solid fa-anchor logo__ancla" aria-hidden="true"></i>
        <span class="logo__nombre" aria-hidden="true"><small>El</small>Muelle</span>"""
    if enlace:
        return f'<a href="index.html" class="logo {clase}" aria-label="{MARCA}, inicio">\n        {interior}\n      </a>'
    return f'<span class="logo {clase}" role="img" aria-label="{MARCA}">\n        {interior}\n      </span>'


def nav(actual):
    items = []
    for href, texto in NAV:
        cur = ' aria-current="page"' if href == actual else ""
        items.append(f'<li><a href="{href}"{cur}>{texto}</a></li>')
    return "\n        ".join(items)


def cabecera(actual):
    return f"""  <header class="cabecera">
    <div class="cabecera__fila contenedor">
      {logo("logo--cabecera", enlace=True)}
      <ul class="redes" aria-label="Redes sociales">
        {REDES}
      </ul>
      <button class="menu-boton" aria-expanded="false" aria-controls="navegacion" aria-label="Abrir menú">
        <i class="fa-solid fa-bars" aria-hidden="true"></i>
      </button>
    </div>
    <nav id="navegacion" class="navegacion contenedor" aria-label="Principal">
      <ul>
        {nav(actual)}
      </ul>
    </nav>
  </header>"""


LEYENDA = """  <section class="leyenda">
    <div class="contenedor">
      <h2 class="titulo-rudo titulo-rudo--versalitas">El Origen de la Hamburguesa</h2>
      <p>Desde el sur, un puñado de inconformistas del sabor se animó a cambiar las reglas.<br>Con fuego en el pecho y ganas de hacer algo auténtico, crearon hamburguesas como ninguna otra.<br>Hoy esa misión sigue en marcha.</p>
      <a href="trabaja-con-nosotros.html" class="boton boton--claro boton--redondeado">Sumate a la tripulación →</a>
    </div>
  </section>"""


def pie(actual):
    navegacion = "\n            ".join(
        f'<li><a href="{h}">{t}</a></li>' for h, t in NAV if h != "franquicias.html"
    )
    return f"""  <footer class="pie">
    <div class="contenedor">
      {logo("logo--pie flota-hover")}
      <p class="pie__bajada">Nos gusta ofrecer una experiencia gastronómica distinta, donde el producto, el lugar y la atención van de la mano.<br>Gracias a quienes nos eligen, seguimos creciendo con el mismo sabor de siempre.<br>¡Vení y sumate a nuestra historia!</p>

      <div class="pie__columnas">
        <div class="pie__col">
          <h2>Navegación</h2>
          <ul>
            {navegacion}
          </ul>
        </div>
        <div class="pie__col">
          <h2>Información</h2>
          <ul>
            <li><a href="franquicias.html">Sumate a la franquicia</a></li>
            <li><a href="trabaja-con-nosotros.html">Trabajá con nosotros</a></li>
            <li><a href="nosotros.html#marcas">Sobre Smash Co.</a></li>
            <li><a href="nosotros.html#marcas">Sobre Papas &amp; Go</a></li>
          </ul>
          <ul class="redes redes--pie" aria-label="Redes sociales">
            {REDES}
          </ul>
        </div>
        <div class="pie__marcas">
          <div class="pie__marcas-logos" aria-hidden="true">
            <span class="submarca submarca--smash">Smash<br>Co.</span>
            <span class="submarca submarca--papas">Papas<br>&amp; Go</span>
          </div>
          <p>Nuestro grupo gastronómico suma marcas que comparten la misma pasión por la comida bien hecha.</p>
        </div>
      </div>
    </div>
    <div class="pie__legal contenedor">© Copyright {MARCA} / <a href="privacidad.html">Política de privacidad y cookies</a></div>
  </footer>

  <a href="#arriba" class="arriba" aria-label="Volver arriba"><i class="fa-solid fa-chevron-up" aria-hidden="true"></i></a>"""


def pagina(archivo, titulo, descripcion, cuerpo, scripts):
    extra = "".join(f'\n  <script src="{s}"></script>' for s in scripts)
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titulo}</title>
  <meta name="description" content="{descripcion}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:opsz,wght@6..12,400;6..12,500;6..12,600;6..12,700;6..12,800&family=Permanent+Marker&family=Rubik+Dirt&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
  <link rel="stylesheet" href="styles.css">
</head>
<body id="arriba">

{cabecera(archivo)}

  <main>
{cuerpo.rstrip()}
  </main>

{LEYENDA}

{pie(archivo)}
{extra}
  <script src="main.js"></script>
</body>
</html>
"""


def construir():
    for fuente in sorted((RAIZ / "fuente").glob("*.html")):
        lineas = fuente.read_text(encoding="utf-8").split("\n", 2)
        meta = lineas[0].strip().removeprefix("<!--").removesuffix("-->").split("|")
        titulo, descripcion = meta[0].strip(), meta[1].strip()
        scripts = [s.strip() for s in meta[2].split(",")] if len(meta) > 2 and meta[2].strip() else []
        archivo = "index.html" if fuente.stem == "inicio" else f"{fuente.stem}.html"
        html = pagina(archivo, titulo, descripcion, lineas[1] + "\n" + lineas[2], scripts)
        (RAIZ / archivo).write_text(html, encoding="utf-8")
        print("✓", archivo)


if __name__ == "__main__":
    construir()
