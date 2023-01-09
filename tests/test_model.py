#  implement at least a test that checks for a given input with shape X that the output of the model have shape Y
from src.data.make_dataset import CorruptMnist
from src.models.model import MyAwesomeModel
import torch
import pytest

def load_data():
    # dataset = MNIST
    train_set = CorruptMnist(train=True, in_folder="../data/raw", out_folder="data/processed")
    test_set = CorruptMnist(train=False, in_folder="../data/raw", out_folder="data/processed")
    return train_set, test_set


def test_input_shape():
    train_set, test_set = load_data()
    assert train_set[0][0].shape == torch.Size([1,28,28]), "Training dataset does not have the correct torch.Size of [1,28,28]"
    assert test_set[0][0].shape == torch.Size([1,28,28]), "Testing dataset does not have the correct torch.Size of [1,28,28]"


def test_output_shape():
    train_set, _ = load_data()
    imgs = train_set[0][0]
    model = MyAwesomeModel()
    imgs = torch.tensor(imgs.reshape(-1, 1, 28, 28), dtype=torch.float)
    log_probs = model(imgs)
    probs = log_probs.softmax(dim=-1)
    assert probs.shape == torch.Size([1,10]), "The output does not have a size of [1,10]."


def test_error_on_wrong_shape():
    model = MyAwesomeModel()
    with pytest.raises(ValueError, match='Expected input to a 4D tensor'):
        model(torch.randn(1,2,3))