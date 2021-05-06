import nn

class PerceptronModel(object):
    def __init__(self, dimensions):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dimensions` is the dimensionality of the data.
        For example, dimensions=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dimensions)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 1 parte 1/3
        # PERCEPTRON 

        dotProduct = nn.DotProduct(x, self.w)
        return dotProduct

    def get_prediction(self, x):
        """
        Calculates the predicted class for a single data point `x`.

        Returns: 1 or -1
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 1 parte 2/3
        # PERCEPTRON 

        dotProduct = self.run(x)
        dotAsScalar = nn.as_scalar(dotProduct)

        if dotAsScalar >= 0:
            return 1
        else:
            return -1

    def train(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 1 parte 3/3
        # PERCEPTRON 

        numberWrong = 1 # Poner a 1 sólo para entrar en un bucle
        batchSize = 1

        while numberWrong > 0:
            numberWrong = 0 # Restablece el número erróneo después de cada lote (batch)

            for x, y in dataset.iterate_once(batchSize):
                if self.get_prediction(x) != nn.as_scalar(y):
                    self.w.update (x, nn.as_scalar(y))
                    numberWrong = numberWrong + 1


class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        # EJERCICIO 2 parte 1/4
        # REGRESION NO LINEAL

        self.batch_size = 1
        self.w1 = nn.Parameter(1, 20)
        self.w2 = nn.Parameter(20, 1)
        self.b1 = nn.Parameter(1, 20)
        self.b2 = nn.Parameter(20, 1)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 2 parte 2/4
        # REGRESION NO LINEAL

        firstLayer = nn.Linear(x, self.w1)
        firstLayerB = nn.AddBias(firstLayer, self.b1)
        firstLayerBNozero = nn.ReLU(firstLayerB)
        
        secondLayer = nn.Linear(firstLayerBNozero, self.w2)
        return nn.AddBias(secondLayer, self.b2)

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 2 parte 3/4
        # REGRESION NO LINEAL

        return nn.SquareLoss(self.run(x), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 2 parte 4/4
        # REGRESION NO LINEAL

        numbeWrong = 1 # Poner a 1 sólo para entrar en el bucle
        while numbeWrong > 0:
            numbeWrong = 0 #  Restablecer el número incorrecto después de cada lote

            # y es la predicción correcta. Por lo tanto, la actualización si el perceptrón se equivoca
            for x, y in dataset.iterate_once(self.batch_size):

                # crear un objeto de pérdida
                loss = self.get_loss(x, y)

                # hacer un gradiente basado en la pérdida con respecto a los parámetros
                gradWrtW1, gradWrtW2, gradWrtB1, gradWrtB2 = nn.gradients (loss, [self.w1, self.w2, self.b1, self.b2])

                if nn.as_scalar(self.get_loss (nn.Constant(dataset.x), nn.Constant(dataset.y))) >= 0.02:
                    self.w1.update(gradWrtW1, -0.009)
                    self.b1.update(gradWrtB1, -0.009)
                    self.w2.update(gradWrtW2, -0.009)
                    self.b2.update(gradWrtB2, -0.009)

                    numbeWrong = numbeWrong + 1



class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        # EJERCICIO 3 parte 1/4
        # CLASIFICACIÓN DE DÍGITOS

        # Aunque no lo pone en la practica hay que añadir esto de nuevo para que funcione
        self.batch_size = 3

        self.w1 = nn.Parameter(784, 200)
        self.w2 = nn.Parameter(200, 10)
        self.b1 = nn.Parameter(1, 200)
        self.b2 = nn.Parameter(1, 10)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 3 parte 2/4
        # CLASIFICACION DE DIGITOS

        firstLayer = nn.Linear(x, self.w1)
        firstLayerB = nn.AddBias(firstLayer, self.b1)
        firstLayerBNozero = nn.ReLU(firstLayerB)
        secondLayer = nn.Linear(firstLayerBNozero, self.w2)

        return nn.AddBias (secondLayer, self.b2)

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 3 parte 3/4
        # CLASIFICACION DE DIGITOS
        # Esta parte no la pide expresamente en la práctica pero creo que tengo que añadirla

        return nn.SoftmaxLoss(self.run(x), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 3 parte 4/4
        # CLASIFICACIÓN DE DIGITOS
        # En la simulación no sé si será normal pero ha tardado muchísimo en acabar
        # el 5 era el número que al principio ha tardado más

        numberWrong = 1
        while numberWrong > 0:
            numberWrong = 0

            for x, y in dataset.iterate_once(self.batch_size):
                loss = self.get_loss(x,y)
                gradWrtW1, gradWrtW2, gradWrtB1, gradWrtB2 = nn.gradients(loss, [self.w1, self.w2, self.b1, self.b2])

                print(dataset.get_validation_accuracy())
                if dataset.get_validation_accuracy() <0.97:

                   #  0,05 es un ajuste excesivo, al igual que 0,01, por lo que es necesario reducirlo
                   self.w1.update(gradWrtW1, -0.007)
                   self.w2.update(gradWrtW2, -0.007)
                   self.b1.update(gradWrtB1, -0.007)
                   self.b2.update(gradWrtB2, -0.007)

                   numberWrong = numberWrong + 1


class LanguageIDModel(object):
    """
    A model for language identification at a single-word granularity.

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Our dataset contains words from five different languages, and the
        # combined alphabets of the five languages contain a total of 47 unique
        # characters.
        # You can refer to self.num_chars or len(self.languages) in your code
        self.num_chars = 47
        self.languages = ["English", "Spanish", "Finnish", "Dutch", "Polish"]

        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        # EJERCICIO 4 parte 1/4
        # IDENTIFICACION LINGUISTICA

        self.hidden_size = 300
        self.learning_rate =  0.3

        self.w_one = nn.Variable(self.num_chars, self.hidden_size)
        self.w_two = nn.Variable(self.hidden_size, 5)
        self.w_three = nn.Variable(self.hidden_size, 5)
        self.w_four = nn.Variable(5, self.hidden_size)

    def run(self, xs):
        """
        Runs the model for a batch of examples.

        Although words have different lengths, our data processing guarantees
        that within a single batch, all words will be of the same length (L).

        Here `xs` will be a list of length L. Each element of `xs` will be a
        node with shape (batch_size x self.num_chars), where every row in the
        array is a one-hot vector encoding of a character. For example, if we
        have a batch of 8 three-letter words where the last word is "cat", then
        xs[1] will be a node that contains a 1 at position (7, 0). Here the
        index 7 reflects the fact that "cat" is the last word in the batch, and
        the index 0 reflects the fact that the letter "a" is the inital (0th)
        letter of our combined alphabet for this task.

        Your model should use a Recurrent Neural Network to summarize the list
        `xs` into a single node of shape (batch_size x hidden_size), for your
        choice of hidden_size. It should then calculate a node of shape
        (batch_size x 5) containing scores, where higher scores correspond to
        greater probability of the word originating from a particular language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
        Returns:
            A node with shape (batch_size x 5) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        

    def get_loss(self, xs, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 5). Each row is a one-hot vector encoding the correct
        language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
            y: a node with shape (batch_size x 5)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"

