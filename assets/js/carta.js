// Arma la carta a partir de window.CARTA (carta-datos.js), con buscador y accesos a cada categoría.
(() => {
  const contenedor = document.getElementById('carta-productos');
  const chips = document.querySelector('.chips');
  const buscador = document.getElementById('buscar');
  const vacia = document.querySelector('.carta-vacia');

  const normalizar = (t) => t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  const slug = (t) => normalizar(t).replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
  const precio = (n) => '$ ' + n.toLocaleString('es-AR');

  contenedor.innerHTML = window.CARTA.map(({ categoria, foto, fotoAlt, productos }, i) => `
    <section class="cat${foto ? '' : ' cat--sin-foto'}" id="${slug(categoria)}" aria-labelledby="t-${slug(categoria)}">
      <header class="cat__cabeza">
        <span class="cat__num">Sector ${String(i + 1).padStart(2, '0')} · ${productos.length} ${productos.length === 1 ? 'opción' : 'opciones'}</span>
        <h2 class="cat__nombre" id="t-${slug(categoria)}">${categoria}</h2>
        ${foto ? `<img class="cat__foto" src="${foto}" alt="${fotoAlt}" loading="lazy" width="360" height="270">` : ''}
      </header>
      <ul class="cat__lista">
        ${productos.map((p) => `
        <li class="item" data-busqueda="${normalizar(p.nombre + ' ' + p.descripcion + ' ' + categoria)}">
          <div class="item__fila">
            <h3 class="item__nombre">${p.nombre}</h3>
            <span class="item__puntos" aria-hidden="true"></span>
            <span class="item__precio">${precio(p.precio)}</span>
          </div>
          <p class="item__desc">${p.descripcion}</p>
        </li>`).join('')}
      </ul>
    </section>`).join('');

  chips.innerHTML = window.CARTA.map(({ categoria }) => `<a href="#${slug(categoria)}">${categoria}</a>`).join('');

  // Si se llegó con #categoria desde otra página, saltar ahí una vez armada la carta.
  if (location.hash) document.getElementById(location.hash.slice(1))?.scrollIntoView();

  const secciones = [...contenedor.querySelectorAll('.cat')];
  buscador.addEventListener('input', () => {
    const q = normalizar(buscador.value.trim());
    let hay = false;
    secciones.forEach((s) => {
      let visibles = 0;
      s.querySelectorAll('.item').forEach((it) => {
        const ok = !q || it.dataset.busqueda.includes(q);
        it.hidden = !ok;
        if (ok) visibles++;
      });
      s.hidden = visibles === 0;
      if (visibles) hay = true;
    });
    vacia.hidden = hay;
  });
})();
