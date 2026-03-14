# Come pubblicare il sito su GitHub Pages / How to deploy to GitHub Pages

## Prerequisiti / Prerequisites

- Il repository deve essere su GitHub (pubblico o privato con GitHub Pro)
- Il file `index.html` deve essere nella root del repository (il build script lo genera automaticamente)

## Passo 1: Push del codice su GitHub / Step 1: Push code to GitHub

Se non e gia stato fatto, fare push del branch `main`:

```bash
git push origin main
```

## Passo 2: Abilitare GitHub Pages / Step 2: Enable GitHub Pages

1. Aprire il repository su **github.com**
2. Cliccare su **Settings** (icona ingranaggio, nella barra in alto del repository)
3. Nel menu laterale sinistro, sotto "Code and automation", cliccare su **Pages**
4. Nella sezione **"Build and deployment"**:
   - **Source**: selezionare **"Deploy from a branch"**
   - **Branch**: selezionare **`main`** e **`/ (root)`**
5. Cliccare **Save**

## Passo 3: Attendere il deploy / Step 3: Wait for deployment

- GitHub impieghera 1-2 minuti per pubblicare il sito
- Nella stessa pagina Settings > Pages apparira l'URL del sito, che sara:
  - `https://<username>.github.io/<nome-repository>/`
  - Ad esempio: `https://enricopicci.github.io/festa-63-63/`
- Si puo verificare lo stato del deploy nella tab **Actions** del repository

## Passo 4: Verificare / Step 4: Verify

Aprire l'URL nel browser e verificare che il sito funzioni correttamente:
- Il toggle IT/EN funziona
- Le immagini si caricano
- Lo spettro politico si anima
- La mappa si visualizza
- La gallery con lightbox funziona

## Aggiornamenti successivi / Subsequent updates

Ogni volta che si fa push su `main`, GitHub Pages ri-pubblica automaticamente il sito. Non serve fare nulla di speciale.

Il flusso e:
1. Modificare un file in `content/` (o aggiungere foto in `pictures/`)
2. Commit e push (il pre-commit hook rigenera `index.html`)
3. La GitHub Action ri-esegue build e test
4. GitHub Pages pubblica la nuova versione
5. Il sito si aggiorna in 1-2 minuti

## Dominio personalizzato (opzionale) / Custom domain (optional)

Se si vuole usare un dominio personalizzato (es. `www.festa63-63.it`):

1. Acquistare il dominio da un registrar (es. Aruba, GoDaddy, Namecheap)
2. In Settings > Pages, nella sezione **"Custom domain"**, inserire il dominio (es. `www.festa63-63.it`)
3. Cliccare **Save**
4. Configurare il DNS presso il registrar:
   - Per un dominio `www`: aggiungere un record **CNAME** che punta a `<username>.github.io`
   - Per un dominio apex (senza www): aggiungere 4 record **A** che puntano agli IP di GitHub Pages:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
5. Abilitare **"Enforce HTTPS"** nella pagina Settings > Pages (disponibile dopo la propagazione DNS, puo richiedere fino a 24 ore)

## Risoluzione problemi / Troubleshooting

| Problema | Soluzione |
|----------|----------|
| Il sito mostra un 404 | Verificare che `index.html` esista nella root del branch `main` |
| Le immagini non si caricano | Verificare che i percorsi siano relativi (es. `pictures/...` e non `/pictures/...`) |
| Il sito non si aggiorna | Controllare la tab Actions per errori nel workflow. Provare a fare un push vuoto: `git commit --allow-empty -m "trigger deploy" && git push` |
| Il CSS/JS non si carica | Svuotare la cache del browser (Ctrl+Shift+R) |
| Errore "Your site is having problems building" | Controllare la tab Actions per i dettagli dell'errore |
