# Import MC wrapper API from the python plugin
from mcapi import *

# Import data types and events from Spigot
from org.bukkit.event.player import PlayerInteractEvent
from org.bukkit.Material import *

# Runs on item used
@asynchronous()
def item_used(e):
    # Get player location and player object
    player = e.getPlayer()
    loc = location(player)

    # Do checks
    if player.getItemInHand().getType() == FLINT_AND_STEEL:
        print(player.getName() + " used a flint and steel at location " + str(loc.getBlockX()) + ", " + str(loc.getBlockY()) + ", " + str(loc.getBlockZ()))

# Register events
listener = add_event_listener(PlayerInteractEvent, item_used)

