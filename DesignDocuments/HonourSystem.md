Warning. This long post might not be coherent. I simply need to get this idea
out of my head in order to move on to other stuff.  It might be worth building
on later.  Who knows.

I'm imagining a game that involves dungeon crawling and monster killing for
treasure... not that out of the ordinary.  But instead of hard coding all of
the rules of say D&D v 3.5  or some equivalent... I would build an encounter
system based on player narrative. Players can choose to succeed or fail in
combat (or other obstacles) and only really need to record their reasons.
Rolling dice is optional and supported but only the player can interpret the
meaning of the die rolls.

Picture this:

Enter a room
The room is 20x30'. It is furnished with bones and detritus of many past meals.
The bones look humanoid. The air is thick with the stench of decay. 
A large mud troll is here, finishing it's latest meal. It is hostile.
Exit: north door, east passage, south passage.

Decide on a response
Although the game is in real time, things partially freeze for the player when
the initiate an encounter. That is, the mob doesn't initiate anything (except
perhaps in certain special coded ambush situations) until the player decides
what their character/puppet wants to do.
However, they cannot leave the room or interact with it's contents until making
a decision about how they will deal with the encounter. Essentially the player
must describe how they intends to play out the encounter in a journal
(automatically recorded). 

> engage
How do you want to engage the large mud troll?
> attacking it with my sword.
How will you determine if "attacking it with my sword" is successful?
a. roll dice 
b. succeed
c. fail
> a 
Enter a number and die size to roll:  ie. 2d6
> 1d20
You roll a 20 sided die ... 13! What does this mean?
a. success
b. failure
> a
You successfully engaged the large mud troll. Please update it's status:
a. hostile
b. friendly
c. helpless or unaware
d. dead
> d
Describe how it died.
> My vorpal blade went snicker snuff.. I lopped its vile head clean off.
You update your journal for today's date and time: 
I encountered a large mud troll and engaged it by "attacking it with my sword"
(I rolled a 13 on 1d20  = success)
"My vorpal blade went snicker snuff.. I lopped its vile head clean off."
-----
> look
The room is 20x30'. It is furnished with bones and detritus of many past meals.
The bones look humanoid. The air is thick with the stench of decay. 
The corpse of a large mud troll is here.
Exit: north door, east passage, south passage.
> look corpse
The corpse of a large mud troll contains:
13 silver pieces, a crude club, 3 human bones, 
 
 Implications
 There are no "rules" per se, however the journal cannot be edited or deleted.
 Under certain circumstances it becomes visible to other players. So lazy
 role-play as well as absurd munchkinism will be embarrassingly obvious. It
 allows the player to decide on the fly how "hard core" they are playing. The
 option to roll for success or failure allows a player to apply RPG rules of
 their choosing.

 Game side. While the player has ultimate power over the success or failure of
 the encounter, the developers/authors can have more influence over the
 behavior of the monsters if they wish.  In this example I provided four
 "states" for the monster. a. hostile, b. friendly, c. helpless or unaware, d.
 dead.  While the player determined which state the monster ended up in.  The
 developer/builder can determine how the monster expresses those states, and
 what state it is initially encountered in. For example, if the player finishes
 their move by declaring "failure" I might include a variety of attack moves
 that the troll will use while in a "hostile" state. 

 Example:
  The large mud troll lunges at your attempting to bite you!
   How do you defend?
   > by ducking out of the way 
   How will you determine if "ducking out of the way" is successful?
   a. roll dice 
   b. succeed
   c. fail
   > c 
   You failed to defend the large mud troll's bite attack. It's horrendous
   teeth sink into your flesh spreading disease.
   How does this affect you?
   a. no effect
   b. it affects my status (update)
   c. it kills me
   > a.
   Why did the large mud troll's bite attack have no effect?
   > because I am wearing a medallion of protection from teeth and disease
   You update your journal for today's date and time: 
   The large mud troll lunged at me attempting to bite me with its filthy
   mouth.
   "ducking out of the way" failed, and
   It's horrendous teeth sunk into my flesh spreading disease.
   The large mud trolls bite attack had no effect because I am wearing a
   medallion of protection from teeth and disease.

   In this case, the trolls attack and the description of its intended effects
   would come from the definition of the troll monster itself.  The definition
   might also explain what a troll does if it is in a "friendly" state - ie.
   maybe it follows the character from room to room, or offers to trade goods,
   or merely ignores them. In most cases helpless or unaware states would allow
   a player to sneak past, pickpocket, or assassinate a monster.  The duration
   of a helpless/unaware state might be specified by the player - preferably
   with a reason. Ie. helpless for 10 minutes because I cast a sleep spell or
   "unaware for 10 seconds as I slip past  it through the shadows".

   Player status

   A similar system allows the player to record effects on their character for
   future reference, usually to help with future game play decisions. In the
   example above, if the player chose "b. it affects my status" this could open
   up a couple of interesting options by calling perhaps an "update" command.

   >update
   What do you want to update:
   a. my existing traits
   b. add a trait
   > b
   Name the trait:
   > infected
   Enter a new value for infected (a numerical score or True/False):
   > true
   Duration: specify number and time unit ie. 1 day, or 2 hours, or 30 sec.
   press enter or "0" for indefinite duration.
   > 1 day
   ...
   after a day worth of time passes in your game:
   ...
   You have been "infected" for 1 day
   a. remove trait
   b. snooze (repeat timer)
   c. update (use this to affect other traits or to edit the timer on this one)
   > c
   What do you want to update:
   a. my existing traits
   b. add a trait
   > a
   Which trait to update?:
   1. Strength = 17
   2. Wisdom = 9
   3. Charisma = 13
   4. Health = 10
   5. Infected = True, 1 day 
   > 4 
   Enter a new value for health (a numerical score or True/False):
   > 6
   Why did your health change?
   > I have been infected for one day.
   You update your journal for today's date and time:
   I have been infected for one day. 
   My Health changed to 6.

   Traits can include all kinds of personal effects from being mortally
   wounded---bleeding out in minutes to being invisible, or invulnerable.
   Traits can be used to record and track traditional RPG stats and abilities
   or even represent the use of weapons, armor, magic items. Even something
   simple as the need for food could easily be simulated by a timed trait.

   While the examples above are not necessarily internally consistent or
   logical, they illustrate a sort of game play. I expect traps, magic items,
   monster encounters even certain parley scenes could be simulated this way. I
   suspect there might even be interesting hybrids of this model - like hard
   coding a certain set of stats for a particular play style to help give the
   players a little bit of focus (ie. prompt the player to role a strength
   check when attacking or dex when evading).  

   A magic system based on this could work with almost no code beyond simple
   spell descriptions as might be found in an RPG rule book. Casting a spell
   might simply add an entry to a journal and allow a player to update
   themselves or other objects in the game.

   One of the products of a game like this would be a journal that details the
   character's exploits, much like a black box recorder. The player can add to
   it in some ways but generally cannot delete or remove events (except perhaps
   optional free form sections not tied to in game events).  Perhaps this hints
   at the simplest possible implementation of this engine.  At any object or
   room in the game with an "obstacle" tag the player is stopped until they
   resolve the obstacle by choosing "pass or fail".  Any resolution requires an
   explanation in the journal. Once the journal entry is completed the player
   chooses pass or fail. Pass allowing them to remove the obstacle tag - and
   resume moving and acting in the mud with normal commands. Fail requires the
   player to decide whether to retreat from the obstacle, leaving it intact and
   ready to trigger next time they engage, or to die. (Whatever that might mean
   in the particular game, permadeath or position reset for example).

   In either implementation of this engine the end result is a journal or log,
   which either makes sense and looks consistent or which is empty and
   meaningless. Ideally the player would have only themselves to credit or
   blame for its final state.


   ...

   end of brain dump for now.

   but questions remain... 

   ...like would this be compatible with PVP? Why not?
   ...could I use this to implement a computer version of Dungeon World(TM) or
   other Powered by the Apocalypse(TM) style RPG.
   ...Is this already how MUSHs work and I look ridiculous right now? (cause I
   honestly have no idea)
   ... why can't I make myself go to sleep.

