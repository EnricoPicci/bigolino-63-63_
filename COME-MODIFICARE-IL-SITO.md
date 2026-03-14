# Come modificare il sito 63-63

## Dove si trovano i testi

Tutti i testi del sito sono nella cartella `content/`. Ci sono due sottocartelle:
- `content/it/` - Testi in italiano
- `content/en/` - Testi in inglese

Ogni sezione del sito ha il suo file:

| File (IT) | File (EN) | Sezione |
|-----------|-----------|---------|
| `hero.md` | `hero.md` | Titolo e data dell'evento |
| `storia.md` | `story.md` | La storia dell'amicizia |
| `giovanni.md` | `giovanni.md` | Profilo di Giovanni |
| `enrico.md` | `enrico.md` | Profilo di Enrico |
| `stefano.md` | `stefano.md` | Profilo di Stefano |
| `gigio.md` | `gigio.md` | Profilo di Gigio |
| `spettro-politico.md` | `political-spectrum.md` | Lo spettro politico |
| `luogo.md` | `venue.md` | Il luogo e come arrivare |
| `dove-dormire.md` | `where-to-stay.md` | Dove dormire |
| `footer.md` | `footer.md` | Testo del footer |

I file sono in formato **Markdown**, un formato di testo semplice:
- `# Titolo` = titolo grande
- `## Sottotitolo` = sottotitolo
- `**grassetto**` = **grassetto**
- `*corsivo*` = *corsivo*
- `- elemento` = lista puntata

## Come modificare un testo (da GitHub.com)

1. Vai su [github.com](https://github.com) e apri il repository del progetto
2. Naviga nella cartella `content/it/` (o `content/en/` per l'inglese)
3. Clicca sul file che vuoi modificare (es. `giovanni.md`)
4. Clicca l'icona **matita** (Edit this file) in alto a destra
5. Modifica il testo
6. Clicca il pulsante verde **"Commit changes..."**
7. Nella finestra che appare, scrivi una breve descrizione della modifica
8. Clicca **"Commit changes"**
9. Aspetta qualche minuto: una GitHub Action ricostruira automaticamente il sito

**Importante**: ricorda di modificare sia il file italiano che quello inglese!

## Come aggiungere una foto

1. Vai su GitHub.com e apri il repository
2. Naviga nella cartella `pictures/`
3. Clicca **"Add file"** -> **"Upload files"**
4. Trascina le foto che vuoi aggiungere
5. Clicca **"Commit changes"**
6. La foto apparira automaticamente nella galleria del sito

## Come modificare in locale (per chi usa git)

1. `git pull` (per scaricare le ultime modifiche)
2. Modifica i file nella cartella `content/` con un qualsiasi editor di testo
3. Per aggiungere foto, copiale nella cartella `pictures/`
4. `git add .`
5. `git commit -m "descrizione della modifica"`
   - Il pre-commit hook ricostruira il sito e fara i test automaticamente
   - Se i test falliscono, il commit viene bloccato e vedrai un messaggio di errore
6. `git push`

## Setup iniziale (solo la prima volta, per chi lavora in locale)

```bash
bash scripts/setup.sh
```

Questo comando installa il pre-commit hook e verifica che tutto funzioni.

## Cosa NON modificare

- `index.html` - Viene generato automaticamente. Le modifiche manuali verranno sovrascritte.
- `template.html` - La struttura HTML. Modificare solo se si sa cosa si sta facendo.
- `css/style.css` - Gli stili. Modificare solo se si vuole cambiare l'aspetto grafico.
- `js/main.js` - Il codice JavaScript. Non toccare.
- `scripts/` - Gli script di build e test. Non toccare.
