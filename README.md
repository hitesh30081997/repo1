[NeMo E 2026-10-08 14:44:27 save_restore_connector:191] Model instantiation failed!
    Target class:	nemo.collections.asr.models.SLUIntentSlotBPEModel
    Error(s):	'MultiLayerPerceptron' object has no attribute 'mlp'
    Traceback (most recent call last):
      File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/core/classes/common.py", line 621, in from_config_dict
        instance = imported_cls(cfg=config, trainer=trainer)
      File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/collections/asr/models/slu_models.py", line 90, in __init__
        self.sequence_generator = SequenceGenerator(
      File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/collections/asr/parts/utils/slu_utils.py", line 76, in __init__
        self.generator = GreedySequenceGenerator(embedding, decoder, log_softmax, **common_args)
      File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/collections/asr/modules/transformer/transformer_generators.py", line 124, in __init__
        self.num_tokens = getattr(self.classifier.mlp, f'layer{self.classifier.mlp.layers - 1}').out_features
      File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1967, in __getattr__
        raise AttributeError(
    AttributeError: 'MultiLayerPerceptron' object has no attribute 'mlp'
    
Traceback (most recent call last):
  File "/home/common/Pictures/app.py", line 8, in <module>
    model = nemo_asr.models.ASRModel.restore_from(restore_path="/home/common/Downloads/nvidia-conformer-large-slurp-other-default-v1/slu_conformer_transformer_large_slurp_1.nemo")
  File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/core/classes/modelPT.py", line 501, in restore_from
    instance = cls._save_restore_connector.restore_from(
  File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/core/connectors/save_restore_connector.py", line 270, in restore_from
    loaded_params = self.load_config_and_state_dict(
  File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/core/connectors/save_restore_connector.py", line 191, in load_config_and_state_dict
    instance = calling_cls.from_config_dict(config=conf, trainer=trainer)
  File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/core/classes/common.py", line 645, in from_config_dict
    raise e
  File "/home/common/miniconda3/envs/cardio_care_ai/lib/python3.10/site-packages/nemo/core/classes/common.py", line 637, in from_config_dict
    instance = cls(cfg=config, trainer=trainer)
TypeError: Can't instantiate abstract class ASRModel with abstract methods setup_training_data, setup_validation_data
