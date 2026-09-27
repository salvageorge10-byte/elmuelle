# Pendientes antes de publicar

Esta réplica copia la estructura, los efectos y las fotos de eldesembarco.com. Tiene 10 páginas: inicio, nosotros, carta, franquicias, blog, un artículo, prensa, contacto, trabajá con nosotros y privacidad. No tiene sucursales, direcciones ni mapas.

## Cómo editar

- **Cabecera, bloque "El origen" y pie** están en `construir.py` (se repiten en todas las páginas).
- **El contenido de cada página** está en `fuente/<página>.html`.
- **La carta** (productos, precios, descripciones y fotos) está en `assets/js/carta-datos.js`. La página se arma sola a partir de ese archivo.
- Después de tocar `construir.py` o algo de `fuente/`, correr `python construir.py` para regenerar las páginas.

## Lo que hay que reemplazar

1. **Nombre y logo.** "El Muelle" y el ancla son provisorios: el nombre se cambia en `construir.py` (variable `MARCA` y la función `logo`) y en los textos de `fuente/`.
2. **Fotos.** Todas son del sitio original. **Varias de la carta tienen el logo de El Desembarco impreso** (vasos de tragos, cervezas y latas): esas hay que cambiarlas sí o sí. La lista de la home está en `IMAGENES.md`; las de la carta están en `assets/img/carta/`.
3. **Carta.** Los productos y los **precios son los del original**. Se cambiaron los nombres propios (Bajoncito → Ancla, Normandía → Tormenta, etc.) y se reescribieron las descripciones, pero hay que cargar los productos y precios reales en `assets/js/carta-datos.js`.
4. **Cifras** (inicio): 50 locales, 700.456 hamburguesas, 97%, 504.007 pedidos y +1,5M de seguidores son **datos de El Desembarco**.
5. **Historia y datos de "Nosotros" y "Franquicias"**: 2017, 50 franquicias, meta de 70 locales y 200 franquicias para 2027, centro de producción y flota de camiones son **datos del original**.
6. **Submarcas** ("Smash Co." y "Papas & Go"): son inventadas para ocupar el lugar de Mr. Tasty y Mila & Go. Aparecen en el pie y en Nosotros. Reemplazarlas o sacarlas.
7. **Formularios** (franquicias, contacto y trabajá con nosotros): validan todo, pero **todavía no envían a ningún lado**. Hay que conectar un servicio (por ejemplo Formspree) y poner su dirección en `ENVIO_FORMULARIOS`, en `main.js`. Mientras tanto, al enviar muestran un aviso de que falta conectarlo.
8. **Redes sociales.** Los íconos apuntan a `#`: faltan los links reales.
9. **Opiniones.** El espacio debajo del título es para el widget de reseñas de Google de la marca.
10. **Franquicias.** En el original hay un video de YouTube de ellos; acá va una foto en su lugar. Si la marca tiene video, se pone ahí.
11. **Política de privacidad.** Es un texto de referencia: revisarlo con un abogado antes de publicar.
12. **Fuentes.** Las del original son pagas (A Love of Thunder, Avenir). Se reemplazaron por Rubik Dirt y Nunito Sans, que son gratuitas.
