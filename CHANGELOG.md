# Changelog

## 0.3.11 - 2025-10-23

- Add type hints for `matplotlib.pyplot`'s `show`, `tight_layout`, `bar`, `xticks` and `yticks`

## 0.3.10 - 2025-10-22

- Add `matplotlib.pyplot.loglog` type hints

## 0.3.9 - 2025-10-22

- Fix broken import in `matplotlib.pyplot.plot_date`

## 0.3.8 - 2025-10-22

- Add `matplotlib.pyplot.xlim` and `matplotlib.pyplot.ylim` overloads, including datetime support

## 0.3.7 - 2025-10-21

- Add `matplotlib.pyplot.axhline`'s kwargs type

## 0.3.6 - 2025-10-19

- Add `matplotlib.axes.Axes.set_xticks`
- Fix `matplotlib.axes.Axes.bar` to support datetime sequences

## 0.3.5 - 2025-10-14

Fix `matplotlib.pyplot.plot` to allow using datetime sequences.

## 0.3.4 - 2025-09-11

- Complete type hints for:
  - `matplotlib.pyplot.subplots_adjust`
  - `matplotlib.pyplot.subplots`
  - `matplotlib.pyplot.subplot_mosaic`

## 0.3.3 - 2025-09-04

- Complete `matplotlib.pyplot.text`'s type hints
- Fix `matplotlib.cm.colors`

## [0.3.2] - 2025-08-07

- Add `matplotlib.cm`'s colormaps

## [0.3.1] - 2025-08-04

- Add return type to `plt.ylabel` and `plt.xlabel`
- Fix/refine argument types for `plt.savefig`, `plt.plot` and `plt.scatter`

## [0.3.0] - 2025-08-02

Improve type hints for the following functions:

- `matplotlib.pyplot.close()`
- `matplotlib.pyplot.figure()`
- `matplotlib.pyplot.legend()`
- `matplotlib.pyplot.plot()`
- `matplotlib.pyplot.savefig()`
- `matplotlib.pyplot.scatter()`
- `matplotlib.pyplot.title()`
- `matplotlib.pyplot.xlabel()`
- `matplotlib.pyplot.ylabel()`

## 0.2.0 - 2023-07-19

- Strictly type Colormap.**call**.
