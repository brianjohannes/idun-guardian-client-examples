from bci_essentials.io.lsl_sources import LslEegSource, LslMarkerSource
from bci_essentials.io.lsl_messenger import LslMessenger
from bci_essentials.erp_data import ErpData
from bci_essentials.classification.erp_single_channel_classifier import ErpSingleChannelClassifier

# create LSL sources, these will block until the outlets are present
eeg_source = LslEegSource()
marker_source = LslMarkerSource()
messenger = LslMessenger()

# Set classifier settings ()
classifier = ErpSingleChannelClassifier()  # you can add a subset here

# Set some settings
classifier.set_p300_clf_settings(
    n_splits=5,
    lico_expansion_factor=1,
    oversample_ratio=0,
    undersample_ratio=0,
)

# Initialize the ERP
test_erp = ErpData(classifier, eeg_source, marker_source, messenger)

# Run main
test_erp.setup(
    online=True,
    training=True,
    pp_low=0.1,
    pp_high=10,
    pp_order=5,
    plot_erp=False,
    trial_start=0.0,
    trial_end=0.8,
    max_num_options=10,
    max_trials_per_option=20,
    max_trials=10000,
    max_decisions=500,
)
test_erp.run()