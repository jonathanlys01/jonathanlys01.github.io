# frozen_string_literal: true

PYTORCH_CANVAS_HTML = '<canvas id="ascii-pytorch-logo-icon" role="img" aria-label="pytorch logo icon" style="width: 50px !important; height: auto !important; aspect-ratio: 54 / 64 !important; flex-shrink: 0; display: inline-block !important; vertical-align: middle; margin-right: 0.75rem;"></canvas>'

PYTORCH_SCRIPT = <<~HTML
<script type="module">
import { mount } from "https://ascii.rest/mount.js";

const meta = {
  name: "pytorch logo icon",
  category: "companies",
  note: "the pytorch logo icon logo, glinting now and then",
  cols: 54,
  rows: 32,
  fps: 30,
  options: { shine: 3 },
  palette: [
    "#ee4c2c", "#f48b76", "#fac9c0", "#ee4c2c", "#f48b76", "#fac9c0",
  ],
};

const MONO = String.raw`

                         _p
                       _p88
                     _p8888
                   _p888888
                 _p8888888P
               _p8888888P'      .p888q,
             _p8888888P'        q888888
           _p8888888P'          '88888"
         _p8888888P'              '"'       _
       _p8888888P'                        _p8q,
      q8888888P'                        _p88888p
     p888888P'                          "8888888q
    p888888"                              "888888p
   q888888"                                "888888p
  .888888"                                  )888888,
  q88888P                                    888888p
  d88888|                                    d88888b
  888888|                                    d888888
  888888|                                    d888888
  d88888p                                    888888P
  '888888,                                  q888888'
   d888888,                                _888888P
    8888888,                              _888888P
     8888888q,                          _p888888P
      Y8888888q,                      _p8888888P
       "88888888q_,                _pp88888888"
         "8888888888qq__________pp8888888888"
           "Y8888888888888888888888888888P"
              "Y8888888888888888888888P"
                  ""Y88888888888PP""

`;

const ART = String.raw`

                         _p
                       _p88
                     _p8888
                   _p888888
                 _p8888888P
               _p8888888P'      .p888q,
             _p8888888P'        q888888
           _p8888888P'          '88888"
         _p8888888P'              '"'       _
       _p8888888P'                        _p8q,
      q8888888P'                        _p88888p
     p888888P'                          "8888888q
    p888888"                              "888888p
   q888888"                                "888888p
  .888888"                                  )888888,
  q88888P                                    888888p
  d88888|                                    d88888b
  888888|                                    d888888
  888888|                                    d888888
  d88888p                                    888888P
  '888888,                                  q888888'
   d888888,                                _888888P
    8888888,                              _888888P
     8888888q,                          _p888888P
      Y8888888q,                      _p8888888P
       "88888888q_,                _pp88888888"
         "8888888888qq__________pp8888888888"
           "Y8888888888888888888888888888P"
              "Y8888888888888888888888P"
                  ""Y88888888888PP""

`;

const INK = String.raw`

                         00
                       0000
                     000000
                   00000000
                 0000000000
               00000000000      0000000
             00000000000        0000000
           00000000000          0000000
         00000000000              000       0
       00000000000                        00000
      0000000000                        00000000
     000000000                          000000000
    00000000                              00000000
   00000000                                00000000
  00000000                                  00000000
  0000000                                    0000000
  0000000                                    0000000
  0000000                                    0000000
  0000000                                    0000000
  0000000                                    0000000
  00000000                                  00000000
   00000000                                00000000
    00000000                              00000000
     000000000                          000000000
      0000000000                      0000000000
       000000000000                000000000000
         000000000000000000000000000000000000
           00000000000000000000000000000000
              00000000000000000000000000
                  000000000000000000

`;

const START = 0.5;
const PASS = 2;
const HALF = 5;
const LEAN = 0.9;
const SOLID = "8dbqpPYOo0";

const lines = (art) => art.slice(1, -1).split("\\n").map((line) => line.padEnd(meta.cols));

function pytorchLogoIcon({ shine = meta.options.shine } = {}) {
  const { cols, rows } = meta;
  const mono = lines(MONO), art = lines(ART), ink = lines(INK);
  const n = meta.palette.length / 6;
  const every = shine > 0 ? Math.max(shine, PASS + 0.5) : 0;
  let lo = Infinity, hi = -Infinity;
  for (const pic of [mono, art])
    pic.forEach((line, y) => {
      for (let x = 0; x < cols; x++) if (line[x] !== " ") (lo = Math.min(lo, x + LEAN * y)), (hi = Math.max(hi, x + LEAN * y));
    });
  const span = hi - lo + 2 * HALF;

  return (t, { paper = false, color } = {}) => {
    const pic = color ? art : mono;
    const since = t - START;
    const at = every && since >= 0 ? lo - HALF + (span * (since % every)) / PASS : -Infinity;
    const out = [];
    for (let y = 0; y < rows; y++) {
      let line = "";
      for (let x = 0; x < cols; x++) {
        let ch = pic[y][x];
        if (ch !== " ") {
          const d = Math.abs(x + LEAN * y - at);
          let k = d < HALF ? 1 - d / HALF : 0;
          k = k * k * (3 - 2 * k);
          if (k > 0.55 && SOLID.includes(ch)) ch = "/";
          if (color) color[y * cols + x] = (paper ? 0 : 3 * n) + (k > 0.6 ? 2 : k > 0.25 ? 1 : 0) * n + parseInt(ink[y][x], 36);
        }
        line += ch;
      }
      out.push(line);
    }
    return out.join("\\n");
  };
}

const el = document.getElementById("ascii-pytorch-logo-icon");
if (el) {
  mount(el, { meta, default: pytorchLogoIcon });
}
</script>
HTML

# Inject the canvas and script into the rendered post layout output
Jekyll::Hooks.register :posts, :post_render do |post|
  tags = Array(post.data['tags']).map(&:to_s).map(&:downcase)
  if tags.include?('pytorch')
    # Inject canvas into the single-post header (<h1 class="post-title">)
    post.output = post.output.sub(/(<h1\s+class=["']post-title["'][^>]*>)/) do |m|
      "#{m}#{PYTORCH_CANVAS_HTML}"
    end
    # Inject mounting script before </body>
    post.output = post.output.sub('</body>', "#{PYTORCH_SCRIPT}\n</body>")
  end
end
