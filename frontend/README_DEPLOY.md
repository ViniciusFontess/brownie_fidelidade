Deploy rápido com Supabase + Vercel / GitHub Pages

Passos resumidos:

1) Criar projeto Supabase
   - Acesse https://app.supabase.com e crie um projeto gratuito.
   - Guarde o URL do projeto (p.ex. https://abcdxyz.supabase.co) e a chave ANON (Settings -> API -> anon key).

2) Criar tabela e políticas
   - No Supabase, abra SQL Editor e rode o script `../supabase/init.sql` (copie o conteúdo deste arquivo) para criar a tabela `purchases` e habilitar RLS.
   - Se quiser que o admin consulte dados, ajuste as policies: por exemplo permita SELECT apenas para `authenticated`.

3) Atualizar as chaves no frontend
   - Abra `frontend/index.html` e `frontend/admin.html` e substitua:
     - `REPLACE_WITH_SUPABASE_URL` pelo URL do seu projeto (ex: https://abcdxyz.supabase.co)
     - `REPLACE_WITH_SUPABASE_ANON_KEY` pela ANON public key do seu projeto

   NOTA: Para deploy no Vercel você pode usar Environment Variables em vez de editar o arquivo diretamente. Se for usar Github Pages (sem variáveis de ambiente), será preciso inserir a ANON KEY no arquivo (atenção: ficará publicamente visível).

4) Teste localmente
   - Abra `frontend/index.html` no navegador (ou use um servidor estático: `python3 -m http.server` na pasta `frontend/`) e teste o formulário. As inserções aparecerão na tabela `purchases` (verifique no Supabase Studio -> Table Editor).

5) Deploy no Vercel (recomendado)
   - Crie uma conta em https://vercel.com e faça o import do repositório.
   - Em Settings > Environment Variables, adicione:
     - SUPABASE_URL = seu URL
     - SUPABASE_ANON_KEY = sua anon key
   - Antes do deploy, ajuste `frontend/index.html` para ler dessas variáveis no build (p.ex. usando um pequeno script de build) ou simplesmente substituir as chaves manualmente.

6) Deploy no GitHub Pages (alternativa)
   - Coloque o conteúdo da pasta `frontend/` na branch `gh-pages` ou em `docs/` e ative GitHub Pages.
   - Se usar GitHub Pages, você provavelmente terá que colocar as chaves diretamente nos arquivos (menos seguro).

Recomendações de segurança
 - Use RLS no Supabase para controlar quem pode ler os dados.
 - Para o painel Admin, prefira usar Supabase Auth (somente usuários autenticados podem ver selects). A chave ANON é desenhada para uso em frontends, mas com políticas RLS bem definidas.

Se quiser, eu posso:
 - substituir os placeholders automaticamente por variáveis de ambiente no momento do build (config para Vercel), ou
 - gerar um pequeno script de build que injeta as variáveis em `index.html` e `admin.html` para GitHub Pages.
