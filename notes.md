Building an image from the dockerfile:
- docker build -f trainer.dockerfile . -t trainer:latest
- docker build -f predict.dockerfile . -t predict:latest

Run a container for image trainer:latest, named experiment1
- docker run --name experiment1 trainer:latest
- docker run --name predict1 predict:latest

To run container and auto move files:
- docker run --name experimentTransfer -v ${PWD}/models:/models/ trainer:latest 


Correct argumentss for prediction:
- docker run --name predictA --rm predict:latest ../../models/trained_model.pt ../../src/data/test.npz
