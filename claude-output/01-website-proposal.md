# Proposta per il sito web "63-63" / Website Proposal for "63-63"

## Panoramica / Overview

Un sito web single-page, bilingue (italiano/inglese), mobile-first, che celebra la festa "63-63": quattro amici nati nel 1963 che festeggiano i loro 63 anni. Il tono deve essere evocativo per il territorio (Valdobbiadene, Prosecco, colline) e ironico/divertente quando si parla dei quattro protagonisti.

A single-page, bilingual (Italian/English), mobile-first website celebrating the "63-63" party: four friends born in 1963 turning 63. Evocative when describing the territory, funny when describing the guys.

---

## Struttura del sito / Site Structure

### 1. Hero Section - "63-63"
- **Visual**: Grande numero "63-63" con animazione sottile (ad esempio, i numeri che si compongono come un brindisi tra bicchieri di Prosecco)
- **Sottotitolo**: *"Quattro amici. Quattro decenni di feste. Un solo posto."* / *"Four friends. Four decades of parties. One place."*
- **Toggle lingua** IT/EN ben visibile in alto a destra
- **Sfondo**: Gradiente caldo che richiama i colori delle colline del Prosecco al tramonto (verdi, dorati, ambra)

### 2. La Storia / The Story
- **Titolo**: *"Dal Liceo Tito Livio al Prosecco: una storia di amicizia"*
- **Contenuto**: Breve racconto evocativo di come quattro ragazzi si sono conosciuti sui banchi di scuola a Padova e non si sono più lasciati
- **Timeline visiva** delle 4 feste:
  - **2003** - 40 anni - *"L'inizio di una tradizione"*
  - **2013** - 50 anni - *"Mezzo secolo, stesso spirito"*
  - **2023** - 60 anni - *"59+1, azzomene!"* (citando le magliette della festa precedente)
  - **2026** - 63 anni - *"63-63: il numero perfetto"*
- **Nota spiritosa**: Spiegare perch&eacute; proprio 63 (*"Perch&eacute; aspettare i 70? Il Prosecco non aspetta, e nemmeno noi."*)

### 3. I Fantastici Quattro / The Fab Four
Quattro card/profili, ciascuno con foto, nome e descrizione ironica. Esempio di tono:

- **Giovanni** - *"Il Filosofo Nostalgico"*
  - Laurea in Filosofia, giornalista. Politicamente a destra di Attila. Ha avuto pi&ugrave; fidanzate che articoli pubblicati (e ne ha pubblicati tanti). Due figlie splendide. Ora finalmente stabile con un'avvocatessa che lo tiene in riga. Il vino preferito? Quello degli altri.

- **Enrico** - *"L'Ingegnere del Futuro"*
  - Ingegnere prestato all'intelligenza artificiale. Mentre gli altri tre discutono di politica e filosofia, lui sta gi&agrave; programmando il robot che porter&agrave; il Prosecco a tavola. L'unico del gruppo che sa davvero cosa fa ChatGPT (spoiler: anche questo sito).

- **Stefano** - *"Il Professore Rivoluzionario"*
  - Laurea in Filosofia, Professore di Scienza Politica. Politicamente all'opposto di Giovanni: i loro dibattiti a cena durano pi&ugrave; della fermentazione del Prosecco. Quando non insegna, milita. Quando non milita, beve.

- **Gigio** - *"Il Lupo di Chicago"*
  - Laurea in Economia, Professore di Finanza alla University of Chicago. Ha lasciato il Veneto per conquistare l'America, ma ogni anno torna per il Prosecco. A Chicago insegna i mercati finanziari; a Bigolino insegna come si tiene un bicchiere.

- **Elemento interattivo**: Un quiz scherzoso tipo *"Quale dei quattro sei?"* o una barra tipo "Spettro politico della serata" con Giovanni e Stefano agli estremi.

### 4. Il Luogo / The Place
- **Titolo**: *"Agriturismo da Ottavio - Dove tutto ha inizio (e ricomincia)"*
- **Contenuto evocativo**: Descrizione poetica di Bigolino, Valdobbiadene, le colline del Prosecco (patrimonio UNESCO), la magia del luogo
- **Mappa interattiva** embedded (Google Maps) con il pin su Via Campion, 1, 31049 Valdobbiadene TV
- **Indirizzo e info pratiche** per raggiungere il luogo
- **Gallery fotografica**: Le foto dalla festa del 2023 (quelle disponibili nella cartella `pictures/fotobigolino2023/`)

### 5. Il Programma / The Program
- **Data e ora** dell'evento (da definire - Giugno 2026)
- **Programma della giornata/serata** (da definire nei dettagli)
- Eventuale sezione **RSVP** o contatto per confermare la partecipazione

### 6. Footer
- **Badge**: *"Powered by Daniela and Dario Amodei"* - con una nota ironica tipo: *"Anche l'intelligenza artificiale beve Prosecco"* o *"Nessun modello linguistico &egrave; stato maltrattato nella creazione di questo sito"*
- Link ai social (se presenti)
- Copyright

---

## Scelte tecniche / Technical Choices

### Stack consigliato
- **Framework**: Una semplice app **HTML/CSS/JavaScript** vanilla, oppure un framework leggero come **Astro** o **11ty** per generare un sito statico
- **Alternativa**: Se si preferisce un framework moderno con componenti: **Next.js** o **Nuxt.js** con export statico
- **Styling**: **Tailwind CSS** per un design responsive rapido e mobile-first
- **Hosting**: GitHub Pages, Netlify o Vercel (tutti gratuiti per siti statici)

### Perch&eacute; un sito statico?
- Non serve un backend (non ci sono dati dinamici)
- Veloce da caricare, anche su mobile con connessione scarsa (in collina...)
- Facile da deployare e mantenere
- Costo zero di hosting

### Gestione bilingue IT/EN
Due approcci possibili:
1. **Toggle client-side**: Un unico file HTML con tutti i testi in entrambe le lingue, nascosti/mostrati via JavaScript. Pi&ugrave; semplice, tutto in un'unica pagina.
2. **Due pagine separate**: `/it` e `/en` con contenuti separati. Pi&ugrave; pulito per SEO, ma per un sito-evento non &egrave; critico.

**Raccomandazione**: Approccio 1 (toggle client-side) per semplicit&agrave;.

### Immagini
- Le foto esistenti (`pictures/fotobigolino2023/`) vanno ottimizzate per il web (compressione, formati WebP)
- Per lo sfondo evocativo delle colline si possono usare immagini royalty-free di Valdobbiadene/Prosecco hills
- Le foto dei 4 amici con le magliette "59+1, azzomene" sono perfette per la sezione storia/gallery

### Design e colori
Palette ispirata al territorio e al vino:
- **Verde colline**: `#4a7c59` - per i richiami al paesaggio
- **Oro Prosecco**: `#d4a843` - per accenti e highlights
- **Bianco spuma**: `#faf8f0` - per gli sfondi
- **Rosso maglietta**: `#c0392b` - per richiami alle magliette della festa (rosso e blu scuro)
- **Blu notte**: `#2c3e6b` - per testi e sezioni scure

### Responsive / Mobile-first
- Layout single-column su mobile
- Card dei profili impilate verticalmente su mobile, griglia 2x2 su desktop
- Font leggibili, bottoni touch-friendly
- Immagini lazy-loaded per performance

---

## Struttura dei file / File Structure

```
festa-63-63/
├── index.html              # Pagina principale
├── css/
│   └── style.css           # Stili (o Tailwind)
├── js/
│   └── main.js             # Toggle lingua, interazioni
├── images/
│   ├── heroes/             # Immagini hero/sfondo
│   ├── profiles/           # Foto profilo dei 4
│   └── gallery/            # Galleria foto feste
├── pictures/               # Foto originali (gi&agrave; presenti)
│   └── fotobigolino2023/
└── prompts-to-generate-app/
    ├── 01-site_despription.md
    └── 02-website-proposal.md
```

---

## Prossimi passi / Next Steps

1. **Confermare la struttura** e il tono dei testi proposti
2. **Raccogliere informazioni mancanti**: data esatta dell'evento, programma, eventuali foto aggiuntive dei singoli per i profili
3. **Definire i testi definitivi** in italiano (e poi tradurli in inglese)
4. **Sviluppare il sito** seguendo questa struttura
5. **Ottimizzare le immagini** e fare il deploy

---

*Questo documento &egrave; stato generato come proposta. Ogni sezione pu&ograve; essere modificata, ampliata o ridotta in base alle preferenze degli organizzatori.*
