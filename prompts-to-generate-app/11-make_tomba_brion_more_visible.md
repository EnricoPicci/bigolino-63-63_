Propose a way to make the button about "Tomba Brion" more visible. I want the visitor to notice is an be tempted to click on it.

# Response
Here's my proposal for making the Tomba Brion button more visible and tempting:                                                     
                                                                  
  ---                                                                                                                                 
  Proposal: Make the Tomba Brion CTA stand out 
                                                                                                                                      
  The current CTA is a white card with a simple navy button — it blends in with the surrounding content. Here are the changes I'd     
  suggest, from most impactful to least:

  1. Add a subtle pulse/glow animation to the button

  A soft repeating glow draws the eye without being obnoxious. The button would have a gentle pulsing box-shadow in gold (prosecco
  color), like a quiet "hey, look at me":

  @keyframes gentle-glow {
    0%, 100% { box-shadow: 0 0 8px rgba(212, 168, 67, 0.3); }
    50%      { box-shadow: 0 0 20px rgba(212, 168, 67, 0.6); }
  }
  .btn-tomba-brion {
    animation: gentle-glow 3s ease-in-out infinite;
  }

  2. Give the card a distinctive background

  Instead of plain white, use a subtle gradient or tinted background with a gold left border to visually separate it from the venue
  section:

  .tomba-brion-cta {
    background: linear-gradient(135deg, #faf8f0, #f0e8d0);
    border-left: 4px solid var(--color-gold-prosecco);
  }

  3. Make the button bigger and bolder

  Slightly larger padding, bigger font, and use the gold color instead of navy to make it stand out from other elements on the page:

  .btn-tomba-brion {
    padding: 1rem 2.5rem;
    font-size: 1.1rem;
    background: var(--color-gold-prosecco);
    color: #2c3e6b;
  }

  4. Add a small architectural icon

  Prepend a small Unicode or inline icon (like 🏛 or ◈) to the button text to make it visually richer.

  ---
  My recommendation: Apply all four together. They complement each other — the glow catches peripheral attention, the tinted card
  separates the CTA from surroundings, the larger gold button gives it visual weight, and the icon adds a touch of intrigue. The
  overall effect is inviting without being garish.

  # Refinement
  Do you think the position is the right one or should we put it more towards the top?

  # Response
  I think its current position actually makes sense. Here's my reasoning:                                                             
                                                                  
  The current placement works well because:                                                                                           
                                                                  
  1. It's contextual. It sits at the end of the venue section — the visitor has just read about Agriturismo da Ottavio in             
  Valdobbiadene and seen the map. "Half an hour from here" makes perfect sense right after seeing where "here" is.                    
  2. It's a natural discovery. Tomba Brion is a side attraction, not the main event. Putting it higher (e.g. after the hero or the
  story) would compete with the core content — who the friends are, what the party is about, RSVP.
  3. The page flow is logical: Hero → RSVP → Story → The Fab Four → Political Spectrum → Venue → "hey, while you're in the area..." →
  Gallery → Where to Stay. The CTA acts as a bonus reward for visitors who are engaged enough to scroll through the venue details.

  Moving it up would risk:
  - Breaking the "half an hour from here" context (from where?)
  - Distracting from the party itself before the visitor has even learned about it
  - Feeling out of place among the personal/celebratory sections

  My recommendation: Keep it where it is, but make it visually louder with the styling changes I proposed. The problem isn't position
  — it's that the CTA currently blends into the venue section like just another paragraph. A gold glow, tinted background, and bigger
  button will make it pop without moving it out of its natural context.