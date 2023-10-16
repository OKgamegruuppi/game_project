UPDATE 1.01 ---- 16.10.2023
Lisätty 'New Game' nappi Game Over screeniin
Restart Game: settingeissä "Restarting" gamestate
map/clear_map -> clear_map() : nollaa kaikki ryhmät, poistaa Groupseista oliot, periaattees pitäis olla tuhoamatta -kaikki- settings jos haluaa tehä high scoren

Lisätty hurt cooldown (invincibility frames) Creature luokkaan
---> self.hurt_cd_dur määrittelee sen pituuden
---> self.status["hurt_cooldown"] : aktiivinen cooldown meneillään

Lisätty wood-chips kuvake puiden hurt iconiksi

Effects luokkaan uutena parametrinä jitter (kuinka paljon efektin sijainti heittää keskipisteestä, oletus 0)
