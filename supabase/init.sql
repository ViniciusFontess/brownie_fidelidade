-- Cria tabela purchases
create extension if not exists pgcrypto;

create table if not exists purchases (
  id uuid primary key default gen_random_uuid(),
  cpf text not null,
  quantity integer not null check (quantity > 0),
  created_at timestamptz default now()
);

-- Habilitar Row Level Security
alter table purchases enable row level security;

-- Política de insert anônimo (aceita apenas linhas válidas)
create policy anon_insert_purchases on purchases
  for insert
  with check (cpf is not null and quantity > 0);

-- (Opcional) bloquear selects de anônimos; permita apenas inserts anônimos
-- Se desejar que apenas usuários autenticados vejam os dados, use a policy abaixo:
-- create policy auth_select on purchases
--   for select using (auth.role() = 'authenticated');
