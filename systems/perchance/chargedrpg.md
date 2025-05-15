```
dsix = {1-6}
dfour = {1-4}
dtwenty = {1-20}

chargedrpg_eb = {import:chargedrpg-eb}
chargedrpg_metamorphica = {import:chargedrpg-metamorphica}

background
  EB
    bgname = [chargedrpg_eb.bgname]
    blurb = [chargedrpg_eb.blurb]
    bond
      Take bond <b>{1-30}</b> from deep Carbon Observatory. ^0
      [chargedrpg_eb.debt] ^1
    name = [chargedrpg_eb.name]
    event1 = [chargedrpg_eb.event1]
    event2 = [chargedrpg_eb.event2]
    equip = [chargedrpg_eb.equip]

physique
  athletic
  brawny
  flabby
  lanky
  rugged
  scrawny
  short
  statuesque
  stout
  towering

skin
  birthmarked
  marked
  oily
  rosy
  scarred
  soft
  tanned
  tattooed
  weathered
  webbed

hair
  no
  braided
  curly
  filthy
  frizzy
  long
  luxurious
  oily
  wavy
  wispy

face
  bony
  broken
  chiseled
  elongated
  pale
  perfect
  rakish
  sharp
  square
  sunken

speech
  blunt
  booming
  cryptic
  droning
  formal
  gravelly
  precise
  squeaky
  stuttering
  whispery

clothing
  antique clothing
  bloody clothing
  elegant clothing
  filthy clothing
  foreign clothing
  frayed clothing
  frumpy clothing
  livery
  rancid clothing
  soiled clothing

virtue
  ambitious
  cautious
  courageous
  disciplined
  gregareous
  honorable
  humble
  merciful
  serene
  tolerant

vice
  aggressive
  bitter
  craven
  deceitful
  greedy
  lazy
  nervous
  rude
  vain
  vengeful

mutation
  <b>You have no mutations</b> ^80
  [chargedrpg_metamorphica] <br><br> <i>Your mutation takes 1 of your inventory slots.</i> ^15
  [chargedrpg_metamorphica] <br><br> [chargedrpg_metamorphica] <br><br> <i>Your mutations take 2 of your inventory slots.</i> ^05
```