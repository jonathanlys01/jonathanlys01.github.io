# ASCII Sharks

`ocean.min.js` bundles [stackedlol/ascii-sharks](https://github.com/stackedlol/ascii-sharks)
at commit `c521e24a787e6d4cc460d4cf2b9815f25e4fe453`.
The original simulation and renderer are unchanged. The site uses its own
small animation loop in `assets/js/site-ocean.js`; monochrome compositing and
theme adaptation live in `assets/css/main.scss`.

To reproduce the vendored ES module from an upstream checkout at that commit:

```sh
npm install --ignore-scripts
node_modules/.bin/esbuild src/index.ts --bundle --format=esm --minify --outfile=ocean.min.js
```

The bundled file is committed so the Jekyll site needs no JavaScript build step.
The aquarium uses system monospace fonts and makes no external requests.
Keep it outside directories named `vendor`, which this repository ignores.
