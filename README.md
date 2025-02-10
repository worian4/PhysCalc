# PhysCalc
PhysCalc is an analog to apps like Photomath, but equievalent for physics.

Algorithm: PhysCalc substitudes input values to precalculated formulas and calculates it as an equasion, so you can make him calculate the difficult physical tasks, that are more difficult, than, for example, solve F = m * a, knowing m and a. Example for a task for PhysCalc can be to find I, knowing P and R (formulas P = U * R, U = I * R).

All data is in located in ```res``` folder. You can find original formulas in ```res/base_formulas.txt``` and pregenrated formulas in ```res/derivative_formulas.txt```. Additionally, ```res``` contains some constants in ```res/consts.txt```, formulas to turn to SI system of measurement in ```sn_input.txt``` and formulas to return to input system of measurement in ```res/sn_output.txt```. Pay attention, that there's not much data in files, that's because my project is more concentrated on code, than on data, so finding your personal data might be required for you.

If you want to locate the class only, download ```core/calc.py```, but i highly reccomend installing all files, as they content basic formulas, constants and formulas to turn input units to system of notation units. Also, in ```main.py``` you can see the examples of input and how to upload ```res```.

Installation:
1. Install all files.
2. Go to ```main.py``` and run part of the code in ```''' '''``` to generate the fomulas.
3. Wait for them to generate (this may take a few minutes).
4. Comment the code back.
5. PhysCalc is installed!

Requirements:
1. Python 3.0 or higher.
2. Sympy Library installed.
