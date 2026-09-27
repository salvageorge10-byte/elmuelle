document.documentElement.classList.add('js');

const reducido = matchMedia('(prefers-reduced-motion: reduce)').matches;
const esMobile = matchMedia('(max-width: 767px)').matches;

// Animaciones de entrada: cada elemento con data-anim aparece al entrar en pantalla,
// como las "Entrance animations" de Elementor del original.
const conAnimacion = document.querySelectorAll('[data-anim]');
const observador = new IntersectionObserver((entradas) => {
  entradas.forEach(({ isIntersecting, target }) => {
    if (!isIntersecting) return;
    target.classList.remove('invisible');
    target.classList.add('animado', target.dataset.animActiva);
    observador.unobserve(target);
  });
});

conAnimacion.forEach((el) => {
  const nombre = esMobile ? (el.dataset.animMobile ?? el.dataset.anim) : el.dataset.anim;
  if (reducido || nombre === 'none') return;
  el.dataset.animActiva = nombre;
  el.classList.add('invisible');
  observador.observe(el);
});

// Carrusel continuo: se duplican las fotos para que el recorrido no tenga corte.
const pista = document.querySelector('.carrusel__pista');
if (pista) {
  const fotos = [...pista.children];
  pista.style.setProperty('--cantidad', fotos.length);
  fotos.forEach((foto) => {
    const copia = foto.cloneNode();
    copia.alt = '';
    copia.setAttribute('aria-hidden', 'true');
    pista.append(copia);
  });
}

// Botón "volver arriba"
const arriba = document.querySelector('.arriba');
const alScrollear = () => arriba.classList.toggle('visible', scrollY > 300);
addEventListener('scroll', alScrollear, { passive: true });
alScrollear();

// Menú mobile
const botonMenu = document.querySelector('.menu-boton');
const nav = document.querySelector('.navegacion');
botonMenu.addEventListener('click', () => {
  const abierto = nav.classList.toggle('abierta');
  botonMenu.setAttribute('aria-expanded', abierto);
  botonMenu.setAttribute('aria-label', abierto ? 'Cerrar menú' : 'Abrir menú');
  botonMenu.firstElementChild.className = abierto ? 'fa-solid fa-xmark' : 'fa-solid fa-bars';
});
nav.addEventListener('click', (e) => {
  if (e.target.closest('a') && nav.classList.contains('abierta')) botonMenu.click();
});

// Formularios: validación, contador de caracteres y nombre del CV.
// El envío todavía no está conectado a ningún servicio (ver PENDIENTES.md):
// cuando haya un endpoint (Formspree, backend propio, etc.), ponerlo en ENVIO_FORMULARIOS.
const ENVIO_FORMULARIOS = '';

document.querySelectorAll('[data-formulario]').forEach((form) => {
  const estado = form.querySelector('.formulario__estado');

  form.querySelectorAll('.campo--area').forEach((campo) => {
    const area = campo.querySelector('textarea');
    const contador = campo.querySelector('.campo__contador');
    const actualizar = () => { contador.textContent = `${area.value.length} / ${area.maxLength}`; };
    area.addEventListener('input', actualizar);
  });

  const archivo = form.querySelector('.campo-archivo input');
  if (archivo) {
    archivo.addEventListener('change', () => {
      form.querySelector('.campo-archivo__nombre').textContent = archivo.files[0]?.name || 'No elegiste ningún archivo';
    });
  }

  const limpiarError = (campo) => {
    campo.classList.remove('campo--error');
    campo.querySelector('.campo__error')?.remove();
  };
  form.addEventListener('input', (e) => {
    const campo = e.target.closest('.campo');
    if (campo) limpiarError(campo);
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    let primero = null;
    form.querySelectorAll('input, textarea').forEach((el) => {
      const campo = el.closest('.campo');
      if (!campo) return;
      limpiarError(campo);
      if (el.checkValidity()) return;
      const msg = document.createElement('span');
      msg.className = 'campo__error';
      msg.textContent = el.validity.valueMissing ? 'Este dato es obligatorio.' : 'Revisá este dato: el formato no es válido.';
      campo.classList.add('campo--error');
      campo.append(msg);
      primero ??= el;
    });
    if (primero) { primero.focus(); return; }

    estado.hidden = false;
    if (!ENVIO_FORMULARIOS) {
      estado.textContent = 'Todo en orden. Falta conectar el envío del formulario: todavía no llega a ningún correo.';
      return;
    }
    estado.textContent = 'Enviando…';
    try {
      const r = await fetch(ENVIO_FORMULARIOS, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
      if (!r.ok) throw new Error(r.status);
      form.reset();
      form.querySelectorAll('.campo__contador').forEach((c) => { c.textContent = c.textContent.replace(/^\d+/, '0'); });
      estado.textContent = '¡Gracias! Recibimos tu mensaje y te vamos a responder a la brevedad.';
    } catch {
      estado.textContent = 'No pudimos enviar el formulario. Probá de nuevo en unos minutos.';
    }
  });
});
