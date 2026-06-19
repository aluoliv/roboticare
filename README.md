# Robótica Educacional com BBC micro:bit — Site do Curso

Site estático (HTML/CSS/JS puro, sem build tools) para o curso de robótica
educacional com BBC micro:bit — formação online de 16h para professores,
em 6 módulos.

## Estrutura

```
index.html          → Início
sobre.html           → Sobre o Curso
cronograma.html       → Cronograma (16h / 6 módulos)
modulos.html          → Hub com os 6 módulos
modulo-1.html ... modulo-6.html → Conteúdo de cada módulo
materiais.html        → Materiais e Recursos
avaliacao.html        → Avaliação e Certificação
contato.html          → Contato e Suporte
404.html              → Página de erro personalizada
css/style.css         → Estilos (tokens de cor, tipografia, componentes)
js/main.js            → Menu mobile, submenu "Módulos" e animação do hero
build/build.py        → Script Python que gera todas as páginas .html
                         a partir de um template comum (não precisa rodar
                         de novo — só use se quiser editar via código)
```

## Publicar no GitHub Pages

**Opção A — pelo site do GitHub (sem usar terminal)**

1. Crie uma conta em [github.com](https://github.com) (se ainda não tiver).
2. Clique em **New repository**, dê um nome (ex.: `curso-robotica-microbit`)
   e marque como **Public**. Não marque "Add a README".
3. Na página do repositório recém-criado, clique em **uploading an existing
   file** e arraste todos os arquivos e pastas deste projeto (mantendo as
   pastas `css/` e `js/`). Clique em **Commit changes**.
4. Vá em **Settings → Pages** (menu lateral).
5. Em **Build and deployment → Source**, selecione **Deploy from a branch**.
6. Em **Branch**, selecione `main` e a pasta `/ (root)`. Clique em **Save**.
7. Aguarde 1–2 minutos e atualize a página. O endereço do site aparecerá no
   topo, algo como:
   `https://SEU-USUARIO.github.io/curso-robotica-microbit/`

**Opção B — pelo terminal (git)**

```bash
cd pasta-do-site
git init
git add .
git commit -m "Site do curso de robótica educacional"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/curso-robotica-microbit.git
git push -u origin main
```

Depois, repita os passos 4 a 7 da Opção A.

## O que personalizar antes de publicar

- **E-mail e grupo de apoio**: em `contato.html` e no rodapé de todas as
  páginas, troque `contato@seudominio.org` e `[inserir link do grupo/turma]`.
- **Materiais (Drive)**: em `materiais.html`, troque o bloco
  `embed-placeholder` por um `<iframe>` com o link de incorporação dos seus
  arquivos do Google Drive (veja o comentário no código-fonte).
- **Formulário de avaliação (Forms)**: em `avaliacao.html`, troque o bloco
  `embed-placeholder` por um `<iframe>` com o link de incorporação do seu
  Google Forms.
- **Nome da instituição/formador**: ajuste o rodapé (presente em todas as
  páginas) e a tabela em `contato.html`.

## Pré-visualizar localmente antes de publicar

Não é obrigatório, mas se quiser ver o site no navegador antes de subir
para o GitHub, rode (com Python instalado):

```bash
cd pasta-do-site
python3 -m http.server 8000
```

E acesse `http://localhost:8000` no navegador.

## Domínio próprio (opcional)

Em **Settings → Pages → Custom domain**, você pode apontar um domínio
próprio (ex. `curso.suaescola.com.br`) seguindo as instruções do GitHub
para configurar o DNS.
