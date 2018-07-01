import tensorflow as tf
import matplotlib.pyplot as plt # Visualizacion del conjunto de datos
import numpy as np              # Biblioteca de Python numerica de bajo nivel
import pandas as pd             # Biblioteca de Python numerica de alto nivel

# Create a graph.
g = tf.Graph()

# Establish the graph as the "default" graph.
with g.as_default():
  # Assemble a graph consisting of the following three operations:
  #   * Two tf.constant operations to create the operands.
  #   * One tf.add operation to add the two operands.
  x = tf.constant(8, name="x_const")
  y = tf.constant(5, name="y_const")
  sum = tf.add(x, y, name="x_y_sum")

  # Task 1: Define a third scalar integer constant z.
  z = tf.constant(4, name="z_const")
  # Task 2: Add z to `sum` to yield a new sum.
  new_sum = tf.add(sum, z, name="x_y_z_sum")

  # Now create a session.
  # The session will run the default graph.
  with tf.Session() as sess:
    print "Sum evaluation: ", sum.eval()
    print "Another sum evaluation: ", new_sum.eval()