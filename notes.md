Building an image from the dockerfile:
- docker build -f trainer.dockerfile . -t trainer:latest
- docker build -f predict.dockerfile . -t predict:latest

Run a container for image trainer:latest, named experiment1
- docker run --name experiment1 trainer:latest
- docker run --name predict1 predict:latest

To run container and auto move files:
- docker run --name experimentTransfer -v ${PWD}/models:/models/ trainer:latest 



docker run --name predictA --rm \
    -v ${PWD}/trained_model.pt:/models/trained_model.pt \  
    -v ${PWD}/data/example_images.npy:/example_images.npy \ 
    predict:latest \
    ../../models/trained_model.pt \ 
    ../../example_images.npy



docker run --name predictAA --rm \
-v ${PWD}/trained_model.pt:/models/trained_model.pt && \ 
-v ${PWD}/data/example_images.npy:/example_images.npy \ 
predict:latest

docker run --name predictAA --rm \
-v ${PWD}/data/example_images.npy:/example_images.npy \ 
    predict:latest


docker run --name predictA1 --rm 
    predict:latest \
    ../../models/trained_model.pt \ 
    ../../example_images.npy


Correct args for prediction:
docker run --name predictA --rm predict:latest ../../models/trained_model.pt ../../src/data/test.npz
docker run --name predictA --rm predict:latest ../../models/trained_model.pt ../../src/data/test_images.pt


docker run --name predictAA --rm -v ${PWD}/trained_model.pt:/models/trained_model.pt -v ${PWD}/data/example_images.npy:/example_images.npy predict:latest


docker run --name predictA --rm predict:latest ../../models/trained_model.pt ../../src/data/example_images.npz