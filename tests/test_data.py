## test that the data has been loaded correctly
from src.data.make_dataset import CorruptMnist
import torch
import os.path
import pytest


def load_data():
    train_set = CorruptMnist(train=True, in_folder="data/raw", out_folder=None)
    test_set = CorruptMnist(train=False, in_folder="data/raw", out_folder=None)
    return train_set, test_set


# file_path = "../data/raw"
# @pytest.mark.skipif(not os.path.exists(file_path), reason="Data files not found")


def test_data_sample_sizes():
    train_set, test_set = load_data()
    assert (
        len(train_set) == 40000
    ), "Training dataset did not have the correct number of samples"
    assert (
        len(test_set) == 5000
    ), "Testing dataset did not have the correct number of samples"
    # assert shape


def test_datapoint_shape():
    train_set, test_set = load_data()
    assert train_set[0][0].shape == torch.Size(
        [1, 28, 28]
    ), "Training dataset does not have the correct torch.Size of [1,28,28]"
    assert test_set[0][0].shape == torch.Size(
        [1, 28, 28]
    ), "Testing dataset does not have the correct torch.Size of [1,28,28]"


def test_labels():
    train_set, _ = load_data()
    torch.unique(
        train_set.targets
    ) == 9, "The targets do not have 9 unique values as required."


train_set, test_set = load_data()


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("len(train_set)", 40000),
        ("len(test_set)", 5000),
        ("train_set[0][0].shape", torch.Size([1, 28, 28])),
        ("test_set[0][0].shape", torch.Size([1, 28, 28])),
    ],
)
def test_parametrize_eval(test_input, expected):
    assert eval(test_input) == expected
