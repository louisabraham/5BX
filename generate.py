from pathlib import Path

DST = Path("frames")
CHARTS = 2
LEVELS = 12

levels = [(chart, level)
          for chart in range(CHARTS)
          for level in range(LEVELS)]

DST.mkdir(exist_ok=True)


for i, (c, l) in enumerate(levels):
    with open(DST / ('%s.html' % i), 'w') as f:
        print('---', file=f)
        print('layout: level', file=f)
        print('chart:', c, file=f)
        print('level:', l, file=f)
        print('---', file=f)
