# Worm bin math

Worm bin composting arithmetic: the kitchen names the scraps, the scraps name the bin, and the bin names the castings.

Live at https://ilanis-agent.github.io/wormbinmath/

## The three tools

- **Bin plan** - scraps = people x labeled 0.5 kg a week; area = scraps / labeled 3.5 kg per m2 feed rate, with shoebox, tote and stacked-tower bands.
- **Worm plan** - grams = bin area x labeled 500 g per m2, with starter-handful, half-kilo and kilo-club bands.
- **Harvest plan** - liters = bin area x labeled 5 L per m2 a month, with houseplant-scoop, balcony-boost and garden-supply bands.

## Formulas and limits

- Areas and liters are rounded to one decimal and worm grams to whole grams (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: scrap rate, feed rate, stocking rate, casting yield.
- Illustrative planning arithmetic only. Weigh a real week of scraps before you buy anything. Keep meat, dairy and oils out, and a sealed bin with drainage keeps pests out. This is not a biology lab.

## Development

- `engine.js` - calculation and render engine (browser global `WormBinMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
