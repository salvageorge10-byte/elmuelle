"""Arma las páginas del sitio.

Cabecera, cierre y pie son comunes a todas las páginas y viven acá.
El contenido de cada página está en fuente/<nombre>.html; la primera línea es
<!-- titulo | descripcion | scripts extra separados por coma -->.
Correr:  python construir.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).parent
MARCA = "El Muelle"

NAV = [
    ("index.html", "Inicio"),
    ("carta.html", "Carta"),
    ("nosotros.html", "Nosotros"),
    ("franquicias.html", "Franquicias"),
    ("blog.html", "Blog"),
    ("prensa.html", "Prensa"),
    ("contacto.html", "Contacto"),
]

REDES = """<li><a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a></li>
          <li><a href="#" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a></li>
          <li><a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a></li>
          <li><a href="#" aria-label="X"><i class="fa-brands fa-x-twitter"></i></a></li>"""


def logo(clase=""):
    return f"""<a href="index.html" class="logo {clase}" aria-label="{MARCA}, inicio">
        <i class="fa-solid fa-anchor logo__ancla" aria-hidden="true"></i>
        <span class="logo__nombre"><small>El</small>Muelle</span>
      </a>"""


def cabecera(actual):
    actual_attr = ' aria-current="page"'
    items = "\n          ".join(
        f'<li><a href="{h}"{actual_attr if h == actual else ""}>{t}</a></li>' for h, t in NAV
    )
    return f"""  <a class="saltar" href="#contenido">Saltar al contenido</a>
  <header class="cabecera">
    <div class="contenedor cabecera__fila">
      {logo("logo--cabecera")}
      <ul class="redes cabecera__redes" aria-label="Redes sociales">
          {REDES}
      </ul>
      <button class="menu-boton" aria-expanded="false" aria-controls="navegacion" aria-label="Abrir menú">
        <span></span><span></span><span></span>
      </button>
    </div>
    <nav id="navegacion" class="navegacion" aria-label="Principal">
      <ul class="contenedor">
          {items}
      </ul>
    </nav>
  </header>"""


CIERRE = """  <section class="cierre" style="--fondo:url('assets/img/m-muelle-luces.jpg')">
    <div class="contenedor cierre__grilla">
      <h2 class="cierre__titulo" data-anim="fadeInLeft" data-anim-mobile="fadeInUp">Te esperamos<br>en el muelle</h2>
      <div class="cierre__texto" data-anim="fadeInRight" data-anim-mobile="fadeInUp">
        <p>Plancha caliente desde el mediodía hasta tarde. Vení con hambre, pedí una doble y quedate a la segunda pinta.</p>
        <div class="cierre__botones">
          <a href="carta.html" class="boton boton--amarillo">Ver la carta completa</a>
          <a href="franquicias.html" class="boton boton--linea-clara">Quiero una franquicia</a>
        </div>
      </div>
    </div>
  </section>"""


def pie():
    nav = "\n            ".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""  <footer class="pie">
    <div class="contenedor pie__grilla">
      <div class="pie__marca">
        {logo("logo--pie")}
        <p>Hamburguesas smash hechas al momento, papas cortadas en casa y cerveza tirada. Una marca que empezó con una plancha y hoy suma locales franquiciados.</p>
        <ul class="redes" aria-label="Redes sociales">
          {REDES}
        </ul>
      </div>
      <div class="pie__col">
        <h2>Navegación</h2>
        <ul>
            {nav}
        </ul>
      </div>
      <div class="pie__col">
        <h2>La marca</h2>
        <ul>
          <li><a href="franquicias.html">Sumá tu franquicia</a></li>
          <li><a href="trabaja-con-nosotros.html">Trabajá con nosotros</a></li>
          <li><a href="carta.html#bebidas">La barra</a></li>
          <li><a href="creditos.html">Créditos de fotos</a></li>
        </ul>
      </div>
      <div class="pie__col pie__col--placa">
        <h2>Bitácora</h2>
        <dl class="placa placa--oscura">
          <div><dt>Plancha</dt><dd>Smash, 2 × 100 g</dd></div>
          <div><dt>Pan</dt><dd>De papa, del día</dd></div>
          <div><dt>Papas</dt><dd>Cortadas en casa</dd></div>
          <div><dt>Canillas</dt><dd>Rubia · Roja · IPA</dd></div>
        </dl>
      </div>
    </div>
    <div class="contenedor pie__legal">
      <span>© {MARCA}</span>
      <a href="privacidad.html">Privacidad y cookies</a>
      <a href="creditos.html">Créditos de fotos</a>
    </div>
  </footer>

  <a href="#arriba" class="arriba" aria-label="Volver arriba"><i class="fa-solid fa-arrow-up" aria-hidden="true"></i></a>"""


def pagina(archivo, titulo, descripcion, cuerpo, scripts, con_cierre):
    clase = archivo.removesuffix(".html")
    extra = "".join(f'\n  <script src="{s}"></script>' for s in scripts)
    cierre = ("\n\n" + CIERRE) if con_cierre else ""
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titulo}</title>
  <meta name="description" content="{descripcion}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700;6..12,800&family=Permanent+Marker&family=Rubik+Dirt&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
  <link rel="stylesheet" href="styles.css">
</head>
<body id="arriba" class="pagina-{clase}">

{cabecera(archivo)}

  <main id="contenido">
{cuerpo.rstrip()}
  </main>{cierre}

{pie()}
{extra}
  <script src="main.js"></script>
</body>
</html>
"""


def construir():
    for fuente in sorted((RAIZ / "fuente").glob("*.html")):
        primera, resto = fuente.read_text(encoding="utf-8").split("\n", 1)
        meta = [m.strip() for m in primera.strip().removeprefix("<!--").removesuffix("-->").split("|")]
        titulo, descripcion = meta[0], meta[1]
        scripts = [s.strip() for s in meta[2].split(",")] if len(meta) > 2 and meta[2] else []
        archivo = "index.html" if fuente.stem == "inicio" else f"{fuente.stem}.html"
        con_cierre = fuente.stem not in ("privacidad", "creditos", "contacto", "trabaja-con-nosotros")
        (RAIZ / archivo).write_text(pagina(archivo, titulo, descripcion, resto, scripts, con_cierre), encoding="utf-8")
        print("ok", archivo)


if __name__ == "__main__":
    construir()
