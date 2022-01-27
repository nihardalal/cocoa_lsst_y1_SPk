from cobaya.likelihoods.lsst_y1._cosmolike_prototype_base import _cosmolike_prototype_base
import cosmolike_lsst_y1_interface as ci
import numpy as np

class lsst_3x2pt(_cosmolike_prototype_base):
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------

    def initialize(self):
        super(lsst_3x2pt,self).initialize(probe="3x2pt")
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------

    def logp(self, **params_values):
        self.set_cosmo_related()
        self.set_lens_related(**params_values)
        self.set_source_related(**params_values)
        datavector = ci.compute_data_vector_masked()
        if self.use_baryon_pca:
            self.set_baryon_related(**params_values)
            datavector = self.add_baryon_pcs_to_datavector(datavector)

        return self.compute_logp(datavector)
    
    def get_datavector(self, **params_values):
        self.set_cosmo_related()
        self.set_lens_related(**params_values)
        self.set_source_related(**params_values)
        datavector = np.array(ci.compute_data_vector_masked())
        if self.use_baryon_pca:
            self.set_baryon_related(**params_values)
            datavector = self.add_baryon_pcs_to_datavector(datavector)
        return np.array(datavector)
