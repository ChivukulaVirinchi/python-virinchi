# Load and prepare CIFAR-10 data. For a detailed description of the CIFAR-10
# file format, see: https://www.cs.toronto.edu/~kriz/cifar.html
import numpy as np

CIFAR_DIRECTORY = '../data/cifar-10-batches-py/'


# Read a CIFAR-10 dictionary. Amongst others, the dictionary includes a "data"
# entry and a "labels" entry. Both are NumPy arrays.
def read_cifar_dictionary(filename):
    import pickle
    with open(filename, 'rb') as f:
        return pickle.load(f, encoding='bytes')


# Insert a column of 1s in the position 0 of a matrix X.
# (“axis=1” stands for: “insert a column, not a row”)
def prepend_bias(X):
    return np.insert(X, 0, 1, axis=1)


# Take a matrix with a single column containing a class label (0 to 9), and
# convert it to a matrix with the same number of rows, and ten one hot encoded
# columns.
def one_hot_encode(Y):
    n_labels = Y.shape[0]
    n_classes = 10
    one_hot_encoded_Y = np.zeros((n_labels, n_classes))
    for i in range(n_labels):
        label = Y[i]
        one_hot_encoded_Y[i][label] = 1
    return one_hot_encoded_Y


# Load training data and return it as two matrices: one matrix for images (that
# includes a bias column), and one matrix for labels (one hot encoded)
def load_training_data():
    import glob
    path = CIFAR_DIRECTORY + 'data_batch_*'
    cifar_training_sets = [read_cifar_dictionary(filename) for
                           filename in glob.glob(path)]
    training_images = [cifar_set[b'data'] for cifar_set in cifar_training_sets]
    training_labels = [cifar_set[b'labels'] for cifar_set in
                       cifar_training_sets]
    X_without_bias = np.concatenate(training_images, axis=0)
    X = np.insert(X_without_bias, 0, 1, axis=1)
    Y_array = np.concatenate(training_labels, axis=0)
    Y = np.reshape(Y_array, (-1, 1))
    return (X, Y)


# Load test data and return it as two matrices: one matrix for images (that
# includes a bias column), and one matrix for labels (*not* one hot encoded)
def load_test_data():
    cifar_test_set = read_cifar_dictionary(CIFAR_DIRECTORY + 'test_batch')
    X_without_bias = cifar_test_set[b'data']
    X = np.insert(X_without_bias, 0, 1, axis=1)
    Y_list = cifar_test_set[b'labels']
    Y = np.reshape(Y_list, (-1, 1))
    return (X, Y)


###############
# Training data
###############

# X has 50 thousands lines (one per example), and 3073 columns (one per pixel
# in each of the red, green, and blue channels, plus 1 column for the bias).
#
# Y has 50 thousands lines (one per example), and 1 column containing a value
# for the label, from 0 to 9.
#
# The one-hot-encoded version of Y has 50 thousands lines (one per example),
# and 10 columns (for 10 one-hot encoded labels).
X_train, Y_train_unencoded = load_training_data()
Y_train = one_hot_encode(Y_train_unencoded)

###########
# Test data
###########

# X has 10 thousands lines (one per example), and 3073 columns (the same as
# the training X).
#
# Y has 10 thousands lines (one per example), and 1 column containing a value
# for the label, from 0 to 9.
X_test, Y_test = load_test_data()
