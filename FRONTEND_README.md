Frontend (Fidelidade) — deploy automático

O repositório contém a pasta `frontend/` com os arquivos estáticos (index.html, admin.html, styles.css).

Configuração automática
- Adicione este repositório ao GitHub como `brownie_fidelidade`.
- O workflow `.github/workflows/deploy.yml` publica automaticamente o conteúdo de `frontend/` para o GitHub Pages sempre que houver push na branch `main`.

Como finalizar (no seu terminal, a partir de ~/brownie_fidelidade):

1. Crie o repositório no GitHub (ex: `vinicius/brownie_fidelidade`).
2. Configure o remoto e empurre:
   ```bash
   cd ~/brownie_fidelidade
   git remote add origin git@github.com:SEU_USUARIO/brownie_fidelidade.git
   git branch -M main
   git push -u origin main
   ```
3. Vá nas Settings do repositório -> Pages e confirme que a ação de GitHub Pages está ativa (o workflow preencherá a pasta). O site ficará em `https://SEU_USUARIO.github.io/brownie_fidelidade/`.

Se preferir, use Vercel (mais simples de integrar). Posso gerar instruções para Vercel se quiser.
