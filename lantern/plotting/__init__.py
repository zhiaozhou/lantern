from .plot_matplotlib import MatplotlibPlot
from .plot_cufflinks import CufflinksPlot
from .plot_bokeh import BokehPlot

_BACKENDS = ['cufflinks', 'plotly', 'bokeh', 'highcharts', 'matplotlib', 'seaborn']


def _backend_to_plot_obj(backend, theme=None):
    if backend == 'matplotlib' or backend == 'seaborn':
        return MatplotlibPlot(theme)
    if backend == 'cufflinks' or backend == 'plotly':
        return CufflinksPlot(theme)
    if backend == 'bokeh':
        return BokehPlot(theme)


def figure(backend='matplotlib', theme=None):
    if backend not in _BACKENDS:
        raise Exception('Must pick backend in %s' % _BACKENDS)
    return _backend_to_plot_obj(backend, theme)


def plot(data, kind='line', backend='matplotlib', theme=None, **kwargs):
    f = figure(backend, theme)

    show_args = {}
    show_args['title'] = kwargs.pop('title', '')
    show_args['xlabel'] = kwargs.pop('xlabel', '')
    show_args['ylabel'] = kwargs.pop('ylabel', '')
    show_args['xaxis'] = kwargs.pop('xaxis', True)
    show_args['yaxis'] = kwargs.pop('yaxis', True)
    show_args['xticks'] = kwargs.pop('xticks', True)
    show_args['yticks'] = kwargs.pop('yticks', True)
    show_args['legend'] = kwargs.pop('legend', True)
    show_args['grid'] = kwargs.pop('grid', True)

    # TODO
    if isinstance(kind, str):
        getattr(f, kind)(data, **kwargs)
        return f.show(**show_args)
    elif isinstance(kind, list):
        pass
    elif isinstance(kind, dict):
        pass
