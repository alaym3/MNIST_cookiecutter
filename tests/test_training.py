# # implement at least one test that asserts something about your training script.

# from src.data.make_dataset import CorruptMnist
# import torch

# def load_data():
#     # dataset = MNIST
#     train_set = CorruptMnist(train=True, in_folder="../data/raw", out_folder="data/processed")
#     test_set = CorruptMnist(train=False, in_folder="../data/raw", out_folder="data/processed")
#     return train_set, test_set

# def test_data():
#     train_set, test_set = load_data()
#     assert len(train_set) == 40000
#     assert len(test_set) == 5000
#     # assert shape


# def test_datapoint_shape():
#     train_set, test_set = load_data()
#     assert train_set[0][0].shape == torch.Size([1,28,28])
#     assert test_set[0][0].shape == torch.Size([1,28,28])

# def test_label_rep():
#     train_set, _ = load_data()
#     torch.unique(train_set.targets) == 9


# def loading_training():
#     train_set = CorruptMnist(train=True, in_folder="data/raw", out_folder="data/processed")
#     dataloader = torch.utils.data.DataLoader(train_set, batch_size=128)
#     optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
#     criterion = torch.nn.CrossEntropyLoss()

#     n_epoch = 5
#     for epoch in range(n_epoch):
#         loss_tracker = []
#         for batch in dataloader:
#             optimizer.zero_grad()
#             x, y = batch
#             preds = model(x.to(device))
#             loss = criterion(preds, y.to(device))
#             loss.backward()
#             optimizer.step()
#             loss_tracker.append(loss.item())


# def training():
