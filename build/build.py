#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera as páginas estáticas do site do curso "Robótica Educacional com
BBC micro:bit" a partir de um template comum (header/nav + footer),
para publicação no GitHub Pages.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODULES = [
    {
        "slug": "modulo-1",
        "title": "Introdução à Robótica Educacional e ao BBC micro:bit",
        "short": "Introdução ao micro:bit",
        "dur": "2h",
        "formato": "Síncrono",
        "objetivo": "Compreender o papel pedagógico da robótica educacional e reconhecer os recursos do BBC micro:bit.",
        "topicos": [
            "O que é robótica educacional e por que ela importa na formação dos alunos",
            "Apresentação do hardware: LEDs, botões, sensores, rádio e Bluetooth",
            "Instalação e configuração do ambiente MakeCode (navegador e app)",
            "Pareamento do dispositivo e primeira transferência de programa",
        ],
        "atividade": "Criar e transferir um programa simples que exiba o nome do professor na matriz de LEDs.",
        "icon": [0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1, 0,1,1,1,0, 0,0,1,0,0],
    },
    {
        "slug": "modulo-2",
        "title": "Programação em Blocos com o MakeCode",
        "short": "Programação em Blocos",
        "dur": "3h",
        "formato": "Síncrono",
        "objetivo": "Aplicar lógica de programação básica (sequência, repetição e condicionais) usando blocos.",
        "topicos": [
            "Tour pela interface do editor MakeCode",
            "Estruturas de repetição (loops) e condicionais (se/então)",
            "Eventos (ao pressionar botão, ao agitar) e variáveis",
            "Boas práticas para planejar um algoritmo antes de programar",
        ],
        "atividade": "Desenvolver um pequeno jogo de reação ou animação interativa.",
        "icon": [0,0,1,0,0, 0,0,0,1,0, 1,1,1,1,1, 0,0,0,1,0, 0,0,1,0,0],
    },
    {
        "slug": "modulo-3",
        "title": "Sensores e Entradas",
        "short": "Sensores e Entradas",
        "dur": "3h",
        "formato": "Síncrono + atividade assíncrona",
        "objetivo": "Utilizar os sensores embarcados para captar dados do ambiente.",
        "topicos": [
            "Acelerômetro e detecção de movimento/gestos",
            "Sensor de luminosidade e de temperatura",
            "Botões, toque e pino de entrada",
            "Exibição de dados capturados na matriz de LEDs",
        ],
        "atividade": "Montar uma mini estação de monitoramento (luz e temperatura) com leitura em tempo real.",
        "icon": [0,0,1,0,0, 0,1,0,1,0, 1,0,1,0,1, 0,1,0,1,0, 0,0,1,0,0],
    },
    {
        "slug": "modulo-4",
        "title": "Atuadores, Saídas e Comunicação por Rádio",
        "short": "Atuadores e Comunicação",
        "dur": "3h",
        "formato": "Síncrono",
        "objetivo": "Explorar as formas de saída do micro:bit e a comunicação entre dispositivos.",
        "topicos": [
            "Matriz de LEDs e criação de imagens animadas",
            "Som e buzzer (built-in e externo)",
            "Comunicação por rádio entre dois ou mais micro:bits",
            "Aplicações pedagógicas da comunicação sem fio",
        ],
        "atividade": "Programar a troca de mensagens entre dois dispositivos em duplas.",
        "icon": [1,0,1,0,1, 0,0,0,0,0, 0,1,0,1,0, 0,0,0,0,0, 1,0,1,0,1],
    },
    {
        "slug": "modulo-5",
        "title": "Projetos Interdisciplinares e Estratégias Pedagógicas",
        "short": "Projetos Interdisciplinares",
        "dur": "3h",
        "formato": "Síncrono + atividade assíncrona",
        "objetivo": "Planejar aulas que integrem a robótica a outras áreas do currículo.",
        "topicos": [
            "Conexões com Matemática, Ciências e Artes",
            "Aprendizagem Baseada em Projetos (ABP) aplicada à robótica",
            "Adaptações para diferentes faixas etárias e contextos escolares",
            "Critérios para avaliar atividades práticas de robótica",
        ],
        "atividade": "Elaborar um plano de aula completo utilizando o micro:bit em outra disciplina.",
        "icon": [0,0,1,0,0, 0,0,1,0,0, 1,1,1,1,1, 0,0,1,0,0, 0,0,1,0,0],
    },
    {
        "slug": "modulo-6",
        "title": "Projeto Final, Avaliação e Certificação",
        "short": "Projeto Final e Certificação",
        "dur": "2h",
        "formato": "Síncrono",
        "objetivo": "Consolidar a aprendizagem por meio da apresentação de um projeto final.",
        "topicos": [
            "Apresentação dos planos de aula e projetos desenvolvidos",
            "Feedback entre pares e troca de boas práticas",
            "Critérios de avaliação e emissão de certificado",
            "Encerramento e indicação de próximos passos/recursos",
        ],
        "atividade": "Apresentar o projeto final desenvolvido ao longo do curso para a turma.",
        "icon": [0,0,1,0,0, 1,0,1,0,1, 0,1,1,1,0, 1,0,1,0,1, 0,0,1,0,0],
    },
]

NAV_ITEMS = [
    ("home", "index.html", "Início"),
    ("sobre", "sobre.html", "Sobre o Curso"),
    ("cronograma", "cronograma.html", "Cronograma"),
    ("modulos", "modulos.html", "Módulos"),
    ("materiais", "materiais.html", "Materiais"),
    ("avaliacao", "avaliacao.html", "Avaliação"),
    ("contato", "contato.html", "Contato"),
]


def led_grid_html(pattern, size_class="size-md", extra_class="", on_light=False):
    classes = "led-grid " + size_class
    if on_light:
        classes += " on-light"
    if extra_class:
        classes += " " + extra_class
    cells = "".join(
        '<div class="led{on}"></div>'.format(on=" on" if v else "")
        for v in pattern
    )
    return '<div class="{c}">{cells}</div>'.format(c=classes, cells=cells)


def nav_html(active):
    sub_open = "open" if active == "modulos" else ""
    sub_links = "\n".join(
        '            <a href="{slug}.html">{short}</a>'.format(slug=m["slug"], short=m["short"])
        for m in MODULES
    )
    items = []
    for key, href, label in NAV_ITEMS:
        if key == "modulos":
            items.append(
                '''        <div class="has-sub {sub_open}">
          <button type="button" aria-haspopup="true" aria-expanded="{exp}" aria-current="{cur}">{label} ▾</button>
          <div class="submenu">
            <a href="modulos.html">Visão geral dos módulos</a>
{sub_links}
          </div>
        </div>'''.format(
                    sub_open=sub_open,
                    exp="true" if sub_open else "false",
                    cur="page" if active == "modulos" else "false",
                    label=label,
                    sub_links=sub_links,
                )
            )
        else:
            current = ' aria-current="page"' if key == active else ""
            items.append('        <a href="{href}"{cur}>{label}</a>'.format(href=href, cur=current, label=label))
    return "\n".join(items)


HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Robótica Educacional com BBC micro:bit</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>
<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{prefix}index.html"><span class="brand-dot"></span> Robótica Educacional · micro:bit</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Abrir menu">☰</button>
    <nav class="main-nav" aria-label="Navegação principal">
{nav}
    </nav>
  </div>
</header>
<main id="conteudo">
"""

FOOTER = """</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <h4>Robótica Educacional com BBC micro:bit</h4>
      <p>Formação online de 16 horas para professores e educadores que querem levar a robótica para a sala de aula.</p>
    </div>
    <div>
      <h4>Navegação</h4>
      <ul>
        <li><a href="{prefix}sobre.html">Sobre o Curso</a></li>
        <li><a href="{prefix}cronograma.html">Cronograma</a></li>
        <li><a href="{prefix}modulos.html">Módulos</a></li>
        <li><a href="{prefix}materiais.html">Materiais e Recursos</a></li>
      </ul>
    </div>
    <div>
      <h4>Contato</h4>
      <ul>
        <li><a href="mailto:contato@seudominio.org">contato@seudominio.org</a></li>
        <li><a href="{prefix}contato.html">Página de contato e suporte</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-note">
    Curso independente de formação de educadores. BBC micro:bit é um produto da Micro:bit Educational Foundation;
    este site não é afiliado oficialmente a ela. Substitua os textos entre [colchetes] pelas informações da sua instituição.
  </div>
</footer>
<script src="{prefix}js/main.js"></script>
</body>
</html>
"""


def page(filename, title, desc, active, content, prefix=""):
    html = HEAD.format(title=title, desc=desc, nav=nav_html(active), prefix=prefix) + content + FOOTER.format(prefix=prefix)
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("gerado:", filename)


# ============================================================
# ÍNDICE (Início)
# ============================================================
modules_teaser_cards = "\n".join(
    '''      <a class="module-card" href="{slug}.html">
        <span class="tag">Módulo {n}</span>
        <h3>{title}</h3>
        <p style="color:var(--slate-soft); font-size:.92rem; margin:0;">{obj}</p>
        <span class="dur">{dur} · {formato}</span>
      </a>'''.format(
        slug=m["slug"], n=i + 1, title=m["short"], obj=m["objetivo"], dur=m["dur"], formato=m["formato"]
    )
    for i, m in enumerate(MODULES)
)

index_content = """
<section class="hero">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Formação online · 16 horas · 6 módulos</p>
      <h1>Robótica educacional na prática, com o BBC micro:bit</h1>
      <p class="lead">Um curso pensado para professores e educadores: programe, teste sensores e atuadores, e leve
      atividades interdisciplinares prontas para a sua sala de aula — sem precisar de experiência prévia em programação.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="cronograma.html">Ver cronograma</a>
        <a class="btn btn-outline" href="modulos.html">Conhecer os módulos</a>
      </div>
      <div class="hero-stats">
        <div class="hero-stat"><b>16h</b><span>Carga horária</span></div>
        <div class="hero-stat"><b>6</b><span>Módulos</span></div>
        <div class="hero-stat"><b>100%</b><span>Online</span></div>
      </div>
    </div>
    <div class="led-stage">
      <div class="led-grid size-lg" data-led-hero style="width:220px;"></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head center" style="margin-left:auto; margin-right:auto;">
      <p class="eyebrow" style="justify-content:center;">Por que este curso</p>
      <h2>Pensado para a rotina de quem ensina</h2>
    </div>
    <div class="cards-3">
      <div class="card">
        {icon1}
        <h3>Aprendizagem prática</h3>
        <p>Você programa um micro:bit real (ou o simulador online) desde o primeiro módulo — sem slides intermináveis antes da prática.</p>
      </div>
      <div class="card">
        {icon2}
        <h3>Foco pedagógico</h3>
        <p>Cada módulo termina em uma atividade prática pensada para ser adaptada e aplicada diretamente na sua turma.</p>
      </div>
      <div class="card">
        {icon3}
        <h3>Flexível para sua rotina</h3>
        <p>Encontros síncronos por videochamada + materiais sempre disponíveis para revisão no seu próprio ritmo.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Estrutura do curso</p>
      <h2>Os 6 módulos, em 16 horas</h2>
      <p>Cada módulo soma horas até completar a carga horária total — do primeiro contato com o micro:bit até o projeto final.</p>
    </div>
    <div class="modules-grid">
{cards}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="cta-banner">
      <div>
        <h3>Pronta(o) para começar?</h3>
        <p>Veja o cronograma completo ou fale com a coordenação para tirar dúvidas e se inscrever.</p>
      </div>
      <div style="display:flex; gap:12px; flex-wrap:wrap;">
        <a class="btn btn-primary" href="cronograma.html">Ver cronograma completo</a>
        <a class="btn btn-outline" style="border-color:rgba(255,255,255,.6);" href="contato.html">Fale com a coordenação</a>
      </div>
    </div>
  </div>
</section>
""".format(
    icon1=led_grid_html(MODULES[0]["icon"], "size-sm", on_light=True),
    icon2=led_grid_html(MODULES[4]["icon"], "size-sm", on_light=True),
    icon3=led_grid_html(MODULES[5]["icon"], "size-sm", on_light=True),
    cards=modules_teaser_cards,
)

page("index.html", "Início", "Curso online de robótica educacional com BBC micro:bit para professores. 16 horas, 6 módulos.", "home", index_content)

# ============================================================
# SOBRE O CURSO
# ============================================================
sobre_content = """
<section class="section">
  <div class="container">
    <p class="eyebrow">Sobre o curso</p>
    <h1>Robótica Educacional com BBC micro:bit</h1>
    <p style="max-width:68ch; font-size:1.05rem; color:var(--slate-soft);">
    Este curso foi desenhado para professores e educadores que desejam incorporar a robótica educacional à sua
    prática pedagógica, utilizando o BBC micro:bit como ferramenta principal. Ao longo de 16 horas, distribuídas
    em 6 módulos, você vai programar, testar sensores e atuadores, e planejar atividades interdisciplinares
    prontas para aplicar em sala de aula.</p>

    <h2 style="margin-top:2em;">Ficha do curso</h2>
    <table class="kv">
      <tr><th>Nome do curso</th><td>Robótica Educacional com BBC micro:bit</td></tr>
      <tr><th>Público-alvo</th><td>Professores e educadores da Educação Básica</td></tr>
      <tr><th>Carga horária</th><td>16 horas, distribuídas em 6 módulos</td></tr>
      <tr><th>Modalidade</th><td>Online (EAD) — encontros síncronos via videochamada + atividades assíncronas</td></tr>
      <tr><th>Pré-requisitos</th><td>Computador com acesso à internet; kit BBC micro:bit (pode ser usado o simulador online caso o kit ainda não esteja disponível)</td></tr>
      <tr><th>Certificação</th><td>Certificado de 16h mediante entrega do projeto final (Módulo 6)</td></tr>
    </table>

    <h2 style="margin-top:2em;">Objetivos de aprendizagem</h2>
    <ul class="check-list">
      <li>Compreender os fundamentos da robótica educacional</li>
      <li>Programar o BBC micro:bit utilizando o editor MakeCode</li>
      <li>Utilizar sensores e atuadores em atividades práticas</li>
      <li>Planejar aulas interdisciplinares com apoio da robótica</li>
      <li>Desenvolver e apresentar um projeto final aplicável à sua realidade escolar</li>
    </ul>

    <div class="cta-banner" style="margin-top:2.4em;">
      <div>
        <h3>Quer ver a divisão de horas?</h3>
        <p>Confira o cronograma completo dos 6 módulos.</p>
      </div>
      <a class="btn btn-primary" href="cronograma.html">Ver cronograma</a>
    </div>
  </div>
</section>
"""
page("sobre.html", "Sobre o Curso", "Ficha completa do curso de robótica educacional com BBC micro:bit: público, carga horária, modalidade e objetivos.", "sobre", sobre_content)

# ============================================================
# CRONOGRAMA
# ============================================================
rows = "\n".join(
    '''      <tr>
        <td class="num">{n:02d}</td>
        <td><a href="{slug}.html">{title}</a></td>
        <td class="num">{dur}</td>
        <td>{formato}</td>
      </tr>'''.format(n=i + 1, slug=m["slug"], title=m["title"], dur=m["dur"], formato=m["formato"])
    for i, m in enumerate(MODULES)
)

cronograma_content = """
<section class="section">
  <div class="container">
    <p class="eyebrow">Cronograma</p>
    <h1>16 horas, distribuídas em 6 módulos</h1>
    <p style="max-width:68ch; color:var(--slate-soft);">O curso é organizado em 6 módulos. Os encontros síncronos
    ocorrem por videochamada, e cada módulo inclui materiais de apoio para consulta a qualquer momento.</p>

    <div class="table-wrap" style="margin-top:1.6em;">
      <table class="schedule">
        <thead>
          <tr><th>Módulo</th><th>Título</th><th>Carga horária</th><th>Formato</th></tr>
        </thead>
        <tbody>
{rows}
          <tr class="total">
            <td colspan="2">Total</td>
            <td class="num">16h</td>
            <td></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="info-box" style="margin-top:1.8em;">
      <strong>Dica de planejamento:</strong> distribua os módulos em 3 a 6 encontros, conforme a disponibilidade
      da turma — por exemplo, um encontro de 2 a 3 horas por semana ao longo de um mês.
    </div>
  </div>
</section>
""".format(rows=rows)
page("cronograma.html", "Cronograma", "Cronograma completo do curso: 6 módulos somando 16 horas, com formato de cada encontro.", "cronograma", cronograma_content)

# ============================================================
# MÓDULOS (hub)
# ============================================================
hub_cards = "\n".join(
    '''      <a class="module-card" href="{slug}.html">
        {icon}
        <span class="tag">Módulo {n} · {dur}</span>
        <h3>{title}</h3>
        <p style="color:var(--slate-soft); font-size:.92rem; margin:0;">{obj}</p>
      </a>'''.format(
        slug=m["slug"], n=i + 1, dur=m["dur"], title=m["title"], obj=m["objetivo"],
        icon=led_grid_html(m["icon"], "size-sm", on_light=True),
    )
    for i, m in enumerate(MODULES)
)

modulos_content = """
<section class="section">
  <div class="container">
    <p class="eyebrow">Módulos do curso</p>
    <h1>Do primeiro contato ao projeto final</h1>
    <p style="max-width:68ch; color:var(--slate-soft);">Cada módulo combina um objetivo claro, os tópicos abordados
    e uma atividade prática para aplicar imediatamente. Clique em um módulo para ver o conteúdo completo.</p>
    <div class="modules-grid" style="margin-top:1.8em;">
{cards}
    </div>
  </div>
</section>
""".format(cards=hub_cards)
page("modulos.html", "Módulos", "Visão geral dos 6 módulos do curso de robótica educacional com BBC micro:bit.", "modulos", modulos_content)

# ============================================================
# PÁGINAS DE CADA MÓDULO
# ============================================================
for i, m in enumerate(MODULES):
    prev_m = MODULES[i - 1] if i > 0 else None
    next_m = MODULES[i + 1] if i < len(MODULES) - 1 else None

    topics_html = "\n".join('      <li>{t}</li>'.format(t=t) for t in m["topicos"])

    if prev_m:
        prev_html = '<a href="{slug}.html"><span class="lbl">← Anterior</span>{short}</a>'.format(slug=prev_m["slug"], short=prev_m["short"])
    else:
        prev_html = '<a href="modulos.html"><span class="lbl">← Voltar</span>Todos os módulos</a>'
    if next_m:
        next_html = '<a href="{slug}.html" style="text-align:right;"><span class="lbl">Próximo →</span>{short}</a>'.format(slug=next_m["slug"], short=next_m["short"])
    else:
        next_html = '<a href="avaliacao.html" style="text-align:right;"><span class="lbl">Avançar →</span>Avaliação e Certificação</a>'

    module_content = """
<section class="section">
  <div class="container">
    <div class="module-hero">
      <div style="background:var(--ink); border-radius:var(--radius); padding:18px;">
        {icon}
      </div>
      <div>
        <p class="eyebrow">Módulo {n} de 6</p>
        <h1>{title}</h1>
        <div class="module-meta">
          <span class="pill">{dur}</span>
          <span class="pill">{formato}</span>
        </div>
      </div>
    </div>

    <h2 style="margin-top:2.2em;">Objetivo</h2>
    <p style="max-width:68ch;">{objetivo}</p>

    <h2 style="margin-top:1.6em;">Tópicos abordados</h2>
    <ul class="topic-list">
{topics}
    </ul>

    <div class="activity-box">
      <p class="eyebrow">Atividade prática</p>
      <p style="margin:0; color:var(--paper);">{atividade}</p>
    </div>

    <div class="module-pager">
      {prev}
      {next}
    </div>
  </div>
</section>
""".format(
        icon=led_grid_html(m["icon"], "size-md"),
        n=i + 1,
        title=m["title"],
        dur=m["dur"],
        formato=m["formato"],
        objetivo=m["objetivo"],
        topics=topics_html,
        atividade=m["atividade"],
        prev=prev_html,
        next=next_html,
    )
    page(
        "{}.html".format(m["slug"]),
        m["short"],
        "Módulo {n} do curso de robótica educacional: {title}.".format(n=i + 1, title=m["title"]),
        "modulos",
        module_content,
    )

# ============================================================
# MATERIAIS E RECURSOS
# ============================================================
materiais_content = """
<section class="section">
  <div class="container">
    <p class="eyebrow">Materiais e recursos</p>
    <h1>Tudo o que você precisa, em um só lugar</h1>
    <p style="max-width:68ch; color:var(--slate-soft);">Links, simuladores e arquivos de apoio para acompanhar
    o curso e revisar o conteúdo no seu próprio ritmo.</p>

    <ul class="check-list" style="margin-top:1.6em; max-width:68ch;">
      <li>Apostila e slides de cada módulo (substitua pelo link da pasta no seu Google Drive)</li>
      <li>Editor oficial MakeCode: <a href="https://makecode.microbit.org" target="_blank" rel="noopener">makecode.microbit.org</a></li>
      <li>Simulador online do micro:bit, para quem ainda não recebeu o kit físico</li>
      <li>Gravações dos encontros síncronos (incorpore o vídeo do Google Drive ou YouTube)</li>
      <li>Glossário de termos técnicos da robótica educacional</li>
    </ul>

    <h2 style="margin-top:2em;">Como incorporar seus arquivos aqui</h2>
    <div class="embed-placeholder">
      <p style="margin:0;"><strong>Substitua este bloco</strong> por um arquivo do Google Drive, uma apresentação
      de slides ou um vídeo do YouTube. No HTML, use uma tag <code>&lt;iframe&gt;</code> com o link de incorporação
      do arquivo (em "Compartilhar → Incorporar item" no Drive).</p>
    </div>
    <!--
    Exemplo de incorporação de uma pasta do Google Drive:
    <iframe class="embed-frame" src="LINK_DE_INCORPORACAO_DO_DRIVE" allow="autoplay"></iframe>
    -->
  </div>
</section>
"""
page("materiais.html", "Materiais e Recursos", "Links, simulador e materiais de apoio do curso de robótica educacional com BBC micro:bit.", "materiais", materiais_content)

# ============================================================
# AVALIAÇÃO E CERTIFICAÇÃO
# ============================================================
avaliacao_content = """
<section class="section">
  <div class="container">
    <p class="eyebrow">Avaliação e certificação</p>
    <h1>Como funciona a certificação</h1>
    <p style="max-width:68ch; color:var(--slate-soft);">O certificado de 16 horas é emitido a partir de critérios
    simples de participação e entrega — pensados para uma rotina de formação realista.</p>

    <ul class="check-list" style="margin-top:1.6em; max-width:68ch;">
      <li>Participação nos encontros síncronos (mínimo de 75% de presença)</li>
      <li>Entrega das atividades práticas de cada módulo</li>
      <li>Apresentação do projeto final no Módulo 6</li>
    </ul>

    <h2 style="margin-top:2em;">Pesquisa de satisfação</h2>
    <div class="embed-placeholder">
      <p style="margin:0;"><strong>Substitua este bloco</strong> pelo seu formulário do Google Forms de avaliação
      final do curso. Em "Enviar → Incorporar (&lt;&gt;)" no Forms, copie o código e cole no lugar deste aviso.</p>
    </div>
    <!--
    Exemplo de incorporação de um Google Forms:
    <iframe class="embed-frame" src="LINK_DE_INCORPORACAO_DO_FORMS" allow="autoplay"></iframe>
    -->
  </div>
</section>
"""
page("avaliacao.html", "Avaliação e Certificação", "Critérios de avaliação e certificação do curso de robótica educacional com BBC micro:bit.", "avaliacao", avaliacao_content)

# ============================================================
# CONTATO
# ============================================================
contato_content = """
<section class="section">
  <div class="container">
    <p class="eyebrow">Contato e suporte</p>
    <h1>Fale com a coordenação do curso</h1>
    <p style="max-width:68ch; color:var(--slate-soft);">Dúvidas sobre o curso, conteúdos ou questões técnicas?
    Use um dos canais abaixo.</p>

    <table class="kv" style="margin-top:1.4em; max-width:68ch;">
      <tr><th>E-mail</th><td><a href="mailto:contato@seudominio.org">contato@seudominio.org</a></td></tr>
      <tr><th>Grupo de apoio</th><td><a href="#">[inserir link do grupo/turma]</a></td></tr>
      <tr><th>Responsável</th><td>[Nome do formador ou da coordenação]</td></tr>
    </table>

    <div style="margin-top:2em;">
      <a class="btn btn-ghost" href="mailto:contato@seudominio.org">Enviar e-mail</a>
    </div>
  </div>
</section>
"""
page("contato.html", "Contato", "Canais de contato e suporte do curso de robótica educacional com BBC micro:bit.", "contato", contato_content)

print("\\nTodas as páginas foram geradas em:", ROOT)
