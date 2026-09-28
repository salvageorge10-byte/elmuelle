# El Muelle — rediseño

Sitio de muestra de una hamburguesería con franquicias. Dirección visual: **señalética de puerto** (azul puerto, papel kraft, rojo señal, amarillo seguridad; Big Shoulders + Archivo + IBM Plex Mono). Mantiene los efectos del sitio anterior: entradas desde los costados y desde abajo (1,25 s), tira de fotos continua, fondos fijos al scrollear y fotos que flotan.

## Cómo editar

- **Cabecera, cierre y pie** (se repiten en todas las páginas): `construir.py`.
- **Contenido de cada página**: `fuente/<página>.html`.
- **Carta** (productos, precios, descripciones, foto de cada categoría): `assets/js/carta-datos.js`.
- Después de tocar `construir.py` o `fuente/`, correr `python construir.py`.

## Fotos

Todas son fotos con licencia **Creative Commons** sacadas de Openverse (Flickr y otros). **Ninguna es de El Desembarco.** La página `creditos.html` lista autor, obra original y licencia de cada una, y está enlazada desde el pie: **no la borres mientras uses estas fotos**, porque las licencias CC BY y CC BY-SA exigen citar al autor. Siete fotos son CC BY-ND (sin obras derivadas): se muestran recortadas por el diseño, pero no se les aplicaron filtros ni retoques.

Cuando la marca tenga fotos propias, se reemplazan manteniendo el nombre del archivo, y se sacan de `creditos.html`.

## Datos de muestra que hay que reemplazar

1. **Nombre y logo.** "El Muelle" es provisorio: variable `MARCA` y función `logo` en `construir.py`, más los textos de `fuente/`.
2. **Cifras** del inicio (50 locales, 700.456 hamburguesas, 504.007 pedidos, 97 %, +1,5 M): son de referencia.
3. **Historia y línea de tiempo** de Nosotros (2017, 2019, 2021, +50 locales, centro de producción): son de muestra.
4. **Submarcas** "Smash Co." y "Papas & Go" en Nosotros: inventadas, reemplazar o quitar.
5. **Carta y precios**: los productos y precios son de referencia.
6. **Frases operativas**: "Plancha caliente desde el mediodía hasta tarde" (cierre) y "Pedidos y reservas por redes" (franja superior). Ajustarlas a los horarios y canales reales.
7. **Formularios** (franquicias, contacto, trabajá con nosotros): validan, pero **no envían a ningún lado**. Poner la dirección del servicio (por ejemplo Formspree) en `ENVIO_FORMULARIOS`, en `main.js`.
8. **Redes sociales**: los íconos apuntan a `#`.
9. **Política de privacidad**: texto de referencia, revisarlo con un abogado.
