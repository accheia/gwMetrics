from lsst.sims.maf.metrics import BaseMetric
import defs as astr
import numpy as np




# Define our class, inheriting from BaseMetric
class AstrometryMetric(BaseMetric):
    # Add a doc string to describe the metric.
    """
    Bayesian Odds Ratio at each position.
    """
    # Add our "__init__" method to instantiate the class.
    # **kwargs allows additional values to be passed to the BaseMetric that you 
    #     may not have been using here and don't want to bother with. 
    def __init__(self, metricName='astrometry', **kwargs):
        # Set the values we want to keep for our class.
        self.AMcol = 'airmass'
        self.Fcol = 'filter'
        cols=[self.AMcol, self.Fcol]
        # Now we have to call the BaseMetric's __init__ method, to get the "framework" part set up.
        # We currently do this using 'super', which just calls BaseMetric's method.
        # The call to super just basically looks like this .. you must pass the columns you need, and the kwargs.
        super(AstrometryMetric, self).__init__(col=cols, metricName=metricName, **kwargs)
    # Now write out "run" method, the part that does the metric calculation.
    def run(self, dataSlice, slicePoint=None):
        result = astr.bayesian_odds_ratio(dataSlice[self.AMcol], dataSlice[self.Fcol], astrometric_error=0.020, zshift=2.1)
        return result

class AirmassRangeMetric(BaseMetric):
    # Add a doc string to describe the metric.
    """
    Range of airmasses at each position.
    """
    # Add our "__init__" method to instantiate the class.
    # **kwargs allows additional values to be passed to the BaseMetric that you 
    #     may not have been using here and don't want to bother with. 
    def __init__(self, metricName='maxairmass', **kwargs):
        # Set the values we want to keep for our class.
        self.AMcol = 'airmass'
        self.Fcol = 'filter'
        cols=[self.AMcol, self.Fcol]
        # Now we have to call the BaseMetric's __init__ method, to get the "framework" part set up.
        # We currently do this using 'super', which just calls BaseMetric's method.
        # The call to super just basically looks like this .. you must pass the columns you need, and the kwargs.
        super(MaxAirmassMetric, self).__init__(col=cols, metricName=metricName, **kwargs)
    # Now write out "run" method, the part that does the metric calculation.
    def run(self, dataSlice, slicePoint=None):
        result = np.max(dataSlice[self.AMcol]) - np.min(dataSlice[self.AMcol])
        return result

class NumObsMetric(BaseMetric):
    # Add a doc string to describe the metric.
    """
    Number of observations at each position.
    """
    # Add our "__init__" method to instantiate the class.
    # **kwargs allows additional values to be passed to the BaseMetric that you 
    #     may not have been using here and don't want to bother with. 
    def __init__(self, metricName='NumObs', **kwargs):
        # Set the values we want to keep for our class.
        self.AMcol = 'airmass'
        self.Fcol = 'filter'
        cols=[self.AMcol, self.Fcol]
        # Now we have to call the BaseMetric's __init__ method, to get the "framework" part set up.
        # We currently do this using 'super', which just calls BaseMetric's method.
        # The call to super just basically looks like this .. you must pass the columns you need, and the kwargs.
        super(NumObsMetric, self).__init__(col=cols, metricName=metricName, **kwargs)
    # Now write out "run" method, the part that does the metric calculation.
    def run(self, dataSlice, slicePoint=None):
        result = len(dataSlice[self.AMcol])
        return result
