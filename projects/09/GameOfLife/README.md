# Summary

Conway's Game of Life simulation implemented in Jack programming language.

See [Wikipedia article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) for more information.

# Usage instructions

1. Make sure the VM emulator is set to "Fast" speed. "Animate" needs to be set
to "No Animation".
2. Follow the instructions on the screen. Namely, press 's' to start.
3. Next, you are presented with a world editor. It is possible to toggle any
points on the screen. Editing begins when 'e' is pressed. Editing is optional
as the world is already prepopulated with various life configurations.
4. Once you are satisfied with the world state press 's' to begin simulation.

# Internals

The simulation uses a 32x64 grid. Smaller points would be hard to see on the
screen.

The grid is modeled with 2 dimensional array. Recomputation is applied row by
row to optimize memory usage (as opposed to computing a whole new state).

The program is designed with a simple object oriented design. There's a Game,
Editor and World. World models the grid and computation of next generations.
Game sets the execution up. For example, certain life forms are spawned and
instructions are shown. Editor handles creation and modification of the world.

There are violations of cohesion in code. Ideally, graphics rendering could be
separated. However, it has been kept inside of the World class for performance
reasons.

# Future work

Simulation never stops so dispose() method is never called on the World and
Editor objects.

Rendering performance could be improved. There are no graphic optimizations
applied.

The editor's user experience leaves a lot to be desired.