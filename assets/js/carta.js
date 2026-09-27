// Arma la carta a partir de window.CARTA (carta-datos.js), con buscador y salto a categorías.
(() => {
  const contenedor = document.getElementById('carta-productos');
  const lista = document.getElementById('lista-categorias');
  const botonCategorias = document.querySelector('.buscador__boton');
  const buscador = document.getElementById('buscar');
  const vacia = document.querySelector('.carta-vacia');

  const slug = (t) => t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
  const precio = (n) => '$' + n.toLocaleString('es-AR');
  const normalizar = (t) => t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');

  contenedor.innerHTML = window.CARTA.map(({ categoria, productos }) => `
    <section class="categoria" id="${slug(categoria)}">
      <h2 class="categoria__titulo">${categoria}</h2>
      <ul class="categoria__grilla">
        ${productos.map((p) => `
        <li class="producto" data-busqueda="${normalizar(p.nombre + ' ' + p.descripcion)}">
          <img class="producto__foto" src="${p.foto}" alt="${p.nombre}" loading="lazy" width="373" height="225">
          <div class="producto__cuerpo">
            <h3 class="producto__nombre">${p.nombre}</h3>
            <p class="producto__precio">${precio(p.precio)}</p>
            <p class="producto__desc">${p.descripcion}</p>
          </div>
        </li>`).join('')}
      </ul>
    </section>`).join('');

  // Si se llegó con un #categoria, saltar ahí una vez armada la carta
  if (location.hash) document.getElementById(location.hash.slice(1))?.scrollIntoView();

  lista.innerHTML = window.CARTA.map(({ categoria }) => `<li><a href="#${slug(categoria)}">${categoria}</a></li>`).join('');

  const cerrarLista = () => { lista.hidden = true; botonCategorias.setAttribute('aria-expanded', 'false'); };
  botonCategorias.addEventListener('click', () => {
    const abrir = lista.hidden;
    lista.hidden = !abrir;
    botonCategorias.setAttribute('aria-expanded', String(abrir));
  });
  lista.addEventListener('click', (e) => { if (e.target.closest('a')) cerrarLista(); });
  document.addEventListener('click', (e) => { if (!e.target.closest('.buscador__categorias')) cerrarLista(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') cerrarLista(); });

  const secciones = [...contenedor.querySelectorAll('.categoria')];
  buscador.addEventListener('input', () => {
    const q = normalizar(buscador.value.trim());
    let hay = false;
    secciones.forEach((s) => {
      let visibles = 0;
      s.querySelectorAll('.producto').forEach((p) => {
        const ok = !q || p.dataset.busqueda.includes(q);
        p.hidden = !ok;
        if (ok) visibles++;
      });
      s.hidden = visibles === 0;
      if (visibles) hay = true;
    });
    vacia.hidden = hay;
  });
})();
