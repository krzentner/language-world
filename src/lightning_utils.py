import torch
import lightning
import lightning.pytorch as pl
import pytorch_utils
from constants import N_EPOCHS
from os.path import expanduser


class LightningModel(pl.LightningModule):
    def __init__(self, model, preprocess, loss_function, learning_rate, momentum):
        super().__init__()
        self.model = model
        self.preprocess = preprocess
        self.loss_function = loss_function
        self.learning_rate = learning_rate
        self.momentum = momentum

    def training_step(self, batch, batch_idx):
        inputs, targets = self.preprocess(batch)
        inputs_dev = [
            i.to(self.device) if isinstance(i, torch.Tensor) else i for i in inputs
        ]
        loss, infos = self.loss_function(
            self.model, *inputs_dev, targets.to(self.device)
        )
        for k, v in infos.items():
            self.log(k, v)
        return loss

    def configure_optimizers(self):
        return torch.optim.SGD(
            self.parameters(), lr=self.learning_rate, momentum=self.momentum
        )


class LightningFitCallbackAdapter(pl.callbacks.Callback):
    def __init__(self, fit_callbacks):
        self.fit_callbacks = fit_callbacks

    def on_train_epoch_start(self, trainer, module):
        self.fit_callbacks.epoch_start(module.model)

    def on_train_epoch_end(self, trainer, module):
        self.fit_callbacks.epoch_end(module.model)

    def on_train_batch_start(self, trainer, module, batch, idx):
        self.fit_callbacks.minibatch_start(module.model)

    def on_train_batch_end(self, trainer, module, outputs, batch, idx):
        self.fit_callbacks.minibatch_start(module.model)

    def on_train_end(self, trainer, module):
        self.fit_callbacks.training_complete(module.model)


class GeneratorIterator:
    def __init__(self, gen_callback):
        self.gen_callback = gen_callback

    def __iter__(self):
        return self.gen_callback()


def fit_model(
    data,
    create_model,
    loss_function,
    model_name,
    preprocess,
    batch_size=16,
    n_epochs=N_EPOCHS,
    seed=pytorch_utils.DEFAULT_SEED,
    learning_rate=1e-4,
    momentum=0.995,
    callbacks=pytorch_utils.FitCallbacks(),
    accelerator="gpu",
):
    torch.manual_seed(seed)
    workdir = expanduser(f"~/data/fit_model={model_name}_seed={seed}")
    model = create_model(preprocess(data[:1])[0])
    module = LightningModel(model, preprocess, loss_function, learning_rate, momentum)
    fit_callbacks = LightningFitCallbackAdapter(callbacks)
    trainer = pl.Trainer(
        max_epochs=n_epochs,
        default_root_dir=workdir,
        accelerator=accelerator,
        callbacks=[fit_callbacks],
    )
    trainer.fit(
        model=module,
        train_dataloaders=GeneratorIterator(
            lambda: pytorch_utils.approx_minibatches(data, batch_size)
        ),
    )


def fit_model_multisource(
    sources,
    source_repeats,
    create_model,
    loss_function,
    model_name,
    preprocess,
    batch_size=16,
    n_epochs=N_EPOCHS,
    seed=pytorch_utils.DEFAULT_SEED,
    learning_rate=1e-4,
    momentum=0.995,
    callbacks=pytorch_utils.FitCallbacks(),
    accelerator="gpu",
):
    torch.manual_seed(seed)
    workdir = expanduser(f"~/data/fit_model={model_name}_seed={seed}")
    first_batch = next(
        pytorch_utils.multisource_approx_minibatch(sources, source_repeats)
    )
    model = create_model(preprocess(first_batch)[0])
    module = LightningModel(model, preprocess, loss_function, learning_rate, momentum)
    fit_callbacks = LightningFitCallbackAdapter(callbacks)
    trainer = pl.Trainer(
        max_epochs=n_epochs,
        default_root_dir=workdir,
        accelerator=accelerator,
        callbacks=[fit_callbacks],
    )
    trainer.fit(
        model=module,
        train_dataloaders=GeneratorIterator(
            lambda: pytorch_utils.multisource_approx_minibatch(sources, source_repeats)
        ),
    )
