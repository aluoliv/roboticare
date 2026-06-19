// ===== Navegação mobile =====
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // ===== Submenu "Módulos" (clique e teclado; hover via CSS opcional) =====
  document.querySelectorAll('.has-sub > button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var parent = btn.closest('.has-sub');
      var isOpen = parent.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.has-sub.open').forEach(function (el) {
      if (!el.contains(e.target)) {
        el.classList.remove('open');
        var b = el.querySelector('button');
        if (b) b.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // ===== Animação da grade de LEDs no hero =====
  // Cada padrão é uma matriz 5x5 (1 = LED aceso). O hero cicla entre eles,
  // como se o próprio board estivesse "contando" os módulos do curso.
  var stage = document.querySelector('[data-led-hero]');
  if (stage) {
    var patterns = [
      // power-on (boas-vindas)
      [0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1, 0,1,1,1,0, 0,0,1,0,0],
      // seta (lógica / fluxo de programação)
      [0,0,1,0,0, 0,0,0,1,0, 1,1,1,1,1, 0,0,0,1,0, 0,0,1,0,0],
      // sensor (leitura irradiando)
      [0,0,1,0,0, 0,1,0,1,0, 1,0,1,0,1, 0,1,0,1,0, 0,0,1,0,0],
      // cruz (interdisciplinar)
      [0,0,1,0,0, 0,0,1,0,0, 1,1,1,1,1, 0,0,1,0,0, 0,0,1,0,0],
      // estrela (projeto final / conquista)
      [0,0,1,0,0, 1,0,1,0,1, 0,1,1,1,0, 1,0,1,0,1, 0,0,1,0,0]
    ];
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var idx = 0;

    function buildGrid() {
      stage.innerHTML = '';
      for (var i = 0; i < 25; i++) {
        var d = document.createElement('div');
        d.className = 'led';
        stage.appendChild(d);
      }
    }
    function paint(pattern) {
      var leds = stage.querySelectorAll('.led');
      pattern.forEach(function (v, i) {
        leds[i].classList.toggle('on', !!v);
        leds[i].classList.toggle('pulse', !!v);
      });
    }
    buildGrid();
    paint(patterns[0]);

    if (!reduceMotion) {
      setInterval(function () {
        idx = (idx + 1) % patterns.length;
        paint(patterns[idx]);
      }, 2600);
    }
  }
});
