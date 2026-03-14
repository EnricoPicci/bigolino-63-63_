# Proposta v3 per il sito web "63-63" / Website Proposal v3

Questo documento aggiorna la proposta v2 (`02-website-proposal-v2.md`), integrando le decisioni prese e rispondendo alla domanda sull'isolamento dei testi.

---

## Architettura dei contenuti: testi isolati in file separati

La risposta alla domanda e: **si, ed e l'approccio consigliato**. I testi del sito saranno in file Markdown con nomi chiari, organizzati per sezione e lingua. Un build script (eseguito automaticamente prima di ogni commit) generera il file `index.html` finale a partire da un template e dai file di contenuto.

### Struttura della cartella `content/`

```
content/
├── it/                          # Contenuti in italiano
│   ├── hero.md                  # Titolo, sottotitolo, data
│   ├── storia.md                # La storia dell'amicizia e la timeline
│   ├── giovanni.md              # Profilo di Giovanni
│   ├── enrico.md                # Profilo di Enrico
│   ├── stefano.md               # Profilo di Stefano
│   ├── gigio.md                 # Profilo di Gigio
│   ├── spettro-politico.md      # Testi dello spettro politico
│   ├── luogo.md                 # Descrizione del luogo e info pratiche
│   ├── dove-dormire.md          # Opzioni di alloggio
│   └── footer.md                # Testi del footer
│
└── en/                          # English content
    ├── hero.md
    ├── story.md
    ├── giovanni.md
    ├── enrico.md
    ├── stefano.md
    ├── gigio.md
    ├── political-spectrum.md
    ├── venue.md
    ├── where-to-stay.md
    └── footer.md
```

### Come funziona in pratica

**Per modificare il profilo di Giovanni in italiano**, si apre `content/it/giovanni.md` e si trova qualcosa come:

```markdown
# Giovanni Della Frattina

## Il Filosofo con la Penna a Destra

Laureato in Filosofia Teoretica con lode all'Universita di Padova, poi
specializzato in Comunicazioni Sociali alla Cattolica di Milano. Capo
della redazione milanese de *Il Giornale*...
```

Si modifica il testo, si fa commit e push. Il precommit hook:
1. Esegue il build script che rigenera `index.html` dai contenuti aggiornati
2. Aggiorna la lista immagini dalla cartella `pictures/`
3. Aggiunge automaticamente al commit il file `index.html` rigenerato
4. Esegue i test per verificare che tutto sia a posto
5. Se i test passano, il commit va a buon fine

**I quattro amici non toccano mai `index.html`, `style.css` o `main.js`**. Modificano solo i file `.md` nella cartella `content/`.

### Il build script

Un singolo script (Python o Node.js) che:
1. Legge il file template (`template.html`) che contiene la struttura HTML e i segnaposto
2. Legge ogni file `.md` dalla cartella `content/`
3. Converte il Markdown in HTML
4. Inserisce i contenuti al posto dei segnaposto nel template
5. Scansiona la cartella `pictures/` e genera la lista delle immagini per la gallery
6. Produce il file `index.html` finale

**Dipendenze**: una sola libreria per il parsing Markdown (ad esempio `markdown-it` per Node o `markdown` per Python). Nient'altro.

---

## Struttura del sito (confermata con aggiornamenti)

### 1. Hero - "63-63"
- Numero "63-63", sfondo colline del Prosecco
- **27 Giugno 2026 - dalle ore 19:00**
- Toggle IT/EN

### 2. La Storia / The Story
- Il racconto dell'amicizia dal Liceo Tito Livio
- Timeline: 2003 (40 anni) → 2013 (50) → 2023 (60, "59+1 azzomene!") → 2026 (63-63)

### 3. I Fantastici Quattro / The Fab Four
Profili con descrizioni ironiche e basate su fatti reali (come nella proposta v2).

### 4. Lo Spettro Politico / The Political Spectrum
Barra interattiva: Stefano a sinistra, Giovanni a destra, Enrico e Gigio al centro. Cursore animato con la scritta *"Dopo il terzo bicchiere, convergono tutti al centro"*.

### 5. Il Luogo / The Place
- Agriturismo da Ottavio, Via Campion 1, Valdobbiadene
- Mappa embedded, descrizione evocativa, data e ora
- Gallery fotografica

### 6. Dove Dormire / Where to Stay
Opzioni di alloggio con commenti ironici **che non menzionano i 4 amici**:

| Nome | Tipo | Distanza | Prezzo indicativo | Commento |
|------|------|----------|-------------------|----------|
| Casa de Eli | B&B | ~2 min | Budget-medio | *"Cosi vicino che sentirai brindare"* |
| Hotel Diana | Hotel | ~5 min | 65-115 EUR | *"Classico e affidabile, come il Prosecco"* |
| Vigneto Vecio | Agriturismo | ~10 min | da ~63 EUR | *"63 euro per 63 anni: coincidenza?"* |
| Agriturismo Vedova | Agriturismo | ~5-10 min | ~90-130 EUR | *"Voto 9.3 su Booking: piu del nostro vino"* |
| Locanda Sandi | Locanda | ~5-10 min | 70-120 EUR | *"Dormire in una tenuta vinicola: la coerenza"* |
| Due Carpini | Agriturismo+Spa | ~10-12 min | ~120-200 EUR | *"Per chi dopo il Prosecco vuole anche la spa"* |
| Municipio 1815 | Boutique Hotel | ~10-15 min | da ~210 EUR | *"Vista sulle vigne fino a Venezia"* |
| Villa Soligo | Hotel di lusso | ~12-15 min | 150-300+ EUR | *"Per chi il Prosecco lo beve nel flute di cristallo"* |

### 7. Footer
- Badge: *"Powered by Daniela and Dario Amodei"*
- *"Anche l'AI beve Prosecco"*

---

## Scelte tecniche (aggiornate)

### HTML/CSS/JS vanilla, nessun framework
Confermato. Nessun framework, nessun Tailwind.

### Hosting: GitHub Pages
Confermato. Il sito viene servito direttamente dal repository GitHub. Deploy automatico ad ogni push su `main`.

### Form RSVP (futuro)
Con GitHub Pages non c'e supporto nativo per form. Quando servira, si potra usare:
- **Formspree** (gratuito fino a 50 invii/mese) - basta aggiungere un `action` al form HTML
- **Google Forms** embedded
- **Tally** (gratuito, illimitato)

Nessuna di queste opzioni richiede di modificare l'architettura del sito.

### Precommit hook
Un **git precommit hook** che esegue automaticamente, ad ogni commit:

1. **Build**: genera `index.html` dai contenuti Markdown + template + lista immagini
2. **Stage**: aggiunge `index.html` aggiornato al commit
3. **Test**: verifica la correttezza del sito generato
4. Se i test falliscono, il commit viene bloccato

Lo hook verra installato automaticamente con uno script `setup.sh` (da lanciare una sola volta dopo il clone del repository).

### Test (precommit)
I test verificano:
- Che tutte le sezioni richieste siano presenti nell'HTML generato
- Che ogni sezione abbia contenuto sia in italiano che in inglese
- Che tutte le immagini referenziate nella gallery esistano nella cartella `pictures/`
- Che i link esterni siano formati correttamente
- Che la struttura HTML sia valida

### Gestione immagini (precommit)
Il build script scansiona automaticamente la cartella `pictures/` e genera la lista delle immagini per la gallery. Per aggiungere una foto:
1. Mettere il file nella cartella `pictures/`
2. Fare commit e push

Nessun altro passaggio. Il precommit hook si occupa di tutto.

---

## Struttura dei file completa

```
festa-63-63/
│
├── index.html                     # GENERATO dal build script (non modificare a mano)
│
├── template.html                  # Template HTML con segnaposto per i contenuti
├── css/
│   └── style.css                  # Stili del sito
├── js/
│   └── main.js                    # Toggle lingua, spettro politico, gallery
│
├── content/                       # CONTENUTI DA MODIFICARE
│   ├── it/                        # Testi in italiano (file .md)
│   │   ├── hero.md
│   │   ├── storia.md
│   │   ├── giovanni.md
│   │   ├── enrico.md
│   │   ├── stefano.md
│   │   ├── gigio.md
│   │   ├── spettro-politico.md
│   │   ├── luogo.md
│   │   ├── dove-dormire.md
│   │   └── footer.md
│   └── en/                        # English texts (.md files)
│       ├── hero.md
│       ├── story.md
│       ├── giovanni.md
│       ├── enrico.md
│       ├── stefano.md
│       ├── gigio.md
│       ├── political-spectrum.md
│       ├── venue.md
│       ├── where-to-stay.md
│       └── footer.md
│
├── pictures/                      # Foto (basta aggiungere file qui)
│   └── fotobigolino2023/          # Foto festa 2023
│
├── scripts/
│   ├── build.py                   # Build script (genera index.html)
│   ├── test.py                    # Test del sito generato
│   └── setup.sh                   # Installa il precommit hook
│
├── prompts-to-generate-app/       # Prompt usati per generare il sito
│   └── 01-site_description.md
├── claude-output/                 # Documenti generati da Claude
│   ├── 02-website-proposal.md
│   ├── 03-website-proposal-v2.md
│   └── 04-website-proposal-v3.md
│
├── COME-MODIFICARE-IL-SITO.md     # Guida per modificare i contenuti (IT)
├── HOW-TO-EDIT-THE-SITE.md        # Guide to editing content (EN)
└── README.md
```

---

## Flusso di lavoro per i quattro amici

### Modificare un testo
1. Aprire il repository su GitHub.com
2. Navigare nella cartella `content/it/` (o `content/en/`)
3. Cliccare sul file da modificare (es. `giovanni.md`)
4. Cliccare l'icona matita (Edit)
5. Modificare il testo
6. Cliccare "Commit changes"
7. Il sito si aggiorna automaticamente in pochi minuti

**Nota**: modificando via GitHub web interface, il precommit hook **non** viene eseguito (gli hook girano solo in locale). Per gestire questo caso, si configurera una **GitHub Action** che esegue lo stesso build + test ad ogni push, e committa il file `index.html` rigenerato se necessario.

### Aggiungere una foto
1. Aprire il repository su GitHub.com
2. Navigare nella cartella `pictures/`
3. Cliccare "Add file" → "Upload files"
4. Trascinare le foto
5. Cliccare "Commit changes"
6. La GitHub Action rigenera il sito con le nuove foto

### Flusso alternativo (locale)
Per chi preferisce lavorare in locale:
1. `git pull`
2. Modificare i file in `content/` o aggiungere foto in `pictures/`
3. `git add . && git commit -m "aggiornato testo di Giovanni"`
4. Il precommit hook rigenera `index.html`, esegue i test, e se tutto e ok il commit va a buon fine
5. `git push`

---

## Prossimi passi

1. **Approvare questa proposta**
2. **Sviluppare il sito**: template HTML, CSS, JS, build script, test, precommit hook, GitHub Action
3. **Scrivere i contenuti**: i file `.md` per tutte le sezioni in entrambe le lingue
4. **Configurare GitHub Pages**: abilitare il deploy dal branch `main`
5. **Scrivere la guida**: `COME-MODIFICARE-IL-SITO.md`
6. **Raccogliere foto**: individuali dei 4 amici, del territorio
