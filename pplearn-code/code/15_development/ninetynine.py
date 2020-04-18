# This configuration hits 99% precision on MNIST. It passes that number for the
# first time at 20 epochs, but then it drops a bit lower for a while. After 60
# epochs, it gets back up over 99%, and it just stays there.

import neural_network_quieter as nn
import mnist_standardized as data
nn.train(data.X_train, data.Y_train, data.X_test, data.Y_test,
         n_hidden_nodes=1200, epochs=100, batch_size=600, lr=0.8)
